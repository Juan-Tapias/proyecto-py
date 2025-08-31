from fastapi import FastAPI
from app.routes import reservation, rooms, sesion, users
from .models.database import createDbAndTables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    createDbAndTables()

# Montar cada router con su prefijo y tag
app.include_router(reservation.router, prefix="/reservation")
app.include_router(users.router, prefix="/users")
app.include_router(rooms.router, prefix="/rooms")
app.include_router(sesion.router, tags=["Registro"])
app.include_router(sesion.router, tags=["Login"])




@app.get("/")
def health_check():
    return {"status": "ok"}

