import requests, json
import boto3
import datetime
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1: Fetch from OpenWeather
def fetch_weather(city="London"):
    api_key = os.getenv("OWM_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Step 2: Upload to S3
def upload_to_s3(data, filename):
    s3 = boto3.client("s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION"))

    bucket = os.getenv("S3_BUCKET")
    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=json.dumps(data),
        ContentType="application/json"
    )
    print(f"✅ Uploaded {filename} to S3")

# Step 3: Optional (Transform → Snowflake Structured Table)
def insert_into_snowflake(filename):
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )
    cur = conn.cursor()
    cur.execute(f"""
        INSERT INTO weatherdata_table (
          CITY_NAME, CITY_ID, TIMEZONE, TIMESTAMP,
          COORD_LON, COORD_LAT,
          WEATHER_ID, WEATHER_MAIN, WEATHER_DESCRIPTION, WEATHER_ICON,
          TEMP, FEELS_LIKE, TEMP_MIN, TEMP_MAX, PRESSURE, HUMIDITY, SEA_LEVEL, GRND_LEVEL,
          WIND_SPEED, WIND_DEG, CLOUD_ALL, VISIBILITY,
          SYS_TYPE, SYS_ID, COUNTRY, SUNRISE, SUNSET,
          WIND_GUST, RAIN_1H
        )
        SELECT
          raw:"name"::STRING,
          raw:"id"::INT,
          raw:"timezone"::INT,
          TO_TIMESTAMP_LTZ(raw:"dt"::INT),
          raw:"coord"."lon"::FLOAT,
          raw:"coord"."lat"::FLOAT,
          raw:"weather"[0]."id"::INT,
          raw:"weather"[0]."main"::STRING,
          raw:"weather"[0]."description"::STRING,
          raw:"weather"[0]."icon"::STRING,
          raw:"main"."temp"::FLOAT,
          raw:"main"."feels_like"::FLOAT,
          raw:"main"."temp_min"::FLOAT,
          raw:"main"."temp_max"::FLOAT,
          raw:"main"."pressure"::INT,
          raw:"main"."humidity"::INT,
          raw:"main"."sea_level"::INT,
          raw:"main"."grnd_level"::INT,
          raw:"wind"."speed"::FLOAT,
          raw:"wind"."deg"::INT,
          raw:"clouds"."all"::INT,
          raw:"visibility"::INT,
          raw:"sys"."type"::INT,
          raw:"sys"."id"::INT,
          raw:"sys"."country"::STRING,
          TO_TIMESTAMP_LTZ(raw:"sys"."sunrise"::INT),
          TO_TIMESTAMP_LTZ(raw:"sys"."sunset"::INT),
          raw:"wind"."gust"::FLOAT,
          raw:"rain"."1h"::FLOAT
        FROM weather_json_raw
        WHERE filename = '{filename}';
    """)
    print("✅ Data inserted into structured table")
    cur.close()
    conn.close()

# === Run all steps ===
if __name__ == "__main__":
    data = fetch_weather()
    ts = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    filename = f"weather_data_{ts}.json"
    upload_to_s3(data, filename)
    # Optional insert step if Snowpipe isn't instant:
    # insert_into_snowflake(filename)
