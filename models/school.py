#!/usr/bin/python3
"""
    Contain the School Class
"""
import models
from models.basemodel import Base
from models.basemodel import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class School(Base, BaseModel, UserMixin):
    """The school class"""
    __tablename__ = "schools"
    
    id = Column(String(16), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(60), unique=True)
    password = Column(String(60), nullable=False)
    address = Column(String(128))
    phone_number = Column(String(16))
    picture = Column(String(60), nullable=False, default="default.png")
    students = relationship('Student', backref='school', cascade="all, delete-orphan")
    staffs = relationship('Staff', backref='school', cascade="all, delete-orphan")
    posts = relationship('Post', backref="school", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """The instantiation method"""
        super().__init__(*args, **kwargs)
        self.generate_id()


    def generate_id(self):
        """Generate id"""
        school_name = self.name[:3].upper()
        last_id = models.storage.get_lastId("School")
        if last_id:
            id_int = int(last_id.split('-', 1)[-1]) + 1
        else:
            id_int = 1
        self.id = f"{school_name}-{id_int:04d}"
