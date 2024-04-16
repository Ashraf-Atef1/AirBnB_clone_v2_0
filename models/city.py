#!/usr/bin/python3
"""The module contains the class City that inherits from BaseModel"""
from models.base_model import BaseModel, Base, storage_t
from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
class City(BaseModel, Base):
    """The class City that inherits from BaseModel"""
    if storage_t == "db":
        __tablename__ = "cities"
        name = Column(VARCHAR(128), nullable=False)
        state_id = Column(VARCHAR(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
