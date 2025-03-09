# Core application logic
from fastapi import FastAPI

from .database import *
from .utils import *

app = FastAPI()

init_db()

@app.get("/")
async def root():
    test_str = generate_random_slug(6)
    return {"message": test_str}

