__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"


from persistence.orm import *


class DB(object):

    dbs = None

    def __init__(self, strConnect):
        """
        strConnect = 'sqlite:///delta.db'
        """
        engine = create_engine(strConnect, echo=True)
        Session = sessionmaker(bind=engine)
        self.dbs = Session()
        Base.metadata.create_all(engine, checkfirst=True)
        self.dbs.commit()
        # con sqlite no respeta o respeta cuando quiere la constrain e inserta un id que no existe en node

    def saveNode(self, node):
        if node is not None:
            n = Node(node.getName(), node.getOSName(), node.getUser(), node.getPassword())
            self.dbs.add(n)
            self.dbs.commit()

    def saveFS(self, node, fs):
        if node is not None and fs is not None:
            n = self.dbs.query(Node).get(node.getId())
            if n is None:
                n = Node(node.getName(), node.getOSName(), node.getUser(), node.getPassword())
                self.dbs.add(n)
                self.dbs.commit()
                self.dbs.refresh(n)
            try:
                # fail because don't get anything, working in progress
                f = self.dbs.query(Filesystem).filter(Filesystem.fs_name == fs.getName(),
                                                      Filesystem.node_id == n.node_id).one()

                if f is None:
                    f = Filesystem(node.getId(), fs.getName(), fs.getMountOn())
                    self.dbs.add(f)
                    self.dbs.commit()
                    self.dbs.refresh(f)
                    fs.setId(f.fs_id)
                else:
                    fs.setId(f.fs_id)
            except:
                f = Filesystem(node.getId(), fs.getName(), fs.getMountOn())
                self.dbs.add(f)
                self.dbs.commit()
                self.dbs.refresh(f)
                fs.setId(f.fs_id)
                raise
            self.saveStatus(fs)

    def saveStatus(self, fs):
        if fs is not None:
            s = Status(fs.getId(), fs.getSize(), fs.getUsed())
            self.dbs.add(s)
            self.dbs.commit()


if __name__ == '__main__':
    db = DB('sqlite:///deltafs.db')
