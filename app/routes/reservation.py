from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..controllers.reservation_controllers import create_reservation, get_reservation_by_user, get_reservation_by_room, get_reservation_by_date, cancel_reservation
from ..models.reservation import Reservation
from datetime import date
from ..auth.dependencias import get_current_user

router = APIRouter(tags=["Reservation"])

@router.post("/create-reservation")
def create_reservations(reservation: Reservation, db: Session = Depends(get_current_user)):
    return create_reservation(db, reservation)

@router.get("/me")
def get_my_room(user_id: int, db: Session = Depends(get_current_user)) :
    return get_reservation_by_user(db, user_id)

@router.get("/reservation/room/{room_id}")
def get_room_id(room_id: int, db: Session = Depends(get_current_user)):
    return get_reservation_by_room(db, room_id)

@router.get("/date/{reservation_date}")
def get_room_date(reservation_date:date, db: Session = Depends(get_current_user)):
    return get_reservation_by_date(db, reservation_date)

@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_current_user)):
    return cancel_reservation(db, reservation_id)
 
