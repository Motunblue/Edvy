#!/usr/bin/python3
"""
    Contain the Post Class
"""
from models.basemodel import BaseModel, Base
from models.basemodel import BaseModel
from models.school import School
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, polymorphic_union
from sqlalchemy.orm.exc import NoResultFound
import models


class Post(Base):
    """The post class"""
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(125), nullable=False)
    content = Column(String(2048), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)

    # Define a relationship with Student or Staff
    user = relationship("User", back_populates="posts")

    def __init__(self, *args, **kwargs):
        """class Instantiation""" 
        super().__init__(*args, **kwargs)
        if not self.school_id:
            raise ValueError("school_id is required")

        try:
            models.storage._DBStorage__session.query(School).filter(School.id == self.school_id).one()
        except NoResultFound:
            raise ValueError(f"School with id {self.school_id} does not exist")

        """
         if self.user_type == 'student':
             self.student_id = self.user_id
         elif self.user_type == 'staff':
            self.staff_id = self.user_id"""

    def save(self):
        """Store the new obj"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
