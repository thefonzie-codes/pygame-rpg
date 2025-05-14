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

ENV SDL_VIDEODRIVER=x11
ENV DISPLAY=:99

CMD CMD xvfb-run -s "-screen 0 1280x720x24" python main.py

