from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from schemas import BookCreateModel, BookModel, BookPatchModel, BookUpdateModel
from data import books

app=FastAPI(root_path = "/api")

@app.get("/")
async def hello():
    return {"message":"Bonjour tout le monde!"}

@app.get("/calculate")
async def calculate(x:int,y:int): 
    z=x+y**y
    return {"result":z}

@app.post("/books",response_model=BookModel)
async def create_book(book:BookCreateModel):
    book_created=BookModel(id=1, name=book.name,description=book.description,nbrePages=book.nbrePages)
    return book_created

@app.get("/books/{id}",response_model=BookModel)
async def get_book(id:int):
    book=books.get(id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce livre n'a pas été trouvé")
    return book

@app.get("/books",response_model=list[BookModel])
async def get_booklist():
    return books.values()

@app.delete("/books/{id}")
async def delete_books(id:int):
    if id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"le livre avec l'id {id} n'a pas été trouvé ou n'existe pas")
    else:
        del books[id]
        if id not in books:
            return JSONResponse(content={"message":"Ce livre a bien été supprimé"},status_code=status.HTTP_204_NO_CONTENT,media_type="application/json")

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