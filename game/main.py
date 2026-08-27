from fastapi import FastAPI
from . import database

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}