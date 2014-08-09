from mock import patch
from config.settings import db_settings
from subprocess import call
import sys

utilities = ['test']

def initialize_test_db():
    print 'Setting up test database...'
    call([
        'createuser', '--no-superuser', '--no-createdb',
        '--no-createrole', 'dupstegu_test'
    ])
    call(['createdb', '-Odupstegu_test', '-Eutf8', 'dupstegu_test'])

def destroy_test_db():
    print 'Destroying test database...'
    call(['dropdb', 'dupstegu_test'])
    call(['dropuser', 'dupstegu_test'])

def run_migrations():
    """ Oh derp I need to change settings to use the test
    database before reaching this step lol """
    print 'Running migrations to update test dabatase...'
    call(['alembic', 'upgrade', 'head'])

@patch('config.settings.db_settings.DATABASE', new=db_settings.TEST_DATABASE)
def run_tests():
    """
    Patching here doesn't work... Which makes sense, the call to nosetests
    launches a separate process, derp.
    IDEA: Temporarily replace db_settings file with db_settings_test file.
    Would need to rename test settings file as 'db_settings' after saving
    actual settings in a temp file. Then when tests are done, we can delete
    the test file and rename the temp file back to 'db_settings'
    """
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
        run_migrations()
        run_tests()
        destroy_test_db()

if __name__ == '__main__':
    main(sys.argv)
