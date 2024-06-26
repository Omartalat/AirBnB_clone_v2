#!/usr/bin/python3
"""
Module with class User
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """
    class User that inherits from BaseModel
    """
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    __tablename__ = "users"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="User", cascade="all, delete")
    else:
        places = None
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="User", cascade="all, delete")
    else:
        reviews = None
