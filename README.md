Data Aggregation System
=======================
The goal of this system is to collect political data about politicians and store
it within our PostgreSQL database.

Setup
-----
To set things up locally for development, refer to [this doc](https://docs.google.com/a/stanford.edu/document/d/1emM6B799iaysc8qCyycbOdt5ElYjxE2T8f4o9J_Py2g)

NOTE
====
In order for this project to run correctly, the PYTHONPATH must be correctly configured.
To ensure that the PYTHONPATH is correct, run the project in a virtualenv that has
the proper configuration files.

TODO
----
- Setup separate database for testing
- Link pg-start command with virtual environment startup, and pg-stop with virtualenv deactivation
- Write query interface layer
- Merge in data fetch layer 
