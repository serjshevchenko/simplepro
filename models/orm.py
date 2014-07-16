from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/simplepro', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


register = {}


#**********************Public API******************************
def getEngine () :
    return engine


def getBase () :
    return Base


def getSession (name) :
    if not name in register :
        register[name] = Session()
    return register[name]
