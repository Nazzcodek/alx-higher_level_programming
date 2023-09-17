#!/usr/bin/python3
"""
This is the model relationship state  module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    Model for state MySQL database table

        __tablename__ : Table name states.
        id: The state's id.
        name: The state's name.
        cities: The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
