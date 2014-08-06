"""
Interface for creating models and storing them into the database.
"""

from models.politician import Politician
from models.tag import Tag
from models.funder import Funder
from models.orm_helper import create_session, create_dbconnection

# TODO: Figure out if db_session should be made global here, or a new one made
# for each transaction.
db_session = create_session(create_dbconnection())

def store_politician(politician_data):
    """
    Given a dict of politician data, stores the given data into the database.

    The passed in dict is assumed to contain the following fields:
    name, the name of the politician
    funders, an array of names of the politician's funders

    Returns True if the politician has been successfully added to the database.
    """
    # Replace the list of funder contribution dicts with funder objects
    if 'funders' in politician_data:
        politician_data['funders'] = map(extract_funders, politician_data['funders'])

    to_save = Politician(politician_data) 
    
    db_session.add(to_save)
    db_session.commit()
    return True

def extract_funders(funder_information):
    """
    Given a dict of funder information, returns a funder object for that info.
    NOTE: I think these should be dicts of the funder information, not tuples... 
    I'm going to continue assuming that its a dict instead

    First checks the database for an already existing entry and returns it if 
    one exists. Otherwise, creates a new db entry for the funder and stores it
    in the database.
    """ 
    existing_funder = Funder.get_by_name(funder_information["name"])
    if existing_funder is not None:
        return existing_funder
    else:
        new_funder = Funder(funder_information)
        db_session.add(new_funder)
        db_session.commit()
        return new_funder
