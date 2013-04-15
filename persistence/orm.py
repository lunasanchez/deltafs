__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from sqlalchemy import Column, ForeignKey, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()


class ORMNode(Base):
    __tablename__ = 'node'
    node_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    node_name = Column(String, unique=True, nullable=False)
    node_os_name = Column(String, unique=True, nullable=False)
    node_login = Column(String, unique=True, nullable=False)
    node_password = Column(String, unique=True, nullable=False)

    def __init__(self, name, os):
        self.node_name = name
        self.node_os_name = os


class ORMFilesystem(Base):
    __tablename__ = 'filesystem'
    fs_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    node_id = Column(Integer, ForeignKey('node.node_id'))
    fs_name = Column(String, unique=True, nullable=False)
    fs_pmount = Column(String, nullable=False)

    def __init__(self, name, pmount):
        self.fs_name = name
        self.fs_pmount = pmount


class ORMStatus(Base):
    __tablename__ = 'status'
    status_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    fs_id = Column(Integer, ForeignKey('filesystem.fs_id'))
    status_size = Column(Integer, nullable=False)
    status_used = Column(Integer, nullable=False)
    status_date = Column(DateTime, nullable=False)

    def __init__(self, fs, size, used):
        self.fs_id = fs.getId()
        self.status_size = size
        self.status_used = used
        self.status_date = date.today()

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    strConnect = 'sqlite:///delta.db'
    engine = create_engine(strConnect, echo=True)
    Session = sessionmaker(bind=engine)
    connection = Session()
    Base = declarative_base()
    Base.metadata.create_all(engine)