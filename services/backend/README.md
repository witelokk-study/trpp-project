# Task management app FastAPI App

REST API для сервиса управления задачами.

## Фичи

- Аутентификация JWT: используется JWT (JSON Web Token) аутентификация для безопасной аутентификации и авторизации пользователей.

- Управление задачами с категориями: пользователи могут создавать задачи и распределять их по категориям для лучшей организации и управления.

- CRUD-операции: пользователи могут выполнять операции создания, чтения, обновления и удаления задач и категорий.

## Требования

- Python 3.11+
- Poetry

## Установка

1. Склонируйте этот репозиторий:

```bash
git clone https://github.com/witelokk-study/trpp-project.git
```

2. Перейдите в каталог проекта:

```bash
cd trpp-project/services/backend/todo
```

3. Установите переменные окружения `POSTGRES_USERNAME`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`, `SECRET_KEY` в файле `.env` (пример `.env.example`).

4. Запустите приложение:

 ```bash
 poetry run python todo.main:app
 ```

## API Эндпоинты

- `POST /auth/`: Создание пользователя
- `POST /auth/token`: Получение токена
- `GET /tasks/`: Получение списка задач
- `POST /tasks/`: Добавления задачи
- `GET /tasks/{task_id}`: Подлучение задачи
- `PATCH /tasks/{task_id}`: Редактирование задачи
- `DELETE /tasks/{task_id}`: Удаление задачи
- `GET /tasks/category/{category_id}`: Получение задачи по категории
- `GET /categories`: Получение списка категорий
- `POST /categories`: Доавбление категории
- `GET /categories/{category_id}`: Получение категории
- `PATCH /categories/{category_id}`: Редактирование категории
- `DELETE /categories/{category_id}`: Удаление категории

Вы можете получить более подробную информацию об этих эндпоинтах, используя документацию по адресу `/docs`.
