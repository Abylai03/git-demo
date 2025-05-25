# RTMP → RTSP Конвертер

## Описание

Данный проект — это конвертер видеопотоков из формата RTMP в RTSP.

- Принимает RTMP-потоки
- Конвертирует в RTSP с помощью FFmpeg
- Отдаёт RTSP-потоки для клиентов (например, VLC или ffplay)

---

## Зависимости

Убедитесь, что у вас установлены:

- Python 3.10+
- FFmpeg
- VLC или ffplay (для проверки RTSP-потока)

### Установка зависимостей

#### macOS:

```bash
brew install ffmpeg vlc

Ubuntu/Debian:
bash

sudo apt update
sudo apt install ffmpeg vlc

Структура проекта

rtmp-to-rtsp-project/
├── rtmp_to_rtsp_converter.py       # основной Python-скрипт
├── config.yaml                     # конфигурация входных/выходных потоков
├── requirements.txt                # зависимости Python
├── install_and_run.sh              # установочный скрипт
├── README.md                       # документация
└── logs/                          # директория для логов

Конфигурация потоков

Настройте файл config.yaml, указав нужные RTMP- и RTSP-адреса:
yaml

streams:
  - id: cam1
    input: rtmp://example.com/live/cam1
    output: rtsp://localhost:8554/cam1

  - id: cam2
    input: rtmp://example.com/live/cam2
    output: rtsp://localhost:8554/cam2

Где:

    input — RTMP-источник

    output — адрес, по которому поток будет доступен по RTSP

    Совет: Если у вас нет настоящих RTMP-потоков, вы можете:

        передавать RTMP из OBS Studio на локальный сервер

        использовать публичные RTMP-потоки

        или сымитировать поток с помощью FFmpeg

Запуск проекта

    Сделайте скрипт исполняемым:

bash

chmod +x install_and_run.sh

    Запустите:

bash

./install_and_run.sh

Скрипт выполнит:

    установку зависимостей (pyyaml)

    проверку наличия FFmpeg

    запуск rtmp_to_rtsp_converter.py

    создание логов в папке logs/

Проверка RTSP-потока
Способ 1: VLC

    Запустите VLC

    Меню → "Открыть сетевой поток"

    Введите:

    rtsp://localhost:8554/cam1

    Нажмите "Play"

Способ 2: ffplay
bash

ffplay rtsp://localhost:8554/cam1

Логирование

Все логи потоков сохраняются в logs/:

    logs/cam1.log

    logs/cam2.log

    logs/stream_manager.log

Логи включают сообщения об ошибках, статусах запуска и остановки потоков.
```
