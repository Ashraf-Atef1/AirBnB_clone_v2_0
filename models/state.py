#!/usr/bin/python3
"""The module contains the class State that inherits from BaseModel"""
from models.base_model import BaseModel, Base, storage_t
from models.city import City
import models
from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """The class State that inherits from BaseModel"""
    if storage_t == "db":
        __tablename__ = "states"
        name = Column(VARCHAR(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """getter for list of city instances related to the state"""
        city_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
