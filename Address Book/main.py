# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from geopy.distance import geodesic
from typing import List
import logging

import models, schemas
from database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to create an address
@app.post("/addresses/", response_model=schemas.AddressInDB)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    """
    Create a new address and save it to the database.
    """
    logger.info("Creating a new address: %s", address)
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    logger.info("Created address with ID: %d", db_address.id)
    return db_address


# Endpoint to update an address
@app.put("/addresses/{address_id}", response_model=schemas.AddressInDB)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    """
    Update an existing address by its ID.
    """
    logger.info("Updating address with ID: %d", address_id)
    db_address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not db_address:
        logger.error("Address with ID %d not found", address_id)
        raise HTTPException(status_code=404, detail="Address not found")
    for key, value in address.dict().items():
        setattr(db_address, key, value)
    db.commit()
    db.refresh(db_address)
    logger.info("Updated address with ID: %d", db_address.id)
    return db_address


# Endpoint to delete an address
@app.delete("/addresses/{address_id}", response_model=schemas.AddressInDB)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    """
    Delete an address by its ID.
    """
    logger.info("Deleting address with ID: %d", address_id)
    db_address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not db_address:
        logger.error("Address with ID %d not found", address_id)
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(db_address)
    db.commit()
    logger.info("Deleted address with ID: %d", db_address.id)
    return db_address


# Endpoint to retrieve addresses within a given distance
@app.get("/addresses/within_distance/", response_model=List[schemas.AddressInDB])
def get_addresses_within_distance(lat: float, lon: float, distance_km: float, db: Session = Depends(get_db)):
    """
    Retrieve addresses within a given distance from specified coordinates.
    """
    logger.info("Fetching addresses within %f km of coordinates (%f, %f)", distance_km, lat, lon)
    addresses = db.query(models.Address).all()
    nearby_addresses = [
        address for address in addresses
        if geodesic((lat, lon), (address.latitude, address.longitude)).km <= distance_km
    ]
    logger.info("Found %d addresses within %f km", len(nearby_addresses), distance_km)
    return nearby_addresses
