#!/usr/bin/python3
"""
    Contain the School Class
"""
import models
from models.basemodel import Base
from models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from web import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_school(school_id):
    return models.storage.all(cls='School', id=school_id)

class School(Base, UserMixin):
    """The school class"""
    __tablename__ = "schools"
    
    id = Column(String(16), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    address = Column(String(128))
    phone_number = Column(String(16))
    #admin_name = Column(String(45), nullable=False)
    logo = Column(String(60), nullable=False, default="default.png")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    students = relationship('Student', backref='school')
    staffs = relationship('Staff', back_populates='school')

    def __init__(self, *args, **kwargs):
        """The instantiation method"""
        if kwargs:
            for k, v in kwargs.items():
                if (k != "__class__"):
                    setattr(self, k, v)

        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.generate_id()


    def save(self):
        """Store the new obj"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def generate_id(self):
        """Generate id"""
        school_name = self.name[:3].upper()
        last_id = models.storage.get_lastId("School")
        if last_id:
            id_int = int(last_id.split('-', 1)[-1]) + 1
        else:
            id_int = 1
        self.id = f"{school_name}-{id_int:04d}"
