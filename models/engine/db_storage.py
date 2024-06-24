#!/usr/bin/python3
"""New engine"""
import os
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.base_model import Base
from models.city import City
from models.place import Place
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """New engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        mysql_user = os.environ.get("HBNB_MYSQL_USER")
        mysql_passwd = os.environ.get("HBNB_MYSQL_PWD")
        mysql_host = os.environ.get("HBNB_MYSQL_HOST")
        mysql_db = os.environ.get("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            mysql_user, mysql_passwd, mysql_host, mysql_db),
              pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """Query all objects depending on the class name (argument cls)"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        obj_dict = {}
        try:
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
                objs = self.__session.query(cls).all()
            else:
                objs = []
                for class_ in class_dict.values():
                    objs.extend(self.__session.query(class_).all())

            for obj in objs:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        except Exception as e:
            print(f"An error occurred: {e}")
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
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory=session_factory)
        self.__session = Session()
        return self.__session
