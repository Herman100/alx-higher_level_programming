#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database
hbtn_0e_6_usa, safe from MySQL injections.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
