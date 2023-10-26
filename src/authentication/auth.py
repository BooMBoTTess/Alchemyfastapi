from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend


SECRET = "SECRET"
#стратегия
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

#хранилище
cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name='Ucookie')

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
