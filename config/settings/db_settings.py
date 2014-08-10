# Application settings for configuring the database

# Database info for generating the db url
DATABASE = {'drivername': 'postgresql',
            'host': 'localhost',
            'port': '5432',
            'username': 'dupstegu',
            'password': 'root',
            'database': 'dupstegu'}

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
