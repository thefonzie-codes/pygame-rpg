FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libportmidi-dev \
    libx11-dev \
    libxcursor-dev \
    xvfb \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo '#!/bin/bash\n\
Xvfb :99 -screen 0 1280x720x24 -ac &\n\
export DISPLAY=:99\n\
python main.py\n' > /start.sh && chmod +x /start.sh

# Command to run the game
CMD ["/start.sh"]
