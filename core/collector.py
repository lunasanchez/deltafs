__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"
from time import sleep
from paramiko import SSHClient
from paramiko import AutoAddPolicy
from paramiko import SSHException
from paramiko import BadHostKeyException
from paramiko import AuthenticationException
from core.base import FileSystem, Node
from persistence.database import DB


class Collector(object):

    def __init__(self):
        pass

    def mainLoop(self):
        while True:
            n = Node(id=1, name='localhost', osname='Linux', port='22', user='root', password='sinclave')
            print("{}".format(n.getName()))
            fsc = FSCollector()
            fsc.sshConnect(n)
            fsc.collectingNodeInfo(n)
            sleep(3)

    def getDataFrom(self, node=None):
        pass


class FSCollector(object):
    _ssh = None
    _OSName = None

    def __init__(self):
        self._ssh = SSHClient()

    def sshConnect(self, Node=None):
        """

        :param Node:
        :return:
        """
        try:
            self._ssh.set_missing_host_key_policy(AutoAddPolicy())
            self._ssh.connect(Node.getName(), username=Node.getUser(), password=Node.getPassword())
        except BadHostKeyException as sshErr:
            print("ssh error: {}".format(sshErr))
        except AuthenticationException as sshErr:
            print("ssh error: {}".format(sshErr))
        except SSHException as sshErr:
            print("ssh error {}".format(sshErr))
        return self

    def setOSName(self):
        """
        parse OS name as http://en.wikipedia.org/wiki/Uname

        """
        OSList = []
        OSList.append('AIX')
        cmd = 'uname -s'
        try:
            stdout = self._ssh.exec_command(cmd, 16, 10, False)
            self._OSName = stdout.read()
            stdout.close()
        except SSHException as sshErr:
            print("ssh connection error {}".format(sshErr))

    def collectingNodeInfo(self, node):
        out = None
        if node._os == 'HP-UX':
            cmd = 'bdf'
        else:
            cmd = 'df -k'
        try:
            stdin, stdout, stderr = self._ssh.exec_command(cmd)
            out = stdout.read()
        except SSHException:
            print('ssh error')

        self.setFSList(node, self.getFSList(out))
        print('collectingNodeInfo')

    def getFSList(self, df):
        """

        :param output:
        :return:
        """
        fsList = []
        i = 0
        for rs in df.split('\n'):
            row = rs.split()
            if i > 0 and len(row) > 0:
                fs = FileSystem(row[0], row[5], row[2], row[3])
                if not self._existFS(fsList, fs):
                    fsList.append(fs)
            i += 1
        return fsList

    def _existFS(self, fsList, fs):

        if len(fsList) == 0:
            return False

        for fsInst in fsList:
            if fsInst.getName() == fs.getName():
                return True

        return False

    def setFSList(self, node, FSList):
        for fs in FSList:
            db = DB('sqlite:///delta.db')
            db.saveFS(node, fs)

    def __del__(self):
        self._ssh.close()