#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Karlo Licudine'
SITENAME = 'AccidentalRebel.com'
SITEURL = ''
THEME = '/home/arebel/blog/arebel-themes/medium-rebel-fox'

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My dev blog', 'http://www.accidentalrebel.com/'),
         ('My maker blog', 'https://www.rebelmaker.me/'))

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/accidentalrebel'),
          ('Github','https://github.com/accidentalrebel'),
          ('YouTube', 'https://www.youtube.com/user/AccidentalRebelGames'))

BLURB = "Programmer from the Philippines. Co-founder and lead dev at @mindcakes. Currently delving into cyber security and pentesting. Also a #maker of game engines, electronics, and machines."

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'title': 'Table of contents:'
            }
        }
    }
