from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.link import Link


class User(BaseModel, Base):
    """class user"""
    __tablename__ = 'users'
    name = Column(String(30), default='anonymous')
    username = Column(String(23), default='none')
    age = Column(Integer(), default=0)
    links = relationship('Link', backref='user')

    def __init__(self, name='none', username='none', age=0):
        self.name = name
        self.username = username
        self.age = age

    def create_link(self, name, url) -> Link:
        """creates a link"""
        link = Link(name, url)
        link.user_id = self.id
        link.save()
        return link

    def save_link(self, link: Link) -> Link:
        """saves a link"""
        link.user_id = self.id
        link.save()
        return link
