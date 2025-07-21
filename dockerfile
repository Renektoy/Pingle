# Use an official Python base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Copy the rest of the application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the devices script
CMD ["python", "devices.py"]
