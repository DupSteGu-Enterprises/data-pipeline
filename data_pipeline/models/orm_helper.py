# A collection of helper functions for use when interacting with the database
# through SQLAlchemy

from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from settings import db_settings
from sqlalchemy import create_engine


def create_connection():
    """ Creates and returns a connection to the database """
    return create_engine(URL(**db_settings.DATABASE))

def create_session(engine):
    """ Creates and returns a session with the database. """
    return sessionmaker(bind=engine)()
