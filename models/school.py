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


class School(Base):
    """The school class"""
    __tablename__ = "schools"
    
    id = Column(String(128), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(60))
    address = Column(String(60))
    phone_number = Column(String(60), nullable=False)
    admin_name = Column(String(45), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    students = relationship('Student', back_populates='school')

    def __init__(self, *args, **kwargs):
        """The instantiation method"""
        if kwargs:
            for k, v in kwargs.items():
                if (k != "__class__"):
                    setattr(self, k, v)

        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at


    def save(self):
        """Store the new obj"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
