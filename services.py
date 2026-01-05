from fastapi import HTTPException, status
from sqlalchemy import Select
from schemas import BookCreateModel
from models import Book
from sqlalchemy.orm import Session

async def create_book(book:BookCreateModel, session:Session):
    book_created=Book(name=book.name, description=book.description, nbrePages=book.nbrePages)
    session.add(book_created)
    session.commit()
    return book_created

async def get_book(id:int, session:Session):
    stmt=Select(Book).where(Book.id==id)
    result=session.execute(statement=stmt)
    #print(result)
    book=result.scalar_one_or_none()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce livre n'a pas été trouvé")
    return book

async def get_booklist(session:Session):
    stm= Select(Book)
    result=session.execute(statement=stm)
    books=result.scalars().all()
    return books