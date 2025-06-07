FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for tesseract and pdf processing
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    openjdk-17-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create required directories and set permissions
RUN mkdir -p input output datasets && \
    chmod 777 input output datasets

# Expose port for the application
EXPOSE 7860

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Start command - runs only FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"] 