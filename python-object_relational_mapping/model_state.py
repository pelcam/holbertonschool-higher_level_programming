#!/usr/bin/python3
'''
Module with the class definition of a State
and an instance Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    States class
    '''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
