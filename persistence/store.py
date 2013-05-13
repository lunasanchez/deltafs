__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from core.base import Singleton
from persistence.orm import *


class Store(Singleton):

    session = None

    def __init__(self, strConnect):
        """
        strConnect = 'sqlite:///delta.db'
        Nota:Con sqlite no respeta o respeta cuando quiere, la constrain e inserta un id que no existe en node
        te fumaras el cigarro te callaras y vendras a pedir perdon por las formas
        """
        engine = create_engine(strConnect, echo=True)
        SessionFactory = sessionmaker(bind=engine)
        self.session = SessionFactory()
        Base.metadata.create_all(engine, checkfirst=True)
        self.session.commit()

    def save_node(self, Node):
        if Node is not None:
            self.session.add(Node)
            self.session.commit()

    def save_fs(self, node_id, fs_name, mount_on, size, used):
        if node is not None and FS is not None:
            try:
                f = self.session.query(Filesystem).filter(Filesystem.fs_name == fs_name,
                                                          Filesystem.node_id == node_id).one()
                if f is None:
                    f = Filesystem(node_id, fs_name, mount_on)
                    self.session.add(f)
                    self.session.commit()
                    self.session.refresh(f)
                    fs_id = f.fs_id
                else:
                    fs_id = f.fs_id
            except:
                f = Filesystem(node_id, fs_name, mount_on)
                self.session.add(f)
                self.session.commit()
                self.session.refresh(f)
                fs_id = f.fs_id
                raise
            self.save_status(fs_id, size, used)

    def save_status(self, fs_id, size, used):
        status = Status(fs_id, size, used)
        self.session.add(status)
        self.session.commit()

    def get_node_list(self):
        return self.session.query(Node).all()



if __name__ == '__main__':
    store = Store('sqlite:///testdb.db')
