#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))		
from base_settings import *

# PRODUCTION CHANGE
SITEURL = "http://pdt.space/"
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

#SITEMAP
SITEMAP_SAVE_AS += ('sitemap.xml',)

# COMMENT
DISQUS_SITENAME="pdt-space"

#COMMENT
GOOGLE_ANALYTICS="UA-60741981-1"
