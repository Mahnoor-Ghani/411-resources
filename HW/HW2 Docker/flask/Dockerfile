# Use the official Ubuntu 22.04 LTS as the base image
FROM ubuntu:22.04

# Set the working directory inside the container
WORKDIR /app

# Update and install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl  # Added curl for health checks

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install flask

# Set environment variable for port
ENV PORT=5000 

# Expose default Flask port
EXPOSE 5000

# Health check (checks every 30 seconds to see if the endpoint returns a successful response)
HEALTHCHECK --interval=30s --timeout=3s \
 CMD curl -f http://localhost:5000/health || exit 1

# Run the Flask app with dynamic port from ENV
CMD ["python3", "app.py"]

