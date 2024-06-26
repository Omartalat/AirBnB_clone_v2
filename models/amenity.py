#!/usr/bin/python3
"""
Module with class Amenity
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity
    """
    name = Column(String(128), nullable=False)
    __tablename__ = "amenities"
