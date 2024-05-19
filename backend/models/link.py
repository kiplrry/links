from models.basemodel import Base, BaseModel
from sqlalchemy import String, Column, ForeignKey,Integer
from sqlalchemy.orm import relationship


class Link(BaseModel, Base):
    """Link class"""
    __tablename__ = 'links'
    name = Column(String(30), default='none')
    url = Column(String(60), default='none')
    user_id = Column(Integer(), ForeignKey('users.id'))

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url

    def save(self):
        """saving link"""
        if not self.user_id:
            raise
        return super().save()