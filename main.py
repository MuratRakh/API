# Depends это функция из фреймворка fastapi отвечает за инъекцию зависимостей(добавляет параметры)
# добавляем с документации роутеры(переменные которые аккумулируют в себе какие-то эндпоинты)
# так же импортируем для них auth_backend, get_user_manager, UserRead, UserCreate


from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Depends
from auth.database import User
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

# Создание экземпляра класса FastAPI
app = FastAPI(
    title="GORODA"
)

# Создание экземпляра класса FastAPIUsers
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# Login/Logout
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# Registration
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
#Получение текущего пользователя(можно создать переменную для получения суперюзера,верифицированного и т.д)
current_user = fastapi_users.current_user()

#Создание защищенного эндпоинта
@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

# не защищенного
@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"



