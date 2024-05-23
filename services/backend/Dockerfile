# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем обновления и необходимые зависимости
RUN apt-get update && apt-get install -y \
    build-essential

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения в контейнер
COPY . .

# Открываем порт 8000 для доступа к FastAPI
EXPOSE 8000

# Указываем команду для запуска FastAPI приложения
CMD ["uvicorn", "todo.main:app", "--host", "0.0.0.0", "--port", "8000"]
