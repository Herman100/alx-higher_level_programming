#!/usr/bin/python3
"""Creates the State "California" with the City "San Francisco" in the
database hbtn_0e_100_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    # Connect to a MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object with the name "California"
    new_state = State(name="California")

    # Create a new City object with the name "San Francisco"
    new_city = City(name="San Francisco", state=new_state)

    # Add the new City and State objects to the session
    session.add(new_city)
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
