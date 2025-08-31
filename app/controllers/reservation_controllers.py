from fastapi import Depends
from sqlmodel import Session
from ..models.reservation import Reservation
from datetime import date
from ..models.database import get_db

def create_reservation(db: Session, reservation: Reservation):
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

def get_reservation(db: Session = Depends(get_db)):
    return db.query(Reservation).all()

def get_reservation_by_id(reservation_id:int, db: Session  = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def get_reservation_by_user(user_id:int, db: Session  = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.usuario_id == user_id)

def get_reservation_by_room(room_id:int, db: Session  = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.room_id == room_id).first()

def get_reservation_by_date(date:date, db: Session  = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.fecha == date)

def cancel_reservation (reservation_id:int, db: Session  = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if reservation:
        reservation.estado = "cancelada"
        db.commit()
        db.refresh(reservation)
    return reservation

