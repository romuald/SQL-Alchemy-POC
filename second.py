from common import Base

from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relation
from sqlalchemy.types import Integer, BigInteger, DateTime, String, Enum

class Domain_(Base):
    __tablename__ = "domain_"
    __table_args__ = {'mysql_engine':'InnoDB', 'schema': "second_db"}

    id = Column("dom_id", Integer, primary_key=True)
    fqdn = Column(String)
    status = Column(Integer)

    def __repr__(self):
        return "<sec Domain %s (%d)>" % (self.fqdn, self.status)

