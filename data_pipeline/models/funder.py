"""
Model for a funder table entry
"""

from models import Base
from settings import db_settings
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from orm_helper import create_session, create_dbconnection


Session = create_session(create_dbconnection())


class Funder(Base):
    """ Defines the Funder model """
    __tablename__ = db_settings.FUNDER_TABLE

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, information_dict=None):
        """
        Constructor for a Funder object

        Can be called with no arguments, creating a Funder 
        object with no attributes set, or with a dict of 
        information to be set at object creation.
        """
        if information_dict is not None:
            super(Funder, self).__init__(**information_dict)
        else:
            super(Funder, self).__init__()

    def __str__(self):
        """ Returns a string representation of a funder object """
        return "Funder #{id}: {name}".format(id=self.id, name=self.name)

    @classmethod
    def get_by_name(class_, name):
        """ 
        Queries the database for one or more funders matching the given name.

        If onlye on funder with a matching name exists, only that funder is 
        returned. If multiple funders with the given name exist, an array of 
        those funders is returned. 
        Returns none if no match is found.
        """
        query = Session.query(class_).filter_by(name=name)
        try:
            return query.one()
        except MultipleResultsFound:
            return query.all()
        except NoResultFound:
            return None











