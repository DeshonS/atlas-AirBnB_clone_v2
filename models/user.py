#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import sqlalchemy as sqla

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = sqla.Column('email', sqla.string(), nullable=False)
    password = sqla.Column('password', sqla.string(), nullable=False)
    first_name = sqla.Column('first_name', sqla.string(), nullable=False)
    last_name = sqla.Column('last_name', sqla.string(), nullable=False)
