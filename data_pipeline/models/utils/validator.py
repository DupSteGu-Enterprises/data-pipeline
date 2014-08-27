"""
Mixin class to provide validations to our SQLAlchemy
models
"""


class Validator(object):
    """
    Provides mechanisms to validate SQLAlchemy ORM objects

    To include validations, models must inherit from Validator and
    overwrite self.validations, which is a dict of properties to
    functions to be run to validate those properties.

    TODO: Write a set of common validation functions to export and be used
    TODO: Create a way to log validation errors encountered. Maybe define a 
          class that is initialized with an error message?
    """
    def __init__(self):
        self.validations = {}
        self.validation_errors = [] #TODO: Have a way of clearing this out if is_valid called mutliple times

    def is_valid(self):
        """
        Validates the object

        The object is validated by running through each of the attributes
        designated for validation and running the given validation function
        on each attribute value.
        Returns True if the object is valid, false otherwise
        """
        for attribute, validation_fn in self.validations.iteritems():
            try:
                value = getattr(self, attribute)
            except AttributeError:
                self.validation_errors.append('AttributeError: ' + attribute + ' is not defined.')

            if not validation_fn(value):
                self.validation_errors.append('ValidationFailure: ' + attribute + ' did not pass validation')
                return False

        # If we reached this point, all validations passed
        return True

    def get_validation_errors(self):
        """ Returns the list of validation errors logged by the validator """
        return self.validation_errors
