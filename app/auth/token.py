from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone

SECRET_KEY = "Clave"
ALGORITHM = "HS356"

def create_token(data: dict, expires_delta: timedelta = None):
    encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))

    encode.update({"exp": expire})
    return  jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.encode(token, SECRET_KEY, algorithm=ALGORITHM)
        return payload
    except JWTError as e:
        raise Exception(f"Token invalido o expirado: {e}")

