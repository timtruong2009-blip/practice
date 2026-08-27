
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = "all_account"
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(unique= True)

