"""
Tests for the data saving features of the query interface.
"""

import unittest
from query_interface.data_store import store_politician
from models.politician import Politician
from models.funder import Funder
from models.contribution import Contribution


class PoliticianDataStorageTests(unittest.TestCase):
    """ Tests saving politician data into the database """
    def setUp(self):
        pass

    def tearDown(self):
        """ TODO: Clear out things added to database """

    def test_storing_politician_no_contributions(self):
        """ Test storing a single politician into the db """
        data = {"name": "Bill Nelson"}
        #to_store = Politician(**data)
        successful = store_politician(data)
        self.assertTrue(successful)

        # Should now be able to find the politician in the db
        result = Politician.get_by_name("Bill Nelson")
        self.assertIsNotNone(result)
        # Only one should exist, politician object should be returned
        self.assertTrue(isinstance(result, Politician))

    def test_storing_politician_one_contribution(self):
        """ Test storing a single politician with accompanying contribution """
        contributions = [{'date': '08/13/2014', 'funder': 'NRA',}]
        data = {'name': 'Marco Rubio', 'contributions': contributions}
        successful = store_politician(data)
        self.assertTrue(successful)

        # Marco Rubio should now be a politician in our db
        result = Politician.get_by_name('Marco Rubio')
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, Politician))

        # Result should have one contribution and one funder
        self.assertEqual(len(result.contributions), 1)
        self.assertEqual(len(result.funders), 1)

        contribution = result.contributions[0]
        funder = result.funders[0]
        # TODO: These checks are silly. Add .to_dict functions to the models
        # and then use them to compare the results with what we stuck in (:
        self.assertTrue(isinstance(contribution, Contribution))
        self.assertTrue(isinstance(funder, Funder))
