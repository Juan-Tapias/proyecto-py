from sqlmodel import Session
from ..models.users import User

def create_users(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id:int):
    return db.query(User).filter(User.id == user_id).first()

def delete_user_by_id(db: Session, user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

