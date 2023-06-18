#!/usr/bin/python3
"""
this script defines a City class
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, ForeignKey, String


class City(Base):
    """
    City class
    Attributes:
    id (int): the id of the class
    name (str): the name of the class
    state_id (int): the state the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
