from sqlalchemy import Float, Column, Integer, String

# Import the Base class from the database module
from database import Base

# Define the Address model as a subclass of Base
class Address(Base):
    # Define the table name for the Address model
    __tablename__ = "addresses"

    # Define columns for each attribute of the address
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    name = Column(String, index=True)  # Name of the address (indexed)
    street = Column(String)  # Street address
    city = Column(String)  # City name
    state = Column(String)  # State name
    zip_code = Column(String)  # Zip code
    latitude = Column(Float)  # Latitude coordinate
    longitude = Column(Float)  # Longitude coordinate
