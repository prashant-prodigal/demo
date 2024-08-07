# Use a base image with Python installed
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY print_logs.py .

# Run the Python script
CMD ["python", "print_logs.py"]
