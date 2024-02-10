#!/usr/bin/python3
"""
    Contain the Staff Class
"""
from models.basemodel import BaseModel, Base
from models.school import School
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
import models


class Staff(BaseModel, Base):
    """The staff class"""
    __tablename__ = "staffs"

    id = Column(String(60), nullable=False, primary_key=True)
    email = Column(String(60))
    address = Column(String(60))
    profession = Column(String(60), nullable=False)
    phone_number = Column(String(60), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)

    school = relationship("School", back_populates="staffs")
    posts = relationship("Post", foreign_keys="[Post.staff_id]")

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
            raise ValueError(f"School with id {self.school_id} does not exist")

        school_initial = self.school_id[:3]
        last_id = models.storage.get_lastId("Staff")
        if last_id:
            id_int = int(last_id.split('-')[-1]) + 1
        else:
            id_int = 1
        self.id = f"{school_initial}-STF-{id_int:04d}"
