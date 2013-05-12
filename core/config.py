__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from ConfigParser import ConfigParser
from base import Singleton


class Config(Singleton):

    def __init__(self, cfg_file):
        config = ConfigParser()
        config.read(cfg_file)
        stime = config.get('core', 'schedule_time')
        dbname = config.get('database', 'dbname')

    def get(self, item):
        return self.__getattribute__(item)

    def set(self, item, value):
        self.__setattr__(item, value)