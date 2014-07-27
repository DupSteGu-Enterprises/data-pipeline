# Simple script to do some database configuration

from sqlalchemy.engine.url import URL
from subprocess import call
import fileinput
from config import settings

def create_database():
    """
    System calls to create postgreSQL database

    These calls will raise errors if database already exists.
    That's okay, ignore them and move on.
    """
    call(["createuser", "dupstegu"])
    call(["createdb", "-Odupstegu", "-Eutf8", "dupstegu"])

def config_alembic_ini_file():
    """Configure our database in the alembic.ini file"""
    for line in fileinput.input("alembic.ini", inplace=True):
        if("sqlalchemy.url" in line):
            print "sqlalchemy.url = %s\n" %(URL(**settings.DATABASE)),
        else:
            print line,

if __name__ == "__main__":
    create_database()
    config_alembic_ini_file()
