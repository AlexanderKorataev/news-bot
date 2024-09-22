# Используем официальный образ Python
FROM python:3.11

RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

# Команда для запуска бота
CMD ["python", "main.py"]
