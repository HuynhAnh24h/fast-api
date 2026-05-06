from pydantic import BaseModel
from app.schemas.post import PostResponse

class CategoryCreate(BaseModel):
    name: str
    
class CategoryUpdate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    slug: str
    post:list[PostResponse] = []
    
    class Config:
        from_attributes = True
