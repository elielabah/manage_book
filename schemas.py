from pydantic import BaseModel, Field

class BookCreateModel(BaseModel):
    name:str
    description:str
    nbrePages:int

class BookModel(BaseModel):
    id:int 
    name:str
    description:str
    nbrePages:int
    
class BookUpdateModel(BaseModel):
    name:str
    description:str
    nbrePages:int

class BookPatchModel(BaseModel):
    name:str | None=Field(examples=["Ninja"],default=None)
    description:str | None=Field(examples=["Descr"],default=None) 
    nbrePages:int | None=Field(examples=[20],default=None)        