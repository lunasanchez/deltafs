__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"


from persistence.orm import *


class DB(object):

    dbs = None

    def __init__(self, strConnect):
        ''' strConnect = 'sqlite:///delta.db'
        '''
        engine = create_engine(strConnect, echo=True)
        Session = sessionmaker(bind=engine)
        self.dbs = Session()
        Base.metadata.create_all(engine, checkfirst=True)
        # con sqlite no respeta la constrain e inserta un id que no existe en node

    def saveFS(self, node, fs):
        if node is not None and fs is not None:
            n = self.dbs.query(ORMNode).get(node.getId())
            if n is None:
                n = ORMNode(node.getName(), node.getOSName(), node.getUser(), node.getPassword())
                self.dbs.add(n)
                self.dbs.commit()
                self.dbs.refresh(n)
            f = self.dbs.query(ORMFilesystem).filter(ORMFilesystem.fs_name == fs.getName(),
                                                     ORMFilesystem.node_id == node.getId())[0]
            if f is None:
                f = ORMFilesystem(node.getId(), fs.getName(), fs.getMountOn())
                self.dbs.add(f)
                self.dbs.commit()
                self.dbs.refresh(f)
                fs.setId(f.fs_id)
            else:
                fs.setId(f.fs_id)
            self.saveStatus(fs)

    def saveStatus(self, fs):
        if fs is not None:
            f = self.dbs.query(ORMStatus).filter(ORMStatus.fs_id == fs.getId(),
                                                 ORMStatus.status_date.like(
                                                     "{}%".format(date.today()))
                                                )[0]
            if f is None:
                s = ORMStatus(fs.getId(), fs.getSize(), fs.getUsed())
                self.dbs.add(s)
                self.dbs.commit()


if __name__ == '__main__':
    db = DB('sqlite:///deltafs.db')
