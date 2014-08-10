# Application settings used for testing

# Test database configuration
DATABASE = {'drivername': 'postgresql',
            'host': 'localhost',
            'port': '5432',
            'username': 'dupstegu_test',
            'password': 'root',
            'database': 'dupstegu_test'}

# The names of various database tables
POLITICIAN_TABLE = 'politicians'
TAG_TABLE = 'tags'
FUNDER_TABLE = 'funders'
POLITICIAN_FUNDERS_TABLE = 'politician_funders'
FUNDER_TAGS_TABLE = 'funder_tags'

# list of all existing database tables
TABLE_LIST = [
    POLITICIAN_TABLE,
    TAG_TABLE,
    FUNDER_TABLE,
    POLITICIAN_FUNDERS_TABLE,
    FUNDER_TAGS_TABLE,
]
