# Task management app

Приложение для управления задачами.

- Бэкенд написан на [Python](https://www.python.org/) и [FastAPI](https://fastapi.tiangolo.com/)
- Фронтенд написан на [SvelteKit](https://kit.svelte.dev/)
- База данных: [PostgreSQL](https://www.postgresql.org/)
- Контейнеризован с помощью докера [Docker](https://www.docker.com/)
- Оркестрирован при помощи [Docker Compose](https://docs.docker.com/compose/)
- CI/CD при помощи [GitHub Actions](https://github.com/features/actions)

## Разработка

### Бэкенд

Ознакомьтесь с [README](services/backend/README.md) для получения инструкций по разработке бэкэнда.

### Фронтенд

Ознакомьтесь с [README](services/frontend/README.md) для получения инструкций по разработке фронтенда.

## Сборка

Чтобы собрать приложение, выполните:

```bash
docker-compose build
```

## Запуск

Чтобы запустить приложение, выполните:

```bash
docker-compose up
```

Приложение будет доступно на [http://localhost:3000](http://localhost:3000).

## Разработчики

- [witelokk](https://github.com/witelokk)
- [benzlokzik](https://github.com/benzlokzik)
