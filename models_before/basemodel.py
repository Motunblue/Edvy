#!/usr/bin/python3
"""
    Creates the Base class
"""
import models
import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BaseModel():
    """The class that other classes will inherit from"""
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)


    def __init__(self, *args, **kwargs):
        """The instantiation method"""
        if kwargs:
            for k, v in kwargs.items():
                if (k != "__class__"):
                 setattr(self, k, v)

        else:
            self.firstname = ""
            self.lastname = ""
            self.password = ""

        self.created_at = datetime.utcnow() 
        self.updated_at = self.created_at


    def __str__(self):
        """String representation of the object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Store the new obj"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()


    def to_dict(self):
        """Returns dictionary representation of the class instance"""
        my_dict = {}
        for k, v in self.__dict__.items():
            if (type(v) == datetime):
                v = v.isoformat()

            my_dict[k] = v

        my_dict["__class__"] = self.__class__.__name__


        return my_dict
