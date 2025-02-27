python-weather-application - DevOps Project with Docker

🌍 Overview

This is a DevOps project that containerizes a Python-based weather application using Docker. The application fetches real-time weather data using the OpenWeatherMap API.

🛠 Technologies Used

Python 3.12 (Slim version for optimized containerization)

Docker (Containerization)

OpenWeatherMap API (Weather data)

🚀 Getting Started

1️⃣ Clone the Repository

git clone https://github.com/yourusername/python-weather-application

cd python-weather-application

2️⃣ Set Up Environment Variables

Create a .env file in the project root and add your OpenWeatherMap API key:

WEATHER_API_KEY=your_api_key_here

3️⃣ Build the Docker Image

docker build -t python-weather-application .

4️⃣ Run the Container

docker run -it --env-file .env python-weather-application


📂 Project Structure

📦 python-weather-application
├── 📄 app.py              # Main application file
├── 📄 requirements.txt    # Dependencies
├── 📄 Dockerfile          # Docker instructions
├── 📄 .env.example        # Environment variables 
├── 📄 README.md           # Project documentation


🎯 Happy Coding & DevOps 🚀

