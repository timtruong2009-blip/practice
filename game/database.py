import os
from dotenv import load_dotenv

from sqlalchemy.pool import NullPool
import sqlalchemy
import sqlalchemy.orm

# getting url from online(supa), keep url hidden in .env
load_dotenv()
# Fetch variables
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# create new engine have a link with database (like a phone number to your dentist)

engine = sqlalchemy.create_engine(DATABASE_URL, poolclass=NullPool)
# make a create new session button which activate if called
# kind of like booking an appointment with your dentist
new_session = sqlalchemy.orm.sessionmaker(autocommit = False, autoflush = False, bind = engine)

# got the db from online
def get_db():
    with new_session() as db:
        yield db

