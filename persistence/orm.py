__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from sqlalchemy import Column, ForeignKey, DateTime, Integer, String
from sqlalchemy import create_engine, exc, exists
from sqlalchemy.orm import sessionmaker, relationship, backref
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

    def __init__(self, name, os, login, passwd):
        self.node_name = name
        self.node_os_name = os
        self.node_login = login
        self.node_password = passwd


class ORMFilesystem(Base):
    __tablename__ = 'filesystem'
    fs_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    node_id = Column(Integer, ForeignKey('ORMNode.node_id'))
    fs_name = Column(String, unique=True, nullable=False)
    fs_pmount = Column(String, nullable=False)
    #parent = relationship("ORMNode", backref=backref('children'))

    def __init__(self, node_id, name, pmount):
        self.node_id = node_id
        self.fs_name = name
        self.fs_pmount = pmount


class ORMStatus(Base):
    __tablename__ = 'status'
    status_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    fs_id = Column(Integer, ForeignKey('filesystem.fs_id'))
    status_size = Column(Integer, nullable=False)
    status_used = Column(Integer, nullable=False)
    status_date = Column(DateTime, nullable=False)

    def __init__(self, fs_id, size, used):
        self.fs_id = fs_id
        self.status_size = size
        self.status_used = used
        self.status_date = date.today()

if __name__ == '__main__':
    strConnect = 'sqlite:///delta.db'
    engine = create_engine(strConnect, echo=True)
    Session = sessionmaker(bind=engine)
    connection = Session()
    Base.metadata.create_all(engine)
    s = ORMStatus(1, 31333236, 16753516)
    n = ORMNode('localhost', 'Linux', 'root', 'sinclave')
    f = ORMFilesystem(1, '/dev/mapper/vg_sys-lv_root', '/')
    connection.add(n)
    connection.commit()
    connection.add(f)
    connection.commit()
    connection.add(s)
    connection.commit()