"""
This module manages the connection to the database and provides db sessions
"""
from . import sessions
from contextlib import contextmanager
from sqlalchemy import create_engine
from config import DATABASE_URI, SQLALCHEMY_ECHO, MYSQL_TIMEOUT
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(DATABASE_URI, echo=SQLALCHEMY_ECHO,
                       # May need a better solution for this 5 min mysql timeout
                       pool_recycle=MYSQL_TIMEOUT)

Base = declarative_base(engine)

def load_session():
    """
    Calls into sessions with a specific DB engine
    """
    return sessions.load_session(engine)

@contextmanager
def scoped_select():
    """
    Calls into sessions with a specific DB engine
    """
    return sessions.scoped_select(engine)

@contextmanager
def scoped_session():
    """
    Calls into sessions with a specific DB engine
    """
    return sessions.scoped_session(engine)
