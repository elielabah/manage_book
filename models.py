from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__="books"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(20))
    description:Mapped[str|None]=mapped_column(Text, default=None)
    nbrePages:Mapped[int]
