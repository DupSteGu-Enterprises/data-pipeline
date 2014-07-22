# Simple script to do some configuration

from sqlalchemy.engine.url import URL
import fileinput
import settings

def config_alembic_ini_file():
    for line in fileinput.input("alembic.ini", inplace=True):
        if("sqlalchemy.url" in line):
            print "sqlalchemy.url = %s" %(URL(**settings.DATABASE)),
        else:
            print line,

if __name__ == "__main__":
    config_alembic_ini_file()
