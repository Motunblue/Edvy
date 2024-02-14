#!/usr/bin/python3
"""
    The Database storage class
"""
from models.basemodel import Base, BaseModel
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import scoped_session, sessionmaker
import models
import sqlalchemy
import models
from models.student import Student
from models.staff import Staff
from models.school import School
from models.post import Post


class DBStorage():
    """Connects to the mysql Database"""
    __engine = None
    __session = None


    def __init__(self):
        """Creates database engine"""
        Edvy_MYSQL_USER = getenv('Edvy_MYSQL_USER')
        Edvy_MYSQL_PWD = getenv('Edvy_MYSQL_PWD')
        Edvy_MYSQL_HOST = getenv('Edvy_MYSQL_HOST')
        Edvy_MYSQL_DB = getenv('Edvy_MYSQL_DB')
        Edvy_ENV = getenv('Edvy_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{Edvy_MYSQL_USER}:'
                                    f'{Edvy_MYSQL_PWD}@{Edvy_MYSQL_HOST}/'
                                    f'{Edvy_MYSQL_DB}'
                                    )

        if Edvy_ENV == 'test':
            Base.metadata.drop_all(self.__engine)
        

    def new(self, obj):
        """Add new object to the database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """Get all data from database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def get_lastId(self, cls):
        """Get the last id of a table"""
        all_classes = {"Student": Student, "School": School, "Staff": Staff}
        last_id = self.__session.query(func.max(all_classes[cls].id)).scalar()
        return last_id


    def count(self, cls=None):
        """Count the number of object in storage"""
        self.reload()
        if cls:
            new_dict = self.all(cls)
        else:
            new_dict = self.all()

        return len(new_dict)

    def get(self, cls, id):
        """Retrieve a single row"""
        if not cls:
            return None

        self.reload()
        k = cls.__name__ + '.' + id
        new_dict = self.all(cls)
        if k in new_dict:
            obj = new_dict[k]
            return obj

        return None


    def delete(self, obj=None):
        """Delete from database"""
        if obj is not None:
            self.__session.delete(obj)


    def all(self, cls, email=None, id=None):
        """Get all class"""
        all_classes = {"Student": Student, "School": School, "Staff": Staff}
        cls = all_classes[cls]
        if email:
            return self.__session.query(cls).filter(cls.email == email).first()
        if id:
            return self.__session.query(cls).filter(cls.email == id).first()
        return self.__session.query(all_classes[cls]).all()
