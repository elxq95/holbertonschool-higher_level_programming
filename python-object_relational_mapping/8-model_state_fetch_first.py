#!/usr/bin/python3
"""This module prints the first State object from the database hbtn_0e_6_usa."""

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
    
    # Create a Session
    session = Session()
    
    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()
    
    # Display the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    
    # Close the session
    session.close()
