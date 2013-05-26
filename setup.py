#!/usr/bin/env python

from distutils.core import setup

setup(name='DeltaFS',
      version='0.0.7',
      description='FileSystem statistic collector',
      author='Jorge A. Medina',
      author_email='jorge@bsdchile.cl',
      url='http://github.com/mnothic/deltafs',
      packages=['src'],
      install_requires=['paramiko>=1.7',
                        'SQLAlchemy>=0.8'],
      )

