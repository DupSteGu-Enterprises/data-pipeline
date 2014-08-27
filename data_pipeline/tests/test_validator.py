"""
Tests the validator class intended to provide a validation mechanism
for our models
"""

import unittest
from models.utils.validator import Validator


class ValidatorTests(unittest.TestCase):
    """ Tests the validator class and its mechanisms """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def nonEmpty(self, someString):
        """ Simple check if a given string is empty """
        return True if someString else False

    def test_validator_no_errors(self):
        """ Test a valid validator with simple attribute and validation """
        validator = Validator();
        validator.myproperty = "valid"
        validator.validations = {'myproperty': self.nonEmpty}
        self.assertTrue(validator.is_valid())
