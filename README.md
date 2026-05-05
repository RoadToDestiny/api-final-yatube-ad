# API для Yatube

Это REST API для социальной сети Yatube, созданный с использованием Django и Django REST Framework.

## Описание

API предоставляет функционал для управления постами, комментариями, группами и подписками в социальной сети Yatube. Приложение использует JWT-токены для аутентификации и предоставляет полный набор CRUD операций для основных сущностей.

### Основные возможности:

- **Посты**: Создание, чтение, обновление и удаление постов
- **Комментарии**: Управление комментариями к постам
- **Группы**: Просмотр и фильтрация постов по группам
- **Подписки**: Управление подписками на других пользователей
- **Аутентификация**: JWT-токены для защиты API
- **Права доступа**: Гибкая система разрешений для разных типов пользователей

## Установка

### Требования

- Python 3.8+
- pip

### Шаги установки

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/api-final-yatube-ad.git
cd api-final-yatube-ad
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# или
source venv/bin/activate  # Linux/Mac
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
cd yatube_api
python manage.py migrate
```

5. Создайте суперпользователя (необязательно):
```bash
python manage.py createsuperuser
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

Сервер будет доступен по адресу `http://127.0.0.1:8000/`

## Документация API

Интерактивная документация API доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

## Примеры использования API

### Получение JWT-токена

```bash
curl -X POST http://127.0.0.1:8000/api/v1/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

Ответ:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Получение списка постов

```bash
curl http://127.0.0.1:8000/api/v1/posts/
```

### Создание поста (требуется аутентификация)

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Мой первый пост!",
    "group": 1
  }'
```

### Получение подписок (требуется аутентификация)

```bash
curl http://127.0.0.1:8000/api/v1/follow/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Подписка на пользователя (требуется аутентификация)

```bash
curl -X POST http://127.0.0.1:8000/api/v1/follow/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"following": "username_to_follow"}'
```

### Добавление комментария к посту

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/1/comments/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text": "Отличный пост!"}'
```

## Структура проекта

```
yatube_api/
├── api/                    # Django приложение для API
│   ├── models.py          # Пустой файл (модели в posts/)
│   ├── serializers.py     # Сериализаторы для моделей
│   ├── views.py           # ViewSets для обработки запросов
│   ├── urls.py            # URL конфигурация
│   ├── permissions.py     # Пользовательские разрешения
│   └── admin.py           # Django admin конфиг
├── posts/                  # Django приложение для моделей
│   ├── models.py          # Модели: Post, Comment, Group, Follow
│   ├── admin.py           # Django admin конфиг
│   └── migrations/        # Миграции БД
├── yatube_api/            # Основная конфигурация проекта
│   ├── settings.py        # Настройки Django
│   ├── urls.py            # Главная URL конфигурация
│   └── wsgi.py            # WSGI конфигурация
└── manage.py              # Скрипт управления Django
```

## Модели данных

### Post
- `id` - Уникальный идентификатор (автоматический)
- `author` - Автор поста (ForeignKey на User)
- `text` - Текст поста
- `pub_date` - Дата публикации (автоматически устанавливается)
- `image` - Изображение (опционально)
- `group` - Группа поста (опционально, ForeignKey на Group)

### Comment
- `id` - Уникальный идентификатор (автоматический)
- `author` - Автор комментария (ForeignKey на User)
- `post` - Пост, к которому относится комментарий (ForeignKey на Post)
- `text` - Текст комментария
- `created` - Дата создания (автоматически устанавливается)

### Group
- `id` - Уникальный идентификатор (автоматический)
- `title` - Название группы
- `slug` - URL-дружественный идентификатор
- `description` - Описание группы

### Follow
- `user` - Подписчик (ForeignKey на User)
- `following` - Пользователь, на которого подписаны (ForeignKey на User)

## Endpoints API

### Posts
- `GET /api/v1/posts/` - Список всех постов (с пагинацией)
- `POST /api/v1/posts/` - Создать новый пост (требуется аутентификация)
- `GET /api/v1/posts/{id}/` - Получить пост по ID
- `PUT /api/v1/posts/{id}/` - Обновить пост полностью (только для автора)
- `PATCH /api/v1/posts/{id}/` - Частичное обновление поста (только для автора)
- `DELETE /api/v1/posts/{id}/` - Удалить пост (только для автора)

### Comments
- `GET /api/v1/posts/{post_id}/comments/` - Список комментариев к посту
- `POST /api/v1/posts/{post_id}/comments/` - Создать комментарий (требуется аутентификация)
- `GET /api/v1/posts/{post_id}/comments/{id}/` - Получить комментарий по ID
- `PUT /api/v1/posts/{post_id}/comments/{id}/` - Обновить комментарий (только для автора)
- `PATCH /api/v1/posts/{post_id}/comments/{id}/` - Частичное обновление (только для автора)
- `DELETE /api/v1/posts/{post_id}/comments/{id}/` - Удалить комментарий (только для автора)

### Groups
- `GET /api/v1/groups/` - Список всех групп
- `GET /api/v1/groups/{id}/` - Получить группу по ID

### Follow (требуется аутентификация)
- `GET /api/v1/follow/` - Список подписок текущего пользователя (с поиском)
- `POST /api/v1/follow/` - Подписаться на пользователя

### JWT
- `POST /api/v1/jwt/create/` - Получить JWT токен
- `POST /api/v1/jwt/refresh/` - Обновить JWT токен
- `POST /api/v1/jwt/verify/` - Проверить JWT токен

## Права доступа

- **Неаутентифицированные пользователи**: Могут только читать посты, комментарии и группы
- **Аутентифицированные пользователи**: Могут создавать посты и комментарии, читать все данные
- **Авторы контента**: Могут редактировать и удалять только свой контент
- **Подписки**: Доступны только аутентифицированным пользователям

## Тестирование

Для запуска тестов используйте:

```bash
pytest
```

Для запуска тестов с подробным выводом:

```bash
pytest -v
```

Коллекция запросов для Postman находится в директории `postman_collection/`.

## Использование Postman

1. Откройте Postman
2. Импортируйте коллекцию из файла `postman_collection/API_for_yatube.postman_collection.json`
3. Установите переменные окружения (если требуется)
4. Выполняйте запросы из коллекции

## Технологии

- Django 3.2.16
- Django REST Framework 3.12.4
- djangorestframework-simplejwt 4.7.2
- django-filter 2.4.0
- Pillow 9.3.0
- SQLite3 (база данных по умолчанию)

## Лицензия

Этот проект распространяется под лицензией MIT.

## Контакты

По вопросам и предложениям обращайтесь к разработчикам проекта.
