#!/usr/bin/env python3

import codesh

from setuptools import setup

setup(name='codesh',
      version='2.0.0',
      setup_requires=['pyperclip==1.6.4', 'requests>=2.20.0'],
      author='Yunus Emre Geldegul',
      author_email='yunusemregeldegul@gmail.com',
      url='http://github.com/emregeldegul/codesh',
      packages=['codesh'],
      entry_points={
        'console_scripts': [
          'codesh = codesh:main',
        ]
      },
      license='Apache License 2.0'

      )
