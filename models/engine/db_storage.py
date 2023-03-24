#!/usr/bin/python3
"""Model to manage DB storage using SQLAlchemy"""
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """Class manage that storage for AirBnB clone using SQLAlchemy"""
    __engine = None
    __session = None
    classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        """Init __engine based on the Enviroment"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        db = "mysql+mysqldb://{}:{}".format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD)
        db += "@{}/{}".format(HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
        self.__engine = create_engine(db, pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects
        depending of the class name
        """
        d = {}
        if cls is None:
            for c in self.classes:
                c = eval(c)
                for instance in self.__session.query(c).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    d[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                d[key] = instance
        return d
    
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete object from the current database sessioon"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create table in database"""
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session
    
    def close(self):
        """closing the session"""
        self.reload()
        self.__session.close()
