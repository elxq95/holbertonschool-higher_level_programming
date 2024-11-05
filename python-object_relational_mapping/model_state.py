#!/usr/bin/python3
"""This module defines a State model class that links to the 'states' table in a MySQL database."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

# Initialize the declarative base for SQLAlchemy ORM
Base = declarative_base()

class State(Base):
    """State class that represents the 'states' table in the database."""
    
    __tablename__ = 'states'

    # Define the 'id' column as a primary key, auto-incremented, unique, and not nullable
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    # Define the 'name' column as a string with max 128 characters and not nullable
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Ensure the command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Create a database engine connection using provided MySQL credentials
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create all tables defined in Base (only 'states' table here)
    Base.metadata.create_all(engine)