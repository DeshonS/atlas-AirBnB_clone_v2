#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = ""
    name = Column('name', String(), nullable=False)
    state_id = Column('state_id', String(), nullable=False)
