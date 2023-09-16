#!/usr/bin/python3
"""
This is the model base module
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State object that inherits from Base
        __tablename__: mysql table name
        id: unique primary key
        name: State name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
