__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from core.collector import Collector
from core.config import CfgParser

if __name__ == '__main__':
    agent = Collector().run()
