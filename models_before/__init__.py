#!/usr/bin/python3
"""
    Initialize models
"""
from os import getenv
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
