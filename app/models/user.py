from sqlalchemy import Column, String,Integer, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    role = Column(String, default="User")

    is_active = Column(Boolean, default=True)

    # profile = relationship("Profile", back_populates="user", uselist=False)