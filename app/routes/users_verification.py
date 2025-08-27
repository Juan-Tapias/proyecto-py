from fastapi import Depends, HTTPException

def get_current_user():
    return {"id": 1, "nombre": "Juan", "email": "juan@test.com", "rol": "user"}
