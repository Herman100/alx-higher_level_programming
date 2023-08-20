#!/usr/bin/python3
"""Defines the State class and an instance of Base."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state in a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
