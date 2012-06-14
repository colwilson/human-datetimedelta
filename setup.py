#!/usr/bin/env python
'''
Examples::

    from datetime import datetime, timedelta

    now = datetime.now()
    an_hour_ago = now - timedelta(hours=1)
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)

    import human

    print human.date(now)                      # 'now'
    print human.date(an_hour_ago)              # 'an hour ago'
    print human.date(an_hour_ago, short=True)  # '1h ago'
    print human.date(an_hour_ago, asdays=True) # 'today'
    print human.date(yesterday, short=True)    # 'yest'
    print human.date(tomorrow)                 # 'tomorrow'

'''
from distutils.core import setup

setup(
    name        = 'human-datetimedelta',
    version     = '0.2',
    description = 'Human readable datetime deltas',
    long_description=__doc__,
    author      = 'Col Wilson',
    author_email= 'tersecol@gmail.com',
    license     = 'MIT License',
    platforms   = 'any',
    url         = 'https://github.com/colwilson/human-datetimedelta/',
    packages    = ['human'],
    requires    = ['datetime'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
