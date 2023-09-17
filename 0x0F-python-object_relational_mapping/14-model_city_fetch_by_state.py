#!/usr/bin/python3
"""
this script filter states by city using ORM
script should take 3 arguments:
    mysql username,
    mysql password,
    database name
"""

import sys
from sqlalchemy import create_engine as e
from sqlalchemy.orm import sessionmaker
from model_city import City, Base
from model_state import Base, State

if __name__ == "__main__":
    engine = e("mysql+mysqldb://{}:{}@localhost/{}"
               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
               pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_state = session.query(City, State) \
                         .filter(City.state_id == State.id) \
                         .order_by(City.id)

    for city, state in fetch_state:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
