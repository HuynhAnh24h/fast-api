from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    category_id: int

class PostUpdate(BaseModel):
    title: str
    content: str
    category_id: int

class PostResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attribute = True