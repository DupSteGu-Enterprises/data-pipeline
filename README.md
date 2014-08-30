Data Aggregation System
=======================
The goal of this system is to collect political data about politicians and store
it within our PostgreSQL database.

Setup
-----
To set things up locally for development, refer to [this doc](https://docs.google.com/a/stanford.edu/document/d/1emM6B799iaysc8qCyycbOdt5ElYjxE2T8f4o9J_Py2g)

Tests
-----
To run tests, simply type `python system_utils.py test` from the project home directory. 
This will create a temporary testing database, run the entire test suite, and then 
destory the test database and restore the project back to the original development
state.

NOTE
====
In order for this project to run correctly, the PYTHONPATH must be correctly configured.
To ensure that the PYTHONPATH is correct, run the project in a virtualenv that has
the proper configuration files.

TODO
----
- Merge in data fetch layer
- Start building calculation API
- Write more tests, including tests for using models.. lots of session interaction
going on there, can and has led to some weird behavior
- Finish implementing validations
- Look further into python multiple inheritance to make `Validator` as slick as
possible
- Write tests for `Politician.get_total_contributions_for(...)`, I'm worried that the
`politician.contributions` line will break, because of circular dependencies between the
contributions and politicians models
- Set up python linting (pylint, pep8) to clean up codebase
