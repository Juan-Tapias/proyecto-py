from fastapi import HTTPException
from sqlmodel import Session
from ..models.room import Room

def create_room(db: Session, room: Room):

    if not all([room.usuario_id, room.room_id, room.fecha,
            room.hora_inicio, room.hora_fin, room.estado]):
        raise HTTPException(
            status_code=400,
            detail="Todos los campos son obligatorios y no pueden ser nulos."
        )
    
    new_room = Room(
        nombre= room.nombre,
        sede= room.sede,
        capacidad= room.capacidad,
        recursos= room.recursos
    )
    db.add(new_room)
    db.commit()
    db.refresh(new_room)

    return {"msg": "Habitacion registrada con éxito", "room_id": new_room.id}
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

