"""
Database models used for representing DB data
"""
from app.db.some_database import Base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

class SomeTable(Base):
    """The user table which is needed to resolve an email address to a uid"""
    __tablename__ = 'SomeTable'
    recNum = Column(Integer, primary_key=True, nullable=False)
    userNum = Column(Integer, nullable=False)
    userId = Column(String(length=255), nullable=False)
