import datetime

from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import config


class Database(object):
    def __init__(self) -> None:
        user = config.DB_USER
        password = config.PASSWORD
        host = config.HOST
        db_name = config.DATABASE
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}')
        self.connect_db()

    def connect_db(self) -> sessionmaker:
        Base.metadata.create_all(self.engine)
        session = sessionmaker(self.engine)
        return session


Base = declarative_base()
database = Database()


class BaseDatabase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)