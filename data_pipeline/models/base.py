"""
Superclass for all of our models
"""

from sqlalchemy.ext.declarative import declarative_base
from .orm_helper import create_dbconnection, create_session

# Session used for querying. Don't use for altering the database, we want to
# handle that using exposed session transactions
Session = create_session(create_dbconnection())


class ModelBase(object):
    """
    A custom base for our models.

    TODO: Fill this in with utilities common among models
    """
    @classmethod
    def get(class_, id):
        """
        Queries the database and returns a class object with a matching id.
        """
        return Session.query(class_).get(id)
