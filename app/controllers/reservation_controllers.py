from sqlmodel import Session
from ..models.reservation import Reservation
from datetime import date


def create_reservation(db: Session, reservation: Reservation):
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

def get_reservation(db: Session):
    return db.query(Reservation).all()

def get_reservation_by_id(db: Session, reservation_id:int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def get_reservation_by_user(db: Session, user_id:int):
    return db.query(Reservation).filter(Reservation.usuario_id == user_id)

def get_reservation_by_room(db: Session, room_id:int):
    return db.query(Reservation).filter(Reservation.room_id == room_id).first()

def get_reservation_by_date(db: Session, date:date):
    return db.query(Reservation).filter(Reservation.fecha == date)

def cancel_reservation (db: Session, reservation_id:int):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if reservation:
        reservation.estado = "cancelada"
        db.commit()
        db.refresh(reservation)
    return reservation

