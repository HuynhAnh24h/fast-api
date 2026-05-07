from pydantic import BaseModel

class ProfileCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    address: str
    
class ProfileUpdate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    address: str

class ProfileResponse(BaseModel):
    first_name: str
    last_name: str
    phone: str
    address: str
    class Config:
        from_attribute = True
