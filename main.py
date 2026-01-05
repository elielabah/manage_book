from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from dbconfig import yield_session
from schemas import BookCreateModel, BookModel, BookPatchModel, BookUpdateModel
from data import books
import services
from sqlalchemy.orm import Session

app=FastAPI(root_path = "/api")

@app.get("/")
async def hello():
    return {"message":"Bonjour tout le monde!"}

@app.get("/calculate")
async def calculate(x:int,y:int): 
    z=x+y**y
    return {"result":z}

@app.post("/books",response_model=BookModel)
async def create_book(book:BookCreateModel,session:Session=Depends(yield_session)):
   return await services.create_book(book=book, session=session)
    
@app.get("/books/{id}",response_model=BookModel)
async def get_book(id:int, session:Session=Depends(yield_session)):
    return await services.get_book(id=id, session=session)

@app.get("/books",response_model=list[BookModel])
async def get_booklist(session:Session=Depends(yield_session)):
    return await services.get_booklist(session=session)

@app.delete("/books/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id:int, session:Session=Depends(yield_session)):
    return await services.delete_book(id=id, session=session)

@app.put("/books/{id}",response_model=BookModel)
async def update_book(id:int, book:BookUpdateModel):
    if id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"le livre avec l'id {id} n'a pas été trouvé ou n'existe pas")
    existing_book=books[id]
    existing_book.name=book.name
    existing_book.description=book.description
    existing_book.nbrePages=book.nbrePages
    return existing_book

@app.patch("/books/{id}",response_model=BookPatchModel)
async def patched_book(id:int, book:BookPatchModel):
    if id not in books:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"le livre avec l'id {id} n'a pas été trouvé ou n'existe pas")
    patched_book=books[id]
    patched_book.name = book.name or patched_book.name
    patched_book.description = book.description or patched_book.description
    patched_book.nbrePages = book.nbrePages or patched_book.nbrePages
    
    return patched_book