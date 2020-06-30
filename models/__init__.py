#!/usr/bin/python3
"""Read doc from model."""
from .engine.file_storage import FileStorage
from .base_model import BaseModel


storage = FileStorage()
storage.reload()
