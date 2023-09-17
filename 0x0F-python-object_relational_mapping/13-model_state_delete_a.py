#!/usr/bin/python3
"""
this script filter states using ORM
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

    delete_state = session.query(State)
    for state in delete_state:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
