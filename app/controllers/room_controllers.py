from sqlmodel import Session
from models.room import Room

def create_room(db: Session, room: Room):
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def get_room(db: Session):
    return db.query(Room).all()

def get_room_by_id(db: Session, room_id:int):
    return db.query(Room).filter(Room.id == room_id).first()

def update_room(db: Session, room_id:int, room_data: Room):
    room = db.query(Room).filter(Room.id == room_id).first()
    if room:
        for key, value in room_data.dict(exclude_unset=True).items():
            setattr(room, key, value)
        db.commit()
        db.refresh(room)
    return room

def delete_room(db: Session, room_id:int):
    room = db.query(Room).filter(Room.id == room_id).first()
    if room:
        db.delete(room)
        db.commit()
    return room

