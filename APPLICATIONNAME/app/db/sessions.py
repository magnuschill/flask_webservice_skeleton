"""
This module manages provides sessions to a given database engine
"""
from sqlalchemy.orm import sessionmaker

def load_session(engine):
    """
    Instantiates a session and returns it to the caller.
    Caller is responsible for calling .close() on the return object
    When possible use one of the scoped sessions in this module instead
    """
    Session = sessionmaker(bind=engine)
    return Session()

def scoped_select(engine):
    """
    Provide a transactional scope around a series of operations.
    does not commit, making state accessible outside of scope
    """
    session = load_session(engine)
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

def scoped_session(engine):
    """Provide a transactional scope around a series of operations."""
    session = load_session(engine)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

