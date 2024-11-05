#!/usr/bin/python3
"""This script adds the State object “Louisiana” to the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Database connection arguments
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine for the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)  # Add the new state to the session
    session.commit()  # Commit the changes to the database

    # Print the new state's id after creation
    print(new_state.id)

    # Close the session
    session.close()