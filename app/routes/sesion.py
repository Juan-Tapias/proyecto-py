from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from ..auth.validar_password import hash_password, verify_password
from ..models.users import UserCreate, User
from ..models.database import get_db
from ..auth.jwt_hand import create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existe = select(User).where(User.email == user.email)

    result = db.exec(existe).first()
    if result:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    password_hash = hash_password(user.password)

    new_user = User(
        nombre = user.nombre,
        email = user.email,
        contrasenia_hash= password_hash,
        rol= user.rol
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "Usuario registrado con éxito", "user_id": new_user.id}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.contrasenia_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_access_token(data={"sub": user.email, "rol": user.rol})
    return {"access_token": token, "token_type": "bearer"}