import os
import sys

from sqlalchemy import create_engine

from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relation
from sqlalchemy.types import Integer, BigInteger, DateTime, String, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
engine = create_engine('mysql://root@localhost/main_db')

Base = declarative_base()
_Session = sessionmaker(autoflush=False)

class Session(_Session):
    def __init__(self):
        return super(Session, self).__init__(bind=engine.connect())
