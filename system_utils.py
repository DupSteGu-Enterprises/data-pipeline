"""
Provides system utilitie functions for the data pipeline project

Current utilities available: test, which sets up and runs the test environment
"""

from mock import patch
from config.settings import db_settings
from subprocess import call
from sqlalchemy.engine.url import URL
import sys
import fileinput


# List of available utilities
utilities = ['test']


def initialize_test_db():
    """ Sets up a test postgre user and the test database """
    print 'Setting up test database...\n'
    call([
        'createuser', '--no-superuser', '--no-createdb',
        '--no-createrole', 'dupstegu_test'
    ])
    call(['createdb', '-Odupstegu_test', '-Eutf8', 'dupstegu_test'])

def destroy_test_db():
    """ Destroys the test database and deletes the associated postgre user """
    print 'Destroying test database...\n'
    call(['dropdb', 'dupstegu_test'])
    call(['dropuser', 'dupstegu_test'])

def run_migrations():
    """ Runs the alembic migrations to bring the test db up to date """
    print 'Running migrations to update test dabatase...\n'
    call(['alembic', 'upgrade', 'head'])

def set_db_test_settings():
    """ Configures the system to use the tests database settings """
    call(['mv', 'config/settings/db_settings.py', 'config/settings/db_settings_temp.py'])
    call(['mv', 'config/settings/db_test_settings.py', 'config/settings/db_settings.py'])

def reset_original_settings():
    """ Restores system settings to the original, pre-test settings """
    call(['mv', 'config/settings/db_settings.py', 'config/settings/db_test_settings.py'])
    call(['mv', 'config/settings/db_settings_temp.py', 'config/settings/db_settings.py'])

def run_tests():
    """
    Runs the testing suite

    TODO: Configure this to be able to run specific tests
    """
    print 'Running tests...\n'
    call(['nosetests'])

def main(argv):
    if len(argv) < 2:
        print 'Invalid usage: Please specify what utility to run'
        return
    if argv[1] not in utilities:
        print 'Invalid usage: Please specify a valid utility'
        return
    if argv[1] == 'test':
        initialize_test_db()
        set_db_test_settings()

        # After changing settings, need to update alembic file 
        call(['python', 'db_setup.py', '--skip-createdb'])

        run_migrations()
        run_tests()
        reset_original_settings()

        # After tests, restore the alembic file to nontesting state
        call(['python', 'db_setup.py', '--skip-createdb'])

        destroy_test_db()

if __name__ == '__main__':
    main(sys.argv)
