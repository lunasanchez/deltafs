__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from ConfigParser import ConfigParser
from base import Singleton

cfg = dict()
cfg['core'] = {'path': '/usr/local/deltafs',
               'schedule_time': 'montly'}

cfg['database'] = {'dbname': 'delta.db',
                   'provider': 'sqlite'}


class Config(Singleton):

    global cfg

    def __init__(self, cfg_file):
        config = ConfigParser()
        config.read(cfg_file)
        for section in cfg.iteritems():
            for k, v in section.iteritems():
                cfg[section] = dict(k=v)

    def get(self, item):
        return self.__getattribute__(item)

    def set(self, item, value):
        self.__setattr__(item, value)