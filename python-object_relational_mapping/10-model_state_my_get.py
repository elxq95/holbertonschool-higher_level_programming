#!/usr/bin/python3
"""This module prints the State object with the name passed as an argument from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Database connection arguments
    username, password, dbname, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create an engine for the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query for the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()
    
    # Display the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    
    # Close the session
    session.close()
