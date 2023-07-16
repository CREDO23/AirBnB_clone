#!/usr/bin/python3


"""In this module , i initialize the storage engine"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
