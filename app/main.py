from fastapi import FastAPI, Depends
# from app.auth.controller import router as auth_router

app = FastAPI()
                   
@app.get("/")
def health_check():
    return {"status": "ok"}

