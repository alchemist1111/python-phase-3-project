# Database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup the database engine
engine = create_engine('sqlite:///library.db')

# Setup the session
Session = sessionmaker(bind=engine)
session = Session()
