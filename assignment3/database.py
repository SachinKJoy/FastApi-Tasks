from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the URL for the SQLite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Create a SQLAlchemy engine to connect to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session maker to generate database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base class for ORM models
Base = declarative_base()
