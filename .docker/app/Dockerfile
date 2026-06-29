FROM python:3.14-slim

# Avoid that python generates .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
  build-essential \
  pkg-config \
  python3-dev \
  libsdl2-dev \
  libsdl2-image-dev \
  libsdl2-mixer-dev \
  libsdl2-ttf-dev \
  libfreetype6-dev \
  libpulse0 \
  pulseaudio-utils \
  && rm -rf /var/lib/apt/lists/*

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