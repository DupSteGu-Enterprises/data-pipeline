"""
Model for a politician table entry
"""

from base import get_model_base
from settings import db_settings
from sqlalchemy import Column, Integer, String


Base = get_model_base()  # Grab the declarative model base to inherit from


class Politician(Base):
    """ Defines the Politician model """
    __tablename__ = db_settings.POLITICIAN_TABLE

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        """
        Returns a string representation of a politician object
        """
        return "Politician #{id}: {name}".format(id=self.id, name=self.name)
