#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR="pdt"
LOCALE="en_US.utf8"
TIMEZONE = 'Asia/Saigon'
DATE_FORMATS="%H:%M %a %d %b %y"
SITENAME = "pdt's Blog!"

DISPLAY_PAGES_ON_MENU = True
WITH_PAGINATION = True
DEFAULT_PAGINATION = 5

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

# Path Meta Data
STATIC_PATHS = ['images', 'assets', 'extras', 'static']
EXTRA_PATH_METADATA = { 'extras/CNAME': {'path': 'CNAME'}, }

# URL Patterns
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

#======= BOOTSTRAP 3 THEMES RELATED
BOOTSTRAP_THEME = "flatly"
CUSTOM_CSS = 'static/css/build/custom_style.css'

#======= END BOOTSTRAP 3
# Theme
OUTPUT_PATH = "../output/blog"
THEME = "theme"

TYPOGRIFY = True
SHOW_DATE_MODIFIED = True
SHOW_ARTICLE_AUTHOR = True

DISPLAY_TAGS_ON_SIDEBAR = False
HIDE_SIDEBAR = True
TAG_CLOUD_STEPS = 1

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')

FAVICON = "extras/favicon"

### plugins

PLUGIN_PATHS = ['../plugins/']
PLUGINS = ['extract_toc', 'gist', ]
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid',
                 'toc(permalink=true)']


#
IGNORE_FILES = ['.#*', '*draft*']
