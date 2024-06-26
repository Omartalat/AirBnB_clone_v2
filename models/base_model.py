#!/usr/bin/python3
"""
Module with class BaseModel
"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Instantiation
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "updated_at" or k == "created_at":
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
            if not hasattr(kwargs, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, (self.id),
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        if '_sa_instance_state' in my_dict:
            del my_dict["_sa_instance_state"]
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

    def delete(self):
        """
        Delet
        """
        models.storage.delete(self)
