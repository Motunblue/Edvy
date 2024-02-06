#!/usr/bin/python3
"""
    Contain the School Class
"""
from models.base_model import Base
from models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey


class School(Base):
    """The school class"""
    __tablename__ = "schools"
    
    id = Column(String(60), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(60))
    address = Column(String(60))
    phone_number = Column(String(60), nullable=False)
    admin_name = Column(String(45), nullable=False)
