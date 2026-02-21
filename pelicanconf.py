#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'AccidentalRebel'
SITENAME = 'AccidentalRebel.com'
SITEURL = ''
THEME = 'themes/rebel-minimal-theme'

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ()

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/juan-karlo-licudine/'),
          ('GitHub', 'https://github.com/accidentalrebel'))

BLURB = "SOC leader and content engineer at TryHackMe. Writing about AI, security tools, malware analysis, and reverse engineering."

DEFAULT_PAGINATION = 10

SUMMARY_END_MARKER = '<!-- PELICAN_END_SUMMARY -->'
SUMMARY_MAX_LENGTH = 50

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('Newsletter', '/category/cybersecurity-x-ai-news-roundup.html'),)

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

PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': { 'articles': 0.7, 'indexes': 0.5, 'pages': 0.3 },
    'changefreqs': { 'articles': 'monthly', 'indexes': 'daily', 'pages': 'monthly' }
}

#=============
# Twitter Card
#=============
# https://dev.twitter.com/cards
TWITTER_CARD_USE = (True) # (False)
TWITTER_CARD_SITE = '@accidentalrebel'  # The site's Twitter handle like @my_blog
TWITTER_CARD_SITE_ID = 'https://twitter.com/accidentalrebel'  # The site's Twitter ID
TWITTER_CARD_CREATOR = '@accidentalrebel'  # Your twitter handle like @monkmartinez
TWITTER_CARD_CREATOR_ID = 'accidentalrebel'  # The site creator's id
GRAVARTAR_URL = ''
