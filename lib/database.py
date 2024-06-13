from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

# Setup the database engine
engine = create_engine(config.DATABASE_URL)

# Setup the session
Session = sessionmaker(bind=engine)
session = Session()
