#!/usr/bin/python3
"""This module lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa."""

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
    
    # Query State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()