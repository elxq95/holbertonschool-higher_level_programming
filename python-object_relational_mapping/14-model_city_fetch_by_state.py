#!/usr/bin/python3
""" This module is for listing all city objects
from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
