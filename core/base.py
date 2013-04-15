__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"


class FileSystem(object):
    _name = None
    _size = None
    _used = None
    _mountOn = None

    def __init__(self, name, mount_on, size, used):
        self.setName(name)
        self.setMountOn(mount_on)
        self.setSize(size)
        self.setUsed(used)

    def getFS(self, id):
        self._id = id

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setSize(self, size):
        self._size = size

    def getSize(self):
        return self._size

    def setUsed(self, used):
        self._used = used

    def getUsed(self):
        return self._used

    def setMountOn(self, mount_on):
        self._mountOn = mount_on

    def getMountOn(self):
        return self._mountOn


class Node(object):
    _id = None
    _os = None
    _name = None
    _port = None
    _user = None
    _password = None

    def __init__(self, **kwargs):
        for key in kwargs:
            if key == 'id':
                self.setId(kwargs[key])
            if key == 'name':
                self.setName(kwargs[key])
            if key == 'osname':
                self.setOSName(kwargs[key])
            if key == 'port':
                self.setPort(kwargs[key])
            if key == 'user':
                self.setUser(kwargs[key])
            if key == 'password':
                self.setPassword(kwargs[key])

    def setId(self, node_id):
        self._id = node_id

    def getId(self):
        return self._id

    def setOSName(self, os):
        self._os = os

    def getOSName(self):
        return self._os

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setPort(self, port):
        self._port = port

    def getPort(self):
        return self._port

    def setUser(self, user):
        self._user = user

    def getUser(self):
        return self._user

    def setPassword(self, port):
            self._password = port

    def getPassword(self):
        return self._password

