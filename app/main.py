from fastapi import FastAPI
from app.routes import reservation, rooms, users, registro 

app = FastAPI()

# Montar cada router con su prefijo y tag
app.include_router(reservation.router, prefix="/reservation", tags=["Reservation"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(registro.router, prefix="/registro", tags=["Registro"])

@app.get("/")
def health_check():
    return {"status": "ok"}

