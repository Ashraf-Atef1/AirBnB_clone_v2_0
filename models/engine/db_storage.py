from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage():
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        query = self.__session.query
        classes = self.all_classes()
        results = {}
        for key in classes:
            if classes[key] is cls or cls is None:
                for obj in query(classes[key]).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    results[key] = obj
        return results
    def new(self, obj):
        self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()
    def close(self):
        self.__session.remove()
    @staticmethod
    def all_classes():
        """Get all models to help in convert string to class"""
        return { "State": State, "User": User, "City": City, "Place": Place }

    def create_object(self, class_name):
        """Create an instance from a class name"""
        return self.all_classes()[class_name]
