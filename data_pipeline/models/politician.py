"""
Model for a politician table entry
"""

from settings import db_settings
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from models import Base
from session import Session
from funder import Funder


politician_funders_table = Table(db_settings.POLITICIAN_FUNDERS_TABLE, Base.metadata,
    Column('politician_id', Integer, ForeignKey('politicians.id')),
    Column('funder_id', Integer, ForeignKey('funders.id')),
)


class Politician(Base):
    """ Defines the Politician model """
    __tablename__ = db_settings.POLITICIAN_TABLE

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # many to many Politician <-> Funder
    funders = relationship(Funder, secondary=politician_funders_table, 
                            backref='politicians')

    def __init__(self, information_dict=None):
        """
        Init can be called with no arguments, or a dict of
        information to be set right at object creation.
        """
        if information_dict is not None:
            super(Politician, self).__init__(**information_dict)
        else:
            super(Politician, self).__init__()

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
        returned. If more than one politician shares the given name, an array
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

    @classmethod
    def get_total_contributions_for(class_, name):
        """
        Finds the number of contributions made to given politician

        If no politician is found with the matching name, an error is raised
        """
        query = Session.query(class_).filter_by(name=name)
        try:
            politician = query.one()
        except NoResultFound:
            # Pass along the exception to be handled by calling scope
            raise NoResultFound

        return len(politician.contributions)
