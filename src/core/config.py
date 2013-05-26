__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from ConfigParser import ConfigParser, RawConfigParser, NoSectionError, ParsingError, Error, NoOptionError
from src.core.base import Singleton


class Config(Singleton):
    config = None
    cfg = dict()
    cfg['core'] = dict()
    cfg['core']['path'] = '/usr/local/deltafs'
    cfg['core']['schedule_time'] = 'montly'
    cfg['database'] = dict()
    cfg['database']['dbname'] = 'delta.db'
    cfg['database']['provider'] = 'sqlite'

    def __init__(self, cfg_file):
        self._validate_cfg(cfg_file)

    def _create_cfg(self, cfg_file):
        config = RawConfigParser()
        for section in self.cfg.iterkeys():
            config.add_section(section)
            for key, value in self.cfg[section].iteritems():
                config.set(section, key, value)
        with open(cfg_file, 'wb') as conf:
            config.write(conf)

    def _validate_cfg(self, cfg_file):
        if not self._exist_cfg(cfg_file):
            self._create_cfg(cfg_file)
        try:
            config = ConfigParser()
            config.read(cfg_file)
            for section in self.cfg.iterkeys():
                for key, value in self.cfg[section].iteritems():
                    self.cfg[section][key] = config.get(section, key)
                    print self.cfg[section][key]
            return True
        except ParsingError:
            print("Parsing Error")
            return False
        except NoSectionError:
            print("Section Error")
            return False
        except NoOptionError:
            print("No Option Error")
            return False
        except Error:
            print("Error during config validation")
            return False

    def _exist_cfg(self, cfg_file):
        try:
            with open(cfg_file):
                return True
        except IOError:
            print('config file not exist')
            return False

    def get(self, section, item):
        pass

    def set(self, setction, itme, value):
        pass

if __name__ == '__main__':
    cfg = Config('delta.cfg')