#!/usr/bin/env python

from setuptools import setup


LONG_DESCRIPTION = '''
LOLcat
======

Straight Python port of the Ruby version at https://github.com/busyloop/lolcat/
but with 100% more fun, because, hey, it's not Ruby. There are no external dependencies..

It's a tool like cat, with added lulz.


Installing
==========

To install the stable version:

    $ pip install lolcat


To install the development version:

    $ pip install git+https://github.com/tehmaze/lolcat.git


Usage and examples
==================

![](https://github.com/tehmaze/lolcat/raw/master/lolcat.png)


Demo
====

Check out the ASCII cast at https://asciinema.org/a/1563


Bugs
====

Send a PR.
'''

setup(name='lolcat',
      version='1.3',
      description='Rainbows and unicorns!',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='Wijnand Modderman-Lenstra',
      author_email='maze@pyth0n.org',
      url='https://github.com/tehmaze/lolcat/',
      scripts=['lolcat'],
     )
