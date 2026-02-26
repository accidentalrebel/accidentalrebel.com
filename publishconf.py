
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.accidentalrebel.com'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

STATIC_PATHS = ['images', 'extras/CNAME', 'extras/robots.txt', 'extras/llms.txt']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/llms.txt': {'path': 'llms.txt'},
}

SUMMARY_MAX_LENGTH = 150
DELETE_OUTPUT_DIRECTORY = True
WITH_FUTURE_DATES = False
DRAFT_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''

# Following items are often useful when publishing

GOOGLE_ANALYTICS = "UA-55068085-2"
