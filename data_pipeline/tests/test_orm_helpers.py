"""
Tests for the ORM helper functions.
"""

import unittest
from orm_helper import create_dbconnection, create_session
from settings import db_settings
from sqlalchemy.engine.base import Engine as sqlalchemy_engine


class DatabaseSessionManagementTests(unittest.TestCase):
    """Tests functions for managing a connection and session with the db"""

    def test_connection_creation(self):
        """Test the creation of a connection with the database"""
        connection = create_dbconnection()

        # A sqlalchemy_engine should be returned, connected to our database
        self.assertTrue(isinstance(connection, sqlalchemy_engine))
        self.assertEqual(connection.name, db_settings.DATABASE['drivername'])

        # All our tables should exist in the database we've connected to
        for table in db_settings.TABLE_LIST:
            self.assertTrue(connection.has_table(table))
