from pydantic import BaseModel
# Структура JWT
# Токен состоит из трёх частей, разделённых точками:
# header.payload.signature
#
# Header (заголовок) — содержит тип токена и алгоритм подписи:
#
# {
#   "alg": "HS256",
#   "typ": "JWT"
# }
# Payload (полезная нагрузка) — содержит утверждения (claims): информация о пользователе, время выпуска, срок действия и другие данные:
#
# {
#   "sub": "user_id_123",
#   "exp": 1735689600,
#   "iat": 1735603200
# }
# Signature (подпись) — создаётся путём шифрования header и payload с секретным ключом.

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: int