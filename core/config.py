__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from ConfigParser import ConfigParser
from base import Singleton


class Config(Singleton):
    cfg = None
    config = None
    cfg['core']['path'] = '/usr/local/deltafs'
    cfg['core']['schedule_time'] = 'montly'
    cfg['database']['dbname'] = 'delta.db'
    cfg['database']['provider'] = 'sqlite'

    def __init__(self, cfg_file):
        config = ConfigParser()
        config.read(cfg_file)
        for section in self.cfg.iterkeys():
            for key in self.cfg[section].iteritems():
                self.cfg[section][key] = config.get(section, key)

    def get(self, section, item):
        return self.config.get(section, item)

    def set(self, section, item, value):
        self.config.set(section, item, value)
