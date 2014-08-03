"""
Model for a funder table entry
"""

from models import Base
from settings import db_settings
from sqlalchemy import Column, Integer, String


class Funder(Base):
    """ Defines the Funder model """
    __tablename__ = db_settings.FUNDER_TABLE

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        """ Returns a string representation of a funder object """
        return "Funder #{id}: {name}".format(id=self.id, name=self.name)
