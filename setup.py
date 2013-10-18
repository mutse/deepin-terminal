#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
from setuptools import setup, find_packages

setup(name='deepin-terminal',
      version='1.0',
      description='Deepin Terminal based on python-vte',
      author='Wang Yong',  
      author_email='lazycat.manatee@gmail.com',
      url='https://github.com/linuxdeepin/deepin-terminal',
      scripts=['deepin-terminal'],
      packages=find_packages(),
      data_files=[
        ('share/deepin-terminal/pixmaps/', glob.glob('data/*.png')),
        ('share/deepin-terminal/scripts/', glob.glob('data/scripts/*')),
      ],
)
