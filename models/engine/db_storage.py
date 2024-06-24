#!/usr/bin/python3
"""New engine"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """New engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize a new DBStorage instance."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        hbnb_env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending of the class name (argument cls)"""
        obj_dict = {}

        class_dict = {
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity
        }

        if cls:
            if isinstance(cls, str):
                cls = class_dict.get(cls)
                if not cls:
                    raise ValueError(f"Class '{cls}' is not defined.")
            if not isinstance(cls, type):
                raise TypeError(f"Expected a class type, got {type(cls)} instead.")
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        1. create all tables in the database
        2. create the current database session (self.__session)
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
