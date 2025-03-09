from fastapi import FastAPI

from app.database import init_db


app = FastAPI()

init_db()

@app.get("/")
async def root():
    return {"message": "hai"}
