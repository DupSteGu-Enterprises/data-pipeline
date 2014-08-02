"""
Tests for the data saving features of the query interface.
"""

import unittest
from query_interface.data_store import store_politician


class PoliticianDataStorageTests(unittest.TestCase):
    """ Tests saving politician data into the database """
    def setUp(self):
        pass

    def test_storing_politician(self):
        """ Tests storing a single politician into the db """
        data = {"name": "Marco Rubio", "funders": None}
        successful = store_politician(data)
        self.assertTrue(successful)
