# Use an official Python image as the base
FROM python:3.11-slim

# Install Java (OpenJDK 17)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean

# Set the working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Compile the Java file
RUN javac GeminiImageGenerator.java

# Expose the port your Flask app runs on
EXPOSE 5000

# Set environment variable for Flask (optional, for production)
ENV FLASK_ENV=production

# Start the server
CMD ["python", "server.py"] 