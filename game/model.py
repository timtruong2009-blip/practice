
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# the base of sqlalchemy
class Base(DeclarativeBase):
    pass

# what a new player would look like if we create one
class Player(Base):
    __tablename__ = "all_account"
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(unique= True)
    password: Mapped[str] = mapped_column()