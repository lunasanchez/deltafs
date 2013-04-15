__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from sqlalchemy import create_engine, exc, exists, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from persistence.orm import ORMNode, ORMFilesystem
from core.base import Node, FileSystem


class DB(object):
    def __init__(self, strConnect):
        ''' strConnect = sqlite:///delta.db
        '''
        engine = create_engine(strConnect, echo=True)
        Session = sessionmaker(bind=engine)
        self.connection = Session()
        self.Base = declarative_base()
        self.Base.metadata.create_all(engine)
        # con sqlite no respeta la constrain e inserta un id que no existe en node

    def saveFS(self, node=Node, fs=FileSystem):
        if node is not None and fs is not None:
            (ret, ), = self.connection.query(exists().where((ORMFilesystem.fs_name == fs.getName()) &
                                                            (ORMFilesystem.node_id == node.getId())))
            if ret:
                self.connection.add(fs)
                self.connection.commit()



if __name__ == '__main__':
    db = DB('sqlite:///deltafs.db')
