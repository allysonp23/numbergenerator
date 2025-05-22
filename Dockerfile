# Dockerfile for Django + Celery using Redis broker
FROM python:3.12-slim

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev postgresql-client --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Default command: run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
