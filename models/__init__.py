#!/usr/bin/python3
"""This file contains the engine"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()