#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """this is the base class"""

    def __init__(self, *args, **kwargs):
        """the definition"""
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":

                    if key == ("created_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    elif key == ("updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """the string version"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """saves the instance"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """handles the key and value"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
