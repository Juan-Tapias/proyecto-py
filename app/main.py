from fastapi import FastAPI, Depends
# from app.auth.controller import router as auth_router
from app.routes.example_route import router as example_router
app = FastAPI()
                   
@app.get("/")
def health_check():
    return {"status": "ok"}

