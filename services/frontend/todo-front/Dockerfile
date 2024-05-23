# Этап сборки Svelte-приложения
FROM node:12 AS build

# Создаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package.json ./
COPY package-lock.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы проекта
COPY . ./

# Собираем проект
RUN npm run build

# Этап развертывания на Nginx
FROM nginx:1.19-alpine

# Копируем собранные файлы из предыдущего этапа в директорию Nginx
COPY --from=build /app/public /usr/share/nginx/html

# Копируем файл конфигурации Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Открываем порт 80
EXPOSE 80

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]
