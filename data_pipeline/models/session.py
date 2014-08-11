"""
Utility for creating a universial connection and session with the
database.
"""
from orm_helper import create_session, create_dbconnection

# This is the global session we'll use to interact with the database
# Using one session ensures that there are no errors when trying to
# ineract with the database from different places and in different
# ways
Session = create_session(create_dbconnection())
