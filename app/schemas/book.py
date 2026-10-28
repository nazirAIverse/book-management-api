from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    title: str
    author: str
    year: int | None = None


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: str
    year: int | None

class BookUpdate(BaseModel):
    title : str
    author : str
    year : int | None = None
