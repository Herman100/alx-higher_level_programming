#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa.
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

    states = session.query(State).filter(
        State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()

    session.close()
