from fastapi import APIRouter, Depends
from .verificar_administracion import admin_required
from sqlmodel  import Session
from ..models.database import get_db
from ..controllers.users_controllers import get_user, delete_user_by_id
from .users_verification import get_current_user

router = APIRouter(tags=["Users"])

@router.get("/me")
def get_my_users(user: dict = Depends(get_current_user)):
    return user

@router.get("/", dependencies=[Depends(admin_required)])
def read_users(db: Session = Depends(get_db)):
    return get_user(db)

@router.delete("/{user_id}", dependencies=[Depends(admin_required)])
def remove_user(user_id: int, db: Session = Depends(get_db), usuario: dict = Depends(admin_required)):
    return delete_user_by_id(db, user_id)
