#!/usr/bin/python3
""" The Database storage engine"""
from models.base_model import Base, BaseModel
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship


class DBStorage:
    """ The database storage engine
    Attributes:
	__engine (sqlalchemy Engine): Sqlalchemy Engine used.
	__session(sqlalchemy Session): the sqlalchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """ initialize a new storage instance."""
        self.__engine = create_engine(
		"mysql+mysqldb://{}:{}@{}/{}".format(
		    getenv("HBNB_MYSQL_USER"),
		    getenv("HBNB_MYSQL_PWD"),
		    getenv("HBNB_MYSQL_HOST"),
		    getenv("HBNB_MYSQL_DB")
		    ),
		pool_pre_ping=True
		) 
    if getenv("HBNB_ENV") == "test":
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ method to query on current db session """
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj = self.__session.query(cls)
        result = {"{}.{}".format(type(v).__name__, v.id): v for v in obj}
        return result

    def new(self, obj):
        """ Method Add obj to the current db session"""
        self.__session.add(obj)

    def save(self):
        """ method that commit all changes to the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method that delete an object from the current db sessin"""
        if obj is not None:
             self.__session.delete(obj)

    def reload(self):
        """method that created all tables in the db and create a new session."""
        Base.metadata.create_all(self.__engine)
        s_f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_f)
        self.__session = Session()
    def close(self):
        """Method that Close the working session"""
        self.__session.close()

