#!/usr/bin/python3
"""
Module with class State
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """
    State
    """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="State", cascade="all, delete")
        name = Column(String(128), nullable=False)
    else:
        name = ""

        @property
        def cities(self):
            """
            list of city
            """
            from models import storage
            li = []
            for k, v in storage.all(City).items():
                if v.state_id == self.id:
                    li.append(v)
            return li
