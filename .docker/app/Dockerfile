FROM python:3.14-slim

# Avoid that python generates .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY app/ .

# Expose ports
EXPOSE 5000

# Entrypoint
CMD ["python", "main.py"]