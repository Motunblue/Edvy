#!/usr/bin/python3
"""
    Contain the Staff Class
"""
from models.basemodel import BaseModel, Base
from models.school import School
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
import models
from flask_login import UserMixin


class Staff(BaseModel, Base, UserMixin):
    """The staff class"""
    __tablename__ = "staffs"

    id = Column(String(60), nullable=False, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(60))
    address = Column(String(60))
    dob = Column(DateTime, nullable=False)
    profession = Column(String(60))
    phone_number = Column(String(60), nullable=False)
    picture = Column(String(45), nullable=False, default="default.png")
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)

    posts = relationship('Post', backref="staff", cascade="all, delete-orphan")

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
            raise ValueError(f"School with ID {self.school_id} does not exist")

        school_initial = self.school_id[:3]
        last_id = models.storage.get_lastId("Staff")
        if last_id:
            id_int = int(last_id.split('-')[-1]) + 1
        else:
            id_int = 1
        self.id = f"STF-{school_initial}-{id_int:04d}"
