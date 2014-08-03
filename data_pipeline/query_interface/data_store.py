"""
Interface for creating models and storing them into the database.
"""

from models.politician import Politician
from models.tag import Tag
from models.funder import Funder
from models.orm_helper import *


def store_politician(politician_data):
    """
    Given a dict of politician data, stores the given data into the database.

    The passed in dict is assumed to contain the following fields:
    name, the name of the politician
    funders, an array of names of the politician's funders

    Returns True if the politician has been successfully added to the database.
    """
    return True
