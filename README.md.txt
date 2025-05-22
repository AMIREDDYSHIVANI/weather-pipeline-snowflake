
# 🌤 Real-Time Weather Data Pipeline

A student-built project that shows how to fetch, store, and visualize real-time weather data using:

- Python
- AWS S3
- Snowflake
- Streamlit

[📚 Explore the docs »](#about-the-project) ·  
[🐛 Report Bug](https://github.com/AMIREDDYSHIVANI/weather-pipeline-snowflake/issues) ·  
[✨ Request Feature](https://github.com/AMIREDDYSHIVANI/weather-pipeline-snowflake/issues)

---

## 📚 Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## 📌 About The Project

This project helps you understand real-time cloud data pipelines. It does four main things:

1. Collects weather data using the OpenWeatherMap API  
2. Stores data in AWS S3 as JSON files  
3. Loads that data into Snowflake using Snowpipe  
4. Displays temperature and humidity on a web dashboard using Streamlit

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [AWS S3](https://aws.amazon.com/s3/)
- [Snowflake](https://www.snowflake.com/)
- [Streamlit](https://streamlit.io/)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

## 🧰 Getting Started

### 📋 Prerequisites

You’ll need Python installed. Then, install required packages:

```bash
pip install -r requirements.txt
````

Also, copy `.env.example` to `.env` and fill in your API keys.

---

### 🔧 Installation

Clone the project to your computer:

```bash
git clone https://github.com/AMIREDDYSHIVANI/weather-pipeline-snowflake.git
cd weather-pipeline-snowflake
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your keys to the `.env` file:

```
OWM_API_KEY=your_openweather_api_key
AWS_ACCESS_KEY=your_aws_key
...
```

---

## 🚀 Usage

To collect and upload data:

```bash
python main.py
```

To see the weather dashboard:

```bash
streamlit run app.py
```

You’ll see live charts showing temperature, humidity, and more.

---

## 🗺️ Roadmap

* ✅ Python automation
* ✅ AWS S3 storage
* ✅ Snowflake ingestion via Snowpipe
* ✅ Streamlit dashboard
* 🔜 Power BI integration (coming soon)

Check [Issues](https://github.com/AMIREDDYSHIVANI/weather-pipeline-snowflake/issues) for features in progress.

---

## 🤝 Contributing

Want to improve it? Awesome!

1. Fork the project
2. Create a new branch:
   `git checkout -b feature/YourFeatureName`
3. Make your changes and commit:
   `git commit -m 'Add your feature'`
4. Push to GitHub:
   `git push origin feature/YourFeatureName`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📬 Contact

**Shivani Reddy**
📎 [LinkedIn](www.linkedin.com/in/shivani-343a32331)
🔗 [GitHub Repo](https://github.com/AMIREDDYSHIVANI/weather-pipeline-snowflake)

---

## 🙏 Acknowledgments

Thanks to the following for inspiration and tools:

* [OpenWeatherMap](https://openweathermap.org/)
* [Streamlit Docs](https://docs.streamlit.io/)
* [Snowflake Docs](https://docs.snowflake.com/)
* [Boto3 Docs](https://boto3.amazonaws.com/)
* [Best README Template](https://github.com/othneildrew/Best-README-Template)

```

---

Let me know if you'd like this turned into a downloadable `README.md` file or want help uploading it to your GitHub repo!
```

