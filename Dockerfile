# File: Dockerfile
# Description: Dockerfile for the backend FastAPI application

# Use official Python image
FROM python:3.11

# Set work directory
WORKDIR /app

# Copy code
COPY . /app

# Install dependencies
RUN pip install fastapi[all] psycopg2-binary

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
