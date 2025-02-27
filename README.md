python-weather-application - DevOps Project with Docker

🌍 Overview

This is a DevOps project that containerizes a Python-based weather application using Docker. The application fetches real-time weather data using the OpenWeatherMap API.

🛠 Technologies Used

Python 3.12 (Slim version for optimized containerization)

Docker (Containerization)

OpenWeatherMap API (Weather data)

🚀 Getting Started


1️⃣ We can create an Ubuntu EC2 Instance on AWS and run the below commands to install docker.

```bash
sudo apt update
sudo apt install docker.io -y
```

Start Docker Daemon

To verify if the Docker daemon is running and active, use the following command

```bash
sudo systemctl status docker
```

If the daemon is not running, start it with
```bash
sudo systemctl start docker
```

Grant User Access to Docker

To allow your user to run Docker commands without sudo, add the user to the Docker group
```bash
sudo usermod -aG docker ubuntu
```
Replace ubuntu with your actual username if needed

Note: You must log out and log back in for the changes to take effect.

🎉 Docker is Installed, Up, and Running! 🚀

2️⃣ Clone the Repository
```bash
git clone https://github.com/rxm-gupta/python-weather-application
cd python-weather-application
```

3️⃣ Set Up Environment Variables

Create a .env file in the project root and add your OpenWeatherMap API key
```bash
WEATHER_API_KEY=your_api_key_here
```

4️⃣ Build the Docker Image
```bash
docker build -t python-weather-application .
```
5️⃣ Run the Container
```bash
docker run -it --env-file .env python-weather-application
```

LFG🔥 Our app will now be running🥳🥳



6️⃣ Push the Docker Image

Login to Docker Hub
```bash
docker login
```
Tag your Docker image with your Docker Hub username
```bash
docker tag python-weather-application your-dockerhub-username/python-weather-application:latest
```
Push the Image to Docker Hub
```bash
docker push your-dockerhub-username/python-weather-application:latest
```
7️⃣ Pull the Docker Image

To run the application on another machine, simply pull the image
```bash
docker pull your-dockerhub-username/python-weather-application:latest
```
Then run it
```bash
docker run -it --env-file .env your-dockerhub-username/python-weather-application
```

*************************

📂 Project Structure

📦 python-weather-application
├── 📄 app.py              # Main application file
├── 📄 requirements.txt    # Dependencies
├── 📄 Dockerfile          # Docker instructions
├── 📄 .env.example        # Environment variables 
├── 📄 README.md           # Project documentation


*************************
HOW TO CREATE A requirements.txt FILE

Open Terminal (Linux/Mac) or Command Prompt (Windows).

Navigate to your project folder where app.py is located.

Run:
```bash
sudo apt install python3-pip
pip freeze > requirements.txt
```
This creates a requirements.txt file with all installed dependencies.
**************************


🎯 Happy Coding & DevOps 🚀

