# https://habr.com/ru/articles/1015148/
# Routers — отвечают только за маршрутизацию и HTTP-ответы.
# Schemas — валидация входящих данных и сериализация ответов.
# Models — описание таблиц в базе данных.
# Services — бизнес-логика, которая может переиспользоваться.
# Core — конфигурация, утилиты, зависимости.
# У вас неправильная логика работы с refresh-токеном, он должен быть одноразовым и содержать уникальный идентификатор, позволяющий различить сессии одного пользователя.
# Новый refresh-токен выдаётся каждый раз при выдаче access-токена. Информация о выданном refresh-токене сохраняется в базе данных.
# При попытке обновления access-токена проверяется не только то, что refresh-токен действителен, но и то, что он есть в базе (сессия пользователя не сброшена) и ещё не использовался.
# Если refresh-токена нет в базе, то требуется аутентификация по логину/паролю.
# Если refresh-токен уже использовался, то предполагается несанкционированный доступ и из базы удаляются все refresh-токены пользователя, что приводит к необходимости его повторной аутентификации во всех сессиях по завершению действия их access-токенов.
# Если refresh-токен в порядке, то он отмечается в базе как использованный и выдаётся новая пара токенов (access + refresh).
# Периодически база очищается от старых refresh-токенов, скажем с возрастом больше двойного срока действия.

import uvicorn
from fastapi import FastAPI

from app.models.database import Base, engine
from app.routers import auth, users

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Demo JWT",
    description="Демонстрация авторизации на FastAPI",
    version="1.0.0"
)
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI JWT Auth API"}

if __name__ == '__main__':
    uvicorn.run(app="app.main:app", reload=True)

#
#   "login": "string",
#   "email": "user@example.com",
#   "password": "string",
#   "full_name": "string"


