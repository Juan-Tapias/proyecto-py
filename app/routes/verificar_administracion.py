from fastapi import APIRouter, HTTPException, Depends


def get_admin_user():
    return {"nombre": "Juan", "rol": "admin"}


def admin_required(usuario: dict = Depends(get_admin_user)):
    if usuario["rol"] != "admin":
        raise HTTPException(status_code=403, detail="Se requiere permisos de administrador")
    return usuario

