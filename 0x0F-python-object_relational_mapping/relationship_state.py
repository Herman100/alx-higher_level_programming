#!/usr/bin/python3
"""Defines the State class with a cities relationship."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state in a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
        cities (sqlalchemy.orm.relationship): The state's cities.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
