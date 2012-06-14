#!/usr/bin/env python

from distutils.core import setup

setup(
    name        = 'human-datetimedelta',
    version     = '0.1',
    description = 'Human readable datetime deltas',
    author      = 'Col Wilson',
    author_email= 'colwilson@bcs.org',
    licence     = 'MIT License',
    url         = 'https://github.com/colwilson/human-datetimedelta/',
    packages    = ['human-datetimedelta'],
    requires    = ['datetime'],
)
