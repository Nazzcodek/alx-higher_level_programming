#!/usr/bin/python3
"""
This is the model city  module
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City object that inherits from Base
        __tablename__: mysql table name
        id: unique primary key
        name: city name
        state_id: foreign key from the states table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
