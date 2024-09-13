# Проект Foodgram
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
## Описание
Хотите делиться любимыми рецептами с друзьями и руки чешутся, чтобы взять и приготовить что-то вкусное? Тогда Фудграмм - ваша любимая соцсеть. Как инста, только для еды (и только еды).

## Основные особенности
- Готовая аутентификация пользователей
- Создание рецептов
- Поиск рецептов

## Стек использованных технологий
+ Django 3.2
+ JWT
+ Python 3.9
+ DRF
+ PostgreSQL 13.10
+ Docker

### Для успешного развертывания проекта необходимо в главной директории создать файл .env, где будут указаны следующие параметры:

- POSTGRES_USER=foodgram_user
- POSTGRES_PASSWORD=foodgram_password
- POSTGRES_DB=foodgram_db
- DB_NAME=foodgram
- DB_HOST=db
- DB_PORT=5432
- SECRET_KEY=somesecretkey
- ALLOWED_HOSTS=127.0.0.1,localhost,ваш_доменный_адрес,ваш_IP_адрес
- DEBUG=False
- USE_SQLITE=False (параметр для быстрой смены БД с PostgreSQL на SQLite)

### Тестовые доступы
https://foodgram.learnguide.io
admin@admin.ru
admin11