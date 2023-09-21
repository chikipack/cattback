from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name_s = Column(String, nullable=False)
    dad_lastname = Column(String, nullable=False)
    mom_lastname = Column(String)
    school_email = Column(String, unique=True, nullable=False)
    personal_email = Column(String, unique=True)
    matricula = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)