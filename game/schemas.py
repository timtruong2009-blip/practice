import pydantic


# the base for player, only name for now
class BaseOfThePlayer(pydantic.BaseModel):
    name: str


# give password and name if they want to create a player
class CheckingPlayerCreation(BaseOfThePlayer):
    # min length 5 and max length 40
    password: str = pydantic.Field(min_length=5, max_length=40)


# only shows the player name and id not the password
class Player(BaseOfThePlayer):
    id: int

    # pydantic BaseModel thought want dictionary, but we give it a class in model.py
    # so from_attributes = True makes it do
    #     schemas.Player(
    #     id=getattr(db_player, "id"),
    #     name=getattr(db_player, "name"),) so it can works on a class
    class Config:
        from_attributes = True
