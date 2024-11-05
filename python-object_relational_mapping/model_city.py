#!/usr/bin/python3
"""Fetches all City objects and displays them grouped by State."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Database connection setup
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)

    # Create a configured "Session" class and a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all City objects, joined with their respective State
    results = session.query(State.name, City.id, City.name).join(City).order_by(City.id).all()

    # Print each city's details in the desired format
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Close the session
    session.close()