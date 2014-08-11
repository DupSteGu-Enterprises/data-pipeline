"""
Model definition for a tag
"""

from models import Base
from settings import db_settings
from sqlalchemy import Column, Integer, String
from session import Session


class Tag(Base):
    """ Defines the Tag ORM object """
    __tablename__ = db_settings.TAG_TABLE

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    def __str__(self):
        """ Returns a string representation of a tag object """
        return "Tag #{id}: {title}".format(id=self.id, title=self.title)
