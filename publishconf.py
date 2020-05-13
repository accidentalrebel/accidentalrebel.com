
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
SITEURL = 'http://www.accidentalrebel.com'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

STATIC_PATHS = ['images', 'extras/CNAME']
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},}

SUMMARY_MAX_LENGTH = None
DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "AccidentalRebel"
DISQUS_URL = "https://accidentalrebel.disqus.com/"
GOOGLE_ANALYTICS = "UA-55068085-2"