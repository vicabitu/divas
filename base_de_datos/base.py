
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#Ver si uso la sesion aca
from sqlalchemy.orm import sessionmaker

from modelo import cliente

def inicio():

    print("Inicio base")

    engine = create_engine('sqlite:///divas.db', echo=True)

    Base = declarative_base()


    Base.metadata.create_all(engine)

