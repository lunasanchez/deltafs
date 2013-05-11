__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"


from core.base import Singleton


time_to_get = None
cfg_path = None


class CfgParser(Singleton):

    def __init__(self):
        global time_to_get
        global cfg_path
        time_to_get = 3