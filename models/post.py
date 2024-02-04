#!/usr/bin/python3
"""
    Contain the Post Class
"""
from models.base_model import BaseModel, Base
from models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Post(BaseModel):
    """The post class"""
    __tablename__ = "posts"

    id = Column(String(60), nullable=False, primary_key=True)
    title = Column(String(125), nullable=False)
    content = Column(String(2048), nullable=False)
    user_id = Column(String(60), nullable=False)
    school_id = Column(String(60), ForeignKey('school.id'), nullable=False)

    # Define a relationship with Student or Staff
    user = relationship("BaseModel", polymorphic=True)
