#!/usr/bin/python3
"""
Model containing the base ORM class
"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A state table representation in mysql db"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(120), nullable=False)
