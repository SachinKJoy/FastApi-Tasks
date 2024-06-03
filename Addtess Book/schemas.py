from pydantic import BaseModel, Field, validator

# Define the base address model with Pydantic
class AddressBase(BaseModel):
    # Define fields for address attributes
    name: str
    street: str
    city: str
    state: str
    zip_code: str
    # Latitude must be between -90 and 90
    latitude: float = Field(..., ge=-90, le=90)
    # Longitude must be between -180 and 180
    longitude: float = Field(..., ge=-180, le=180)

    # Validator to ensure latitude is within valid range
    @validator('latitude')
    def latitude_must_be_valid(cls, v):
        if not (-90 <= v <= 90):
            raise ValueError('Latitude must be between -90 and 90')
        return v

    # Validator to ensure longitude is within valid range
    @validator('longitude')
    def longitude_must_be_valid(cls, v):
        if not (-180 <= v <= 180):
            raise ValueError('Longitude must be between -180 and 180')
        return v

# Define the address model for data stored in the database
class AddressInDB(AddressBase):
    # Include an ID field for database records
    id: int

    class Config:
        orm_mode = True  # Allows the model to be used with ORM (SQLAlchemy)

# Define the address model for creating new addresses
class AddressCreate(AddressBase):
    pass

# Define the address model for updating existing addresses
class AddressUpdate(AddressBase):
    pass
