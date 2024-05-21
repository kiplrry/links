from models.basemodel import Base, BaseModel
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, validates


class Link(BaseModel, Base):
    """Link class"""

    __tablename__ = 'links'
    name = Column(String(30), nullable=False)
    url = Column(String(60), nullable=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    descr = Column(String(30), nullable=True)

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url

    def save(self) -> int:
        if not [self.user_id, self.name]:
            raise ValueError('No user_id')
        return super().save()
