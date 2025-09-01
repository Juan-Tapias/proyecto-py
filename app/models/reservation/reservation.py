from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, time

class Reservation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int
    room_id: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    estado: str = Field(default="pendiente", max_length=20)


class ReservationCreate(SQLModel):
    usuario_id: int
    room_id: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    estado: str 