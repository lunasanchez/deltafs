__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"

from src.core.collector import Collector

if __name__ == '__main__':
    agent = Collector().run()
