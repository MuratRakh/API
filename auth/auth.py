# Authentication backend состоит из из двух частей:
# Transport(Он управляет тем, как токен будет передан по запросу) и
# Strategy(Он управляет тем, как генерируется и защищается токен.)
# Как транспорт выберем Cookie, как стратегию JWT (скопируем блоки кода из документации)

from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

cookie_transport = CookieTransport(cookie_max_age=3600)

SECRET = "SECRET"   # нужно будет заменить на любой другой, по которому и будет кодироваться токен

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
