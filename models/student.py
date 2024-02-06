#!/usr/bin/python3
"""
    Contain the Student Class
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
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
        print(self.school)
        school_name = self.school.name[:3].upper()
        student_count = models.storage.count("Student") + 1
        self.id = f"{school_name}-STD-{student_count:04d}"
