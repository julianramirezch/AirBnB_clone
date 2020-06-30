"""Read doc from model."""
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State
from .user import User

storage = FileStorage()
storage.reload()
