# rtmp_to_rtsp_converter.py

import subprocess
import threading
import yaml
import os
import logging

# --- Настройка логирования ---
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("stream_manager.log"),
        logging.StreamHandler()
    ]
)

# --- Загрузка конфигурации ---
def load_config(path='config.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

# --- Функция запуска потока ---
def start_stream(stream_id, input_url, output_path):
    log_file = open(f"logs/{stream_id}.log", "a")
    command = [
        "ffmpeg", "-re", "-i", input_url,
        "-c:v", "copy", "-f", "rtsp", output_path
    ]
    logging.info(f"Запуск потока {stream_id}: {input_url} -> {output_path}")
    process = subprocess.Popen(command, stdout=log_file, stderr=subprocess.STDOUT)
    return process

# --- Основная функция ---
def main():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    config = load_config()
    threads = []

    for stream in config['streams']:
        t = threading.Thread(
            target=start_stream,
            args=(stream['id'], stream['input'], stream['output'])
        )
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
