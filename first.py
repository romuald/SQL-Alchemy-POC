from common import Base

from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relation
from sqlalchemy.types import Integer, BigInteger, DateTime, String, Enum

class Domain_(Base):
    __tablename__ = "Domain_"

    id = Column("domain_id", Integer, primary_key=True, autoincrement=True)
    fqdn = Column("fqdn", String)
    owner_id = Column(Integer, ForeignKey("Owner.id"))
    date_end = Column(DateTime)
    piapia = Column(String)

    def __repr__(self):
        return "<main Domain %s>" % self.fqdn


class Owner(Base):
    __tablename__ = "Owner"

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)

Domain_.owner = relation("Owner", primaryjoin=Domain_.owner_id==Owner.id)
