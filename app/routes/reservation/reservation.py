from fastapi import APIRouter, Depends
from sqlmodel import Session
from ...controllers.reservation.reservation_controllers import create_reservation, get_reservation_by_user, get_reservation_by_room, get_reservation_by_date, cancel_reservation
from ...models.reservation.reservation import ReservationCreate
from datetime import date
from ...models.database.database import get_db

router = APIRouter(tags=["Reservation"])

@router.post("/create-reservation")
def create_reservations(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return create_reservation(reservation, db)

@router.get("/me")
def get_my_room(user_id: int, db: Session = Depends(get_db)) :
    return get_reservation_by_user(user_id, db)

@router.get("/reservation/room/{room_id}")
def get_room_id(room_id: int, db: Session = Depends(get_db)):
    return get_reservation_by_room(room_id, db)

@router.get("/date/{reservation_date}")
def get_room_date(reservation_date:date, db: Session = Depends(get_db)):
    return get_reservation_by_date(reservation_date, db)

@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return cancel_reservation(reservation_id, db)
 
