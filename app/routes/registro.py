from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from ..auth.registre import hash_password
from ..models.users import UserCreate, User
from ..models.database import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existe = select(User).WHERE(User.email == user.email)

    result = db.exec(existe).first()
    if result:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    password_hash = hash_password(UserCreate.password)

    new_user = User(
        nombre = user.nombre,
        email = user.email,
        contraseña_hash= password_hash,
        rol= user.rol
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "Usuario registrado con éxito", "user_id": new_user.id}