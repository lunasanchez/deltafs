__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from sqlalchemy import create_engine, exc, exists, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from persistence.orm import ORMNode, ORMFilesystem


class DB(object):
    def __init__(self, strConnect):
        ''' strConnect = sqlite:///delta.db
        '''
        self.engine = create_engine(strConnect, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.connection = self.Session()
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.connection.commit()
        # con sqlite no respeta la constrain e inserta un id que no existe en node

    def saveFS(self, node=None, fs=None):
        if node is not None and fs is not None:
            try:
                (ret, ), = self.connection.query(exists().where(ORMFilesystem.fs_name == fs.getName()))
            except exc.OperationalError:
                n = ORMNode(node.getName(), node.getOSName(), node.getUser(), node.getPassword())
                self.connection.add(n)
                self.connection.commit()
            if ret:
                self.connection.add(fs)
                self.connection.commit()



if __name__ == '__main__':
    db = DB('sqlite:///deltafs.db')
