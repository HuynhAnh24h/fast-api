from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)

    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    address = Column(String)
    avatar = Column(String, default="https://i.pinimg.com/236x/02/72/35/02723528ae01d17bbf67ccf6b8da8a6b.jpg")

    # Tạo quan hệ với user
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", back_populates="profile")