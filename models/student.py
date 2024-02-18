#!/usr/bin/python3
"""
    Contain the Student Class
"""
from models.school import School
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
import models


class Student(BaseModel, Base):
    """The Derived student class"""
    __tablename__ = 'students'

    id = Column(String(60), nullable=False, primary_key=True)
    school_id = Column(String(16), ForeignKey('schools.id'), nullable=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)

    posts = relationship('Post', backref="student", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Class instantiation"""
        super().__init__(*args, **kwargs)
        self.generate_id()


    def generate_id(self):
        """Generate id"""
        if not self.school_id:
            raise ValueError("school_id is required")

        try:
            models.storage._DBStorage__session.query(School).filter(School.id == self.school_id).one()
        except NoResultFound:
            raise ValueError(f"School with id {self.school_id} does not exist")

        school_initial = self.school_id[:3]
        last_id = models.storage.get_lastId("Student")
        if last_id:
            id_int = int(last_id.split('-')[-1]) + 1
        else:
            id_int = 1
        self.id = f"STD-{school_initial}-{id_int:04d}"
