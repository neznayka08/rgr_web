
# 📺 Видеоплатформа

Это проект видеоплатформы с возможностью регистрации, загрузки и просмотра видео.

## 🚀 Запуск проекта

### Backend (Django)
1. Установите зависимости:
```
pip install -r requirements.txt
```

2. Примените миграции:
```
python manage.py migrate
```

3. Запустите сервер:
```
python manage.py runserver
```

### Frontend (React)
1. Перейдите в папку frontend:
```
cd video-platform-frontend
```

2. Установите зависимости:
```
npm install
```

3. Запустите сервер:
```
npm start
```

---

## 🔗 API Документация

Базовый URL:  
`http://127.0.0.1:8000/api/`

---

### 🌐 Общие эндпоинты

#### `GET /api/`
**Описание:** Корневой эндпоинт API  
**Ответ:**
```json
{
  "videos": "http://127.0.0.1:8000/api/videos/",
  "register": "http://127.0.0.1:8000/api/auth/register/",
  "login": "http://127.0.0.1:8000/api/auth/login/"
}
```

---

### 🔐 Аутентификация

#### `POST /api/auth/register/`
**Описание:** Регистрация нового пользователя  
**Запрос:**
```json
{
  "username": "new_user",
  "email": "user@example.com",
  "password": "securepassword",
  "password2": "securepassword"
}
```

#### `POST /api/auth/login/`
**Описание:** Получение JWT-токенов  
**Запрос:**
```json
{
  "username": "new_user",
  "password": "securepassword"
}
```

**Ответ:**
```json
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

---

### 📹 Видео

#### `GET /api/videos/`
**Описание:** Получить список видео  
**Требуется токен**  
**Ответ:**
```json
[
  {
    "id": 1,
    "title": "Пример",
    "description": "Описание",
    "video_file": "http://127.0.0.1:8000/media/videos/example.mp4"
  }
]
```

#### `GET /api/videos/<id>/`
**Описание:** Получить одно видео

---

#### `POST /api/videos/`
**Описание:** Загрузить видео  
**Заголовки:**
- `Authorization: Bearer <access_token>`
- `Content-Type: multipart/form-data`

**Форма:**
- `title`: Название
- `description`: Описание
- `video_file`: Видео-файл

---

## 🗃️ Структура проекта

- `video/` — Django-приложение с моделями, сериализаторами и views
- `video-platform-frontend/` — React-фронтенд
- `media/videos/` — Путь хранения загруженных видео

---

## 📌 Примечания
- Убедитесь, что включены настройки CORS и MEDIA (в `settings.py`)
- Для доступа к видео используйте `video.video_file` в ответе

---

## 👤 Автор
Разработано в рамках проекта видеоплатформы.
