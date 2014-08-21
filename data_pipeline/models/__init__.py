"""
Initialize the model base to be shared among all models.
"""

from .base import ModelBase
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(cls=ModelBase)
