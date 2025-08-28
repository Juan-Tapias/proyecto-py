from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta,  timezone
from pydantic import BaseModel
import bcrypt

SECRET_KEY = "Clave_aun_mas_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 30

app = FastAPI()

