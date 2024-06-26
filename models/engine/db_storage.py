#!/usr/bin/python3
"""
DBStorage
"""
import os
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        init
        """
        usr = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(usr,
                                      password, host, database),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        All
        """
        obj = {}
        if cls is None:
            for class_name in (User, State, City, Amenity, Place, Review):
                query = self.__session.query(class_name).all()
                for i in query:
                    k = "{}.{}".format(i.__class__.__name__, i.id)
                    obj[k] = i
        else:
            query = self.__session.query(cls).all()
            for i in query:
                k = "{}.{}".format(i.__class__.__name__, i.id)
                obj[k] = i
        return obj

    def new(self, obj):
        """
        New
        """
        self.__session.add(obj)

    def save(self):
        """
        Save
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reload
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """
        close
        """
        self.__session.remove()
