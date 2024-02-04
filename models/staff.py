#!/usr/bin/python3
"""
    Contain the Staff Class
"""
from models.base_model import BaseModel, Base
from models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Staff(BaseModel, Base):
    """The staff class"""
    __tablename__ = "staffs"

    id = Column(String(60), nullable=False, primary_key=True)
    email = Column(String(60))
    address = Column(String(60))
    profession = Column(String(60), nullable=False)
    phone_number = Column(String(60), nullable=False)
    school_id = Column(String(60), ForeignKey('school.id'), nullable=False)

    def __init__():
        """Class instantiation"""
        super().__init__(*args, **kwargs)

