#!/usr/bin/python3
"""
__init__ file
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
