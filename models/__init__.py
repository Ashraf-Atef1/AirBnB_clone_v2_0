#!/usr/bin/python3
"""The __init__ module"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")
if storage_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
