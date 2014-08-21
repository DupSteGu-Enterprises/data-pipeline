"""
Interface for creating models and storing them into the database.
"""

from models.politician import Politician
from models.tag import Tag
from models.funder import Funder
from models.contribution import Contribution
from models.session import Session
from datetime import datetime

DATE_FORMAT = '%m/%d/%Y'

def store_politician(politician_data):
    """
    Given a dict of politician data, stores the given data into the database.

    The passed in dict is assumed to contain the following fields:
    name, the name of the politician
    funders, an array of dicts representing contributions made by a
    politician's funders

    Returns True if the politician has been successfully added to the database.

    TODO: Check if we've already encountered this politician - then how do we 
    respond? Assume we have new contributions/funders to add to its list?
    Also need to add validations
    """
    new_politician = Politician({'name': politician_data['name']})
    if 'contributions' in politician_data:
        for contribution in politician_data['contributions']:
            set_contribution(contribution, new_politician)
    Session.add(new_politician)
    Session.commit()
    return True

def set_contribution(contribution_info, politician):
    """
    Given a dict of contribution information, returns a contribution object
    created from that information.

    Returns True if the contribution object was successfully created and added
    to the database.
    TODO: Add validations/checking and error handling.
    """
    # First create the new contribution object and set its fields
    contribution = Contribution()
    contribution.date = datetime.strptime(contribution_info['date'], DATE_FORMAT)

    funder = Funder.get_by_name(contribution_info['funder'])
    if funder is not None:
        contribution.funder = funder
    else:
        # This funder doesn't exist yet, so we need to create it
        funder = Funder({'name': contribution_info['funder']})
        Session.add(funder)
        Session.commit()
        contribution.funder = funder
    contribution.politician = politician

    # If this funder is a new one for the given politician, add it to his/her
    # funders list
    politician.funders.append(funder)

    Session.add(contribution)
    Session.commit()
    return True
