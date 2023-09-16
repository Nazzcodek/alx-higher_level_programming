#!/usr/bin/python3
"""
this script filter states using ORM nd print the first state
script should take 3 arguments:
    mysql username,
    mysql password,
    database name
"""

import sys
from sqlalchemy import create_engine as e
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = e("mysql+mysqldb://{}:{}@localhost/{}"
               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
               pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(first_state.id, first_state.name))
