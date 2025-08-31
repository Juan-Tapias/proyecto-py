from sqlmodel import SQLModel, Field
from typing import Optional

class Room(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    sede: str
    capacidad: int
    recursos: str

class RoomCreate(SQLModel):
    nombre: str
    sede: str
    capacidad: int 
    recursos: str