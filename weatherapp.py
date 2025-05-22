import streamlit as st
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
)

# Query latest 50 records
df = pd.read_sql("""
    SELECT *
    FROM weatherdata_table
    ORDER BY TIMESTAMP DESC
    LIMIT 50;
""", conn)

st.title("🌤 Real-Time Weather Dashboard")

# Show city dropdown
cities = df['CITY_NAME'].unique()
city = st.selectbox("Select a City", cities)

# Filter and plot
filtered = df[df["CITY_NAME"] == city]

st.line_chart(filtered.set_index("TIMESTAMP")[["TEMP"]], height=300, use_container_width=True)
st.line_chart(filtered.set_index("TIMESTAMP")[["HUMIDITY"]], height=300, use_container_width=True)

st.dataframe(filtered)
