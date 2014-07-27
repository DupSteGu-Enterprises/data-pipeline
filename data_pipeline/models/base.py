# Superclass for all of our models

from sqlalchemy.ext.declarative import declarative_base


def get_model_base():
    """ Returns a base object to be used in defining other models """
    return declarative_base(cls=ModelBase)


class ModelBase(object):
    """
    A custom base for our models.

    TODO: Fill this in with utilities common among models
    """
