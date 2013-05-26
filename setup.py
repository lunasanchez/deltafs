#!/usr/bin/env python
__copyright__ = "Copyright (C) 2013 Jorge A. Medina"
__revision__ = "$"
__version__ = "$"
__author__ = "theManda"


from distutils.core import setup

setup(name='DeltaFS',
      version='0.0.7',
      description='FileSystem statistic collector',
      author='Jorge A. Medina',
      author_email='jorge@bsdchile.cl',
      url='http://github.com/mnothic/deltafs',
      packages=['src'],
      )

install_requires=[
   'paramiko>=0.97',
   'SQLAlchemy==0.5',
]