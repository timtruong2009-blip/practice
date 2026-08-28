
from fastapi import FastAPI, Depends
import sqlalchemy.orm
import model
import schemas
import crud
import database

# get Base, get blueprint of Base(metadata), if it doesn't exist, create it(create_all)
# database.engine is the phone number of the database, tell it to create in that
model.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# test
@app.get("/")
def read_root():
    return {"message": "main page"}

# return all player,
@app.get("/players/", response_model=list[schemas.Player])
def give_all_players(db: sqlalchemy.orm.Session):
    return crud.get_players_db(db)

# return one player using id
@app.get("/players/{player_id}", response_model=schemas.Player)
def give_one_players(player_id: int, db: sqlalchemy.orm.Session):
    db_player = crud.get_one_player_db(db, player_id)
    return db_player

















# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from . import models, schemas, crud
# from .database import engine, get_db
#
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"message": "hello"}
#
# @app.get("/players/", response_model=list[schemas.Player])
# def read_players(db: Session = Depends(get_db)):
#     return crud.get_players(db)
#
# @app.get("/players/{player_id}", response_model=schemas.Player)
# def read_player(player_id: int, db: Session = Depends(get_db)):
#     db_player = crud.get_player(db, player_id)
#     if db_player is None:
#         raise HTTPException(status_code=404, detail="Player not found")
#     return db_player
#
# @app.post("/players/", response_model=schemas.Player)
# def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
#     return crud.create_player(db, player)