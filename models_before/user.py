#!/usr/bin/python3
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
import models


class User(BaseModel, Base):
    """Base class for both Student and Staff"""
    __tablename__ = 'users'

    id = Column(String(60), nullable=False, primary_key=True)
    #school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    #first_name = Column(String(45), nullable=False)                             
    #last_name = Column(String(45), nullable=False)
    #password = Column(String(45), nullable=False)

    # Define the relationship with Post
    posts = relationship("Post", back_populates="user")

    #def __init__(self, *args, **kwargs):
    #"""Class instantiation"""
        #super().__init__(*args, **kwargs)
        #self.generate_id()

    """
    def generate_id(self):"""
    """Generate id"""
    """ if not self.school_id:
            raise ValueError("school_id is required")

        try:
            models.storage._DBStorage__session.query(School).filter(School.id == self.school_id).one()
        except NoResultFound:
            raise ValueError(f"School with id {self.school_id} does not exist")

        school_initial = self.school_id[:3]
        last_id = models.storage.get_lastId(type(self).__name__)
        if last_id:
            id_int = int(last_id.split('-')[-1]) + 1
        else:
            id_int = 1
        self.id = f"{school_initial}-{type(self).__name__[:3]}-{id_int:04d}"""

