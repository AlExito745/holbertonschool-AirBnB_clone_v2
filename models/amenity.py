#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel):
    """
    Inherits from BaseModel and Base, amenities for the database
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary="place_amenity", backref="amenities")
