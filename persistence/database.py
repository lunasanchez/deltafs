__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"


from persistence.orm import *


class DB(object):

    DBS = None

    def __init__(self, strConnect):
        ''' strConnect = 'sqlite:///delta.db'
        '''
        engine = create_engine(strConnect, echo=True)
        Session = sessionmaker(bind=engine)
        self.DBS = Session()
        Base.metadata.create_all(engine, checkfirst=True)
        # con sqlite no respeta la constrain e inserta un id que no existe en node

    def saveFS(self, node, fs):
        if node is not None and fs is not None:
            f = self.DBS.query(ORMFilesystem).filter(ORMFilesystem.fs_name==fs.getName(),
                                                         ORMFilesystem.node_id==node.getId())[0]
            if f is None:
                f = ORMFilesystem(node.getId(), fs.getName(), fs.getMountOn())
                self.DBS.add(f)
                self.DBS.commit()
                self.DBS.refresh(f)
                fs.setId(f.fs_id)
            else:
                fs.setId(f.fs_id)

    def saveStatus(self, fs):
        if node is not None and fs is not None:
            try:
                (ret, ), = self.DBS.query(exists().where(
                    (ORMFilesystem.fs_name==fs.getName())&(ORMFilesystem.node_id==node.getId())))
            except exc.OperationalError:
                raise
            if not ret:
                s = ORMStatus(fs.getId(), fs.getSize(), fs.getUsed())
                self.DBS.add(s)
                self.DBS.commit()


if __name__ == '__main__':
    db = DB('sqlite:///deltafs.db')
