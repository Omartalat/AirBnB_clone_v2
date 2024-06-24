#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from models.engine.file_storage import FileStorage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref="State", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Get a list of all related Cities."""
            cities_list = []
            for city in FileStorage.all(City).values():
                if city.id == self.id:
                    cities_list.append(city)
            return cities_list
