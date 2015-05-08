#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Paul W. Joireman'
SITENAME = u'Technically Me - Paul W. Joireman'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

THEME = "gum"
#THEME = "blueidea"

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Site built by Pelican', 'http://getpelican.com/'),
         ('Powered by Python', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('physIQ, Inc.', 'http://www.physiq.com'),)

# Social widget
SOCIAL = (('LinkedIn Profile', 'https://www.linkedin.com/pub/paul-joireman/3/a5b/334'),
          ('@PaulJoireman', 'https://twitter.com/PaulJoireman'),
          ('github', 'https://github.com/joireman'),)
     
STATIC_PATHS = ['images', 'pdfs']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
