# Use Python base image
FROM python:3.9-slim

# Set the working directory in the Docker container for the project
WORKDIR /app

# Copy all files from the local machine to the Docker container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the wtw.sh script executable
RUN chmod +x /app/wtw.sh

# Set the entry point to the wtw.sh script
CMD ["/app/wtw.sh"]
