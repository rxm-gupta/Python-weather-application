# Use an official lightweight Python image
FROM python:3.12-slim

#Set the working directory in the container 
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "app.py"] 
