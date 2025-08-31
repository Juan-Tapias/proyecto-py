from fastapi import Depends
from sqlmodel import Session
from ..models.reservation import Reservation, ReservationCreate
from datetime import date
from ..models.database import get_db

def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    new_reservation = Reservation(
        usuario_id=reservation.usuario_id,
        room_id=reservation.room_id,
        fecha=reservation.fecha,
        hora_inicio=reservation.hora_inicio,
        hora_fin=reservation.hora_fin,
        estado=reservation.estado
        )
    
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return {"msg": "Reservacion registrada con éxito", "reservation_id": new_reservation.id}

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

