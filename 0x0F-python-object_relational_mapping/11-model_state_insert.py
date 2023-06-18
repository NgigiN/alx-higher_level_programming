#!/usr/bin/python3
"""This script adds the State object "Louisiana"
to the database
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Access to the database"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print('{0}'.format(state.id))
    session.close()
