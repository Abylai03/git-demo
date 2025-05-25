#!/bin/bash

# Установка зависимостей
echo "Установка зависимостей..."
pip install -r requirements.txt

# Проверка наличия FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Устанавливаю ffmpeg..."
    brew install ffmpeg  # или apt install ffmpeg
fi

# Создание папки для логов
mkdir -p logs

# Запуск Python-приложения
echo "Запуск конвертера..."
python index.py