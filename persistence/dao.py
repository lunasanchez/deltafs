__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"


from persistence.orm import *


class DAO(object):

    session = None

    def __init__(self, strConnect):
        """
        strConnect = 'sqlite:///delta.db'
        """
        engine = create_engine(strConnect, echo=True)
        SessionFactory = sessionmaker(bind=engine)
        self.session = SessionFactory()
        Base.metadata.create_all(engine, checkfirst=True)
        self.session.commit()
        # con sqlite no respeta o respeta cuando quiere, la constrain e inserta un id que no existe en node

    def saveNode(self, Node):
        if Node is not None:
            self.session.add(Node)
            self.session.commit()

    def saveFS(self, node, fs):
        if node is not None and fs is not None:
            n = self.session.query(Node).get(node.getId())
            if n is None:
                n = Node(node.getName(), node.getOSName(), node.getUser(), node.getPassword())
                self.session.add(n)
                self.session.commit()
                self.session.refresh(n)
            try:
                # fail because don't get anything, working in progress
                f = self.session.query(Filesystem).filter(Filesystem.fs_name == fs.getName(),
                                                      Filesystem.node_id == n.node_id).one()

                if f is None:
                    f = Filesystem(node.getId(), fs.getName(), fs.getMountOn())
                    self.session.add(f)
                    self.session.commit()
                    self.session.refresh(f)
                    fs.setId(f.fs_id)
                else:
                    fs.setId(f.fs_id)
            except:
                f = Filesystem(node.getId(), fs.getName(), fs.getMountOn())
                self.session.add(f)
                self.session.commit()
                self.session.refresh(f)
                fs.setId(f.fs_id)
                raise
            self.saveStatus(fs)

    def saveStatus(self, fs):
        if fs is not None:
            s = Status(fs.getId(), fs.getSize(), fs.getUsed())
            self.session.add(s)
            self.session.commit()

    def get_node_list(self):
        return self.session.query(Node).all()



if __name__ == '__main__':
    dao = DAO('sqlite:///deltafs.db')
