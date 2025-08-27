from fastapi import APIRouter, Depends, HTTPException
from verificar_administracion import admin_required
from sqlmodel import Session
from models.database import get_db
from controllers.room_controllers import get_room, create_room, delete_room, update_room
from models.room import Room

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.get("/")
def get_rooms(db: Session = Depends(get_db)):
    return get_room(db)

@router.post("/", dependencies=[Depends(admin_required)])
def create_room_post(room: Room, db: Session = Depends(get_db)):
    return create_room(db, room)

@router.put("/{room_id}", dependencies=[Depends(admin_required)])
def update_room_post(db: Session, room_id: int, room_data: Room):
    return update_room(db, room_id, room_data)

@router.delete("/{room_id}", dependencies=[Depends(admin_required)])
def delete_rooms(db:Session, room_id:int):
    return delete_room(db, room_id)