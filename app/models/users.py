from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    contraseña_hash: str
    rol: str = "user"  

class UserCreate(SQLModel):
    nombre: str
    email: str
    password: str 
    rol: str = "user"