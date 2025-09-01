from fastapi import APIRouter, Depends
from ..verification.verificar_administracion import admin_required
from sqlmodel import Session
from ...models.database.database import get_db
from ...controllers.room.room_controllers import get_room, create_room, delete_room, update_room
from ...models.room.room import RoomCreate, Room

router = APIRouter(tags=["Rooms"])

@router.get("/me")
def get_rooms(db: Session = Depends(get_db)):
    return get_room(db)

@router.post("/create-room", dependencies=[Depends(admin_required)])
def create_room_post(room: RoomCreate, db: Session = Depends(get_db)):
    return create_room(db, room)

@router.put("/{room_id}", dependencies=[Depends(admin_required)])
def update_room_post(room_id: int, room_data: Room, db: Session = Depends(get_db)):
    return update_room(db, room_id, room_data)

@router.delete("/{room_id}", dependencies=[Depends(admin_required)])
def delete_rooms(room_id:int, db: Session = Depends(get_db)):
    return delete_room(db, room_id)