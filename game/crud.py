
import sqlalchemy.orm
import model
import schemas

#get ALL the player data, make db a session so we can comminicate with database
def get_players_db(db: sqlalchemy.orm.Session):
    return db.query(model.Player).all()

# get ONE specific player data using id num (the first one with same id)
def get_one_player_db(db: sqlalchemy.orm.Session, player_id: int):
     return db.query(model.Player).filter(model.Player.id == player_id).first()


# creating a new player,  name and password required
# get themplate for what we need from schemas, get player template from model
def create_player(db: sqlalchemy.orm.Session, player: schemas.CheckingPlayerCreation):
     new_player = model.Player(name=player.name)
     db.add(new_player)
     db.commit()
     db.refresh(new_player)
     return new_player
