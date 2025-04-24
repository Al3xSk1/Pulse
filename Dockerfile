# Dockerfile
FROM python:3.13.3-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Entrypoint is handled by docker-compose `command`
