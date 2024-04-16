#!/usr/bin/python3
"""The module contains the class User that inherits from BaseModel"""
from models.base_model import BaseModel, Base, storage_t
from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship
class User(BaseModel, Base):
    """The class User that inherits from BaseModel"""
    if storage_t == "db":
        __tablename__ = "users"
        email = Column(VARCHAR(128), nullable=False)
        password = Column(VARCHAR(128), nullable=False)
        first_name = Column(VARCHAR(128), nullable=False)
        last_name = Column(VARCHAR(128), nullable=False)
        places = relationship("Place", backref="users")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
