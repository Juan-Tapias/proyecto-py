from fastapi import APIRouter, Depends, HTTPException
from verificar_administracion import admin_required
from users_verification import get_current_user
from sqlmodel import Session
from models.database import get_db
from controllers.reservation_controllers import create_reservation, get_reservation_by_user, get_reservation_by_room, get_reservation_by_date, cancel_reservation
from models.reservation import Reservation
from datetime import date

router = APIRouter(prefix="/romm", tags=["Rooms"])

@router.post("/")
def create_reservations(db: Session, reservation: Reservation):
    return create_reservation(db, reservation)

@router.get("/")
def get_my_room(db: Session, user_id: int):
    return db.query(Reservation).filter(Reservation.usuario_id == user_id)

@router.get("/")
def get_room_id(db: Session, room_id: int):
    return db.query(Reservation).filter(Reservation.room_id == room_id)

@router.get("/")
def get_room_date(db: Session, date:date):
    return get_reservation_by_date(db, date)

@router.delete("/")
def delete_reservation(db:Session, reservation_id: int):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id)

    if reservation:
        reservation.estado = "cancelada"
        db.commit()
        db.refresh(reservation)
    return reservation
 
