#!/usr/bin/python3
"""
    Creates the Base class
"""
import models
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from web import login_manager

Base = declarative_base()

@login_manager.user_loader
def load_user(user_id):
    if user_id[:3] == "STD":
        return models.storage.all(cls='Student', id=user_id)
    elif user_id[:3] == "STF":
        return models.storage.all(cls='Staff', id=user_id)
    return models.storage.all(cls='School', id=user_id)


class BaseModel():
    """The class that other classes will inherit from"""
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """The instantiation method"""
        if kwargs:
            for k, v in kwargs.items():
                if (k != "__class__"):
                 setattr(self, k, v)
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
    
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        if "password" in my_dict:
            del my_dict["password"]
        if "picture" in my_dict:
            del my_dict["picture"]
        return my_dict
