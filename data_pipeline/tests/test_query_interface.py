"""
Tests for the data saving features of the query interface.
"""

import unittest
from query_interface.data_store import store_politician
from models.politician import Politician


class PoliticianDataStorageTests(unittest.TestCase):
    """ Tests saving politician data into the database """
    def setUp(self):
        pass

    def test_storing_politician(self):
        """ Tests storing a single politician into the db """
        data = {"name": "Bill Nelson"}
        #to_store = Politician(**data)
        successful = store_politician(data)
        self.assertTrue(successful)

        # Should now be able to find the politician in the db
        result = Politician.get_by_name("Bill Nelson")
        self.assertIsNotNone(result)
        # Only one should exist, politician object should be returned
        self.assertTrue(isinstance(result, Politician))
