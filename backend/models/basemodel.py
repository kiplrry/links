#!/usr/bin/env python3
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base
import models
from json import JSONEncoder


Base = declarative_base()


class BaseModel:
    """Basemodel"""

    id = Column(Integer(), primary_key=True, autoincrement=True)
    created_at = Column(DateTime(), default=datetime.utcnow())
    updated_at = Column(DateTime(), default=datetime.utcnow())

    def __init__(self, *args, **kwargs) -> None:
        """initialize the instance"""
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id})"

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def save(self) -> int:
        """saves the obj"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        id = models.storage.save(self)
        return id

    def delete(self):
        """deletes the obj instance"""
        models.storage.delete(self)

    def update(self, **kwargs):
        """updates the obj instance"""
        if kwargs:
            kwargs.pop('id', None)
            kwargs.pop('updated_at', None)
            kwargs.pop('created_at', None)

            for arg, val in kwargs.items():
                setattr(self, arg, val)
        self.save()
        return self

    @classmethod
    def get(cls, id: int):
        """gets an instance using its id"""
        obj = models.storage.get(cls=cls, id=id)
        return obj

    @classmethod
    def all(cls):
        """return all instances of a cls"""
        all_obj = models.storage.all(cls)
        return all_obj
