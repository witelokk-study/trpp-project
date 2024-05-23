# Используем официальный образ Python
FROM python:3.12-bookworm

# Устанавливаем обновления и необходимые зависимости
RUN apt-get update && apt-get install -y \
    build-essential

# Устанавливаем Poetry
RUN pip install poetry==1.8.3

# Устанавливаем переменные окружения для Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry install --without dev && rm -rf $POETRY_CACHE_DIR

# Копируем весь код приложения в контейнер
COPY . .

# Открываем порт 8000 для доступа к FastAPI
EXPOSE 8000

# Указываем команду для запуска FastAPI приложения
CMD ["uvicorn", "todo.main:app", "--host", "0.0.0.0", "--port", "8000"]
