#!/usr/bin/python3
"""
    Contain the Student Class
"""
from models.base_model import BaseModel, Base
from models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey
import sqlalchemy


class Student(BaseModel, Base):
    """The Derived student class"""
    __tablename__ = 'students'

    id = Column(String(60), nullable=False, primary_key=True)
    school_id = Column(String(60), ForeignKey('school.id'), nullable=False)
    class_id = Column(String(60), ForeignKey('class.id'), nullable=False)

    def __init__():
        """Class instantiation"""
        super().__init__(*args, **kwargs)

