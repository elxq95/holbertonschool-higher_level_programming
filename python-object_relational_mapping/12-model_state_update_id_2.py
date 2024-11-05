#!/usr/bin/python3
"""This script changes the name of the State where id = 2 to 'New Mexico' in the database hbtn_0e_6_usa."""

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

    # Query for the state with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"  # Change the name to "New Mexico"
        session.commit()  # Commit the change

    # Close the session
    session.close()
