from fastapi import Depends, HTTPException
from datetime import timedelta, date, time
from sqlmodel import Session
from ...models.reservation.reservation import Reservation, ReservationCreate
from ...models.database.database import get_db

from datetime import datetime, timedelta

def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    base_date = datetime(2000, 1, 1)  
    hora_inicio = datetime.combine(base_date, reservation.hora_inicio)
    hora_fin = datetime.combine(base_date, reservation.hora_fin)

    if hora_fin - hora_inicio != timedelta(hours=1):
        raise HTTPException(
            status_code=400,
            detail="Las reservas deben ser de bloques de 1 hora exacta."
        )

    hora = db.query(Reservation).filter(
        Reservation.room_id == reservation.room_id,
        Reservation.fecha == reservation.fecha,
        Reservation.hora_inicio < reservation.hora_fin,
        Reservation.hora_fin > reservation.hora_inicio
    ).first()

    if hora:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una reserva en este horario para esta sala."
        )

    if not all([reservation.usuario_id, reservation.room_id, reservation.fecha,
                reservation.hora_inicio, reservation.hora_fin, reservation.estado]):
        raise HTTPException(
            status_code=400,
            detail="Todos los campos son obligatorios y no pueden ser nulos."
        )

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
    return db.query(Reservation).filter(Reservation.usuario_id == user_id).all()

def get_reservation_by_room(room_id:int, db: Session  = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.room_id == room_id).first()

def get_reservation_by_date(date:date, db: Session  = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.fecha == date).all()

def cancel_reservation (reservation_id:int, db: Session  = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if reservation:
        reservation.estado = "cancelada"
        db.commit()
        db.refresh(reservation)
    return reservation

