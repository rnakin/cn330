# Dockerfile for HowIs CLI
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Environment variables (optional, can be overridden in compose file or CLI)
ENV IPGEO_API_KEY="YOUR_IPGEO_API_KEY"
ENV WEATHER_API_KEY="YOUR_WEATHER_API_KEY"

# Set entrypoint
ENTRYPOINT ["python", "howis.py"]
