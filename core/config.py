__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from ConfigParser import ConfigParser
from base import Singleton




class Config(Singleton):

    cfg = {}
    cfg['core'] = {}
    cfg['core']['path'] = '/usr/local/deltafs'
    cfg['core']['schedule_time'] = 'montly'
    cfg['database'] = {}
    cfg['database']['dbname'] = 'delta.db'
    cfg['database']['provider'] = 'sqlite'

    def __init__(self, cfg_file):
        config = ConfigParser()
        config.read(cfg_file)
        for section in cfg.iterkeys():
            for key in cfg[section].iteritems():
                cfg[section][key] = config.get(section, key)

    def get(self, item):
        return self.__getattribute__(item)

    def set(self, item, value):
        self.__setattr__(item, value)
