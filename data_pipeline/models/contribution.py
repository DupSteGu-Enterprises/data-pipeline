"""
Model for a contribution table entry.

Each contribution has a funder and a politician, while
politicians and funders may have many contributions.
"""

from models import Base
from settings import db_settings
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from orm_helper import create_session, create_dbconnection

Session = create_session(create_dbconnection())

class Contribution(Base):
    """ Defines the Contribution model """
    __tablename__ = db_settings.CONTRIBUTION_TABLE

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    politician_id = Column(Integer, ForeignKey('politicians.id'))
    funder_id = Column(Integer, ForeignKey('funders.id'))

    politician = relationship("Politician", backref=backref('contributions'))
    funder = relationship("Funder", backref=backref('funders'))

    def __str__(self):
        """ Returns a string representation of a contribution object """
        return "Contribution #{id}: {date} {contributor} to {funded}".format(
            id=self.id, date=self.date, contributor=self.funder.name, funded=self.politician.name)
