from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL-encoded password
DATABASE_URL = 'postgresql://postgres:Arun%4012345678@localhost:5432/My_Database'

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)
