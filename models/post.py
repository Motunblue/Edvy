#!/usr/bin/python3
"""
    Contain the Post Class
"""
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class Post(Base, BaseModel):
    """The post class"""
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(125), nullable=False)
    content = Column(String(2048), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    student_id = Column(String(60), ForeignKey('students.id'))
    staff_id = Column(String(60), ForeignKey('staffs.id'))
