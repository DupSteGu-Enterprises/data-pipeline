"""
Tests for the ORM helper functions.
"""

import unittest
from orm_helper import create_dbconnection, create_session
from settings import db_settings
from sqlalchemy.engine.base import Engine as sqlalchemy_engine
from sqlalchemy.orm.session import Session as sqlalchemy_session


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

    def test_session_creation(self):
        """Test the creation of a session for transactions with the db"""
        connection = create_dbconnection()
        self.assertTrue(isinstance(connection, sqlalchemy_engine))

        session = create_session(connection)
        self.assertTrue(isinstance(session, sqlalchemy_session))
        # The session should be bound to our db connection
        self.assertEqual(session.get_bind(), connection)
        session.close()
