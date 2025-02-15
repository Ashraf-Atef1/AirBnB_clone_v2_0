#!/usr/bin/python3
"""The module contains the class Place that inherits from BaseModel"""
from models.base_model import BaseModel, Base, storage_t
from sqlalchemy import Column, VARCHAR, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """The class Place that inherits from BaseModel"""
    if storage_t == "db":
        __tablename__ = "places"
        city_id = Column(VARCHAR(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(VARCHAR(60), ForeignKey("users.id"), nullable=False)
        name = Column(VARCHAR(128), nullable=False)
        description = Column(VARCHAR(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
    amenity_ids = []
