#!/usr/bin/python3
"""
    Contain the Student Class
"""
from models.school import School
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
import sqlalchemy
import models


class Student(BaseModel, Base):
    """The Derived student class"""
    __tablename__ = 'students'

    id = Column(String(60), nullable=False, primary_key=True)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    #class_id = Column(String(60), ForeignKey('class.id'), nullable=False)

    school = relationship("School", back_populates='students')

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
        self.id = f"{school_initial}-STD-{id_int:04d}"
