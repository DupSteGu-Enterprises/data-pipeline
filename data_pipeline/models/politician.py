"""
Model for a politician table entry
"""

from settings import db_settings
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from .orm_helper import create_session, create_dbconnection
from .base import get_model_base


Base = get_model_base()  # Grab the declarative model base to inherit from
Session = create_session(create_dbconnection()) # Used only for querying


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

    @classmethod
    def get_by_name(class_, name):
        """
        Queries the database for politicians with a matching name as given.

        If only one politician has the given name, only that politician is
        returns. If more than one politician shares the given name, an array
        of those politicians is returned.
        Returns none if no match found.
        """
        query = Session.query(class_).filter_by(name=name)
        try:
            return query.one()
        except MultipleResultsFound:
            return query.all()
        except NoResultFound:
            return None
