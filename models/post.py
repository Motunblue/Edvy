#!/usr/bin/python3
"""
    Contain the Post Class
"""
from models.basemodel import Base, BaseModel
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, polymorphic_union
import models
from datetime import datetime


class Post(Base, BaseModel):
    """The post class"""
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(125), nullable=False)
    content = Column(String(2048), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    student_id = Column(String(60), ForeignKey('students.id'))
    staff_id = Column(String(60), ForeignKey('staffs.id'))
