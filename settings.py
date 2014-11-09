# -*- coding: utf-8 -*-
from scrapy.settings.default_settings import ITEM_PIPELINES


# Scrapy settings for voodoobot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'voodoobot'

SPIDER_MODULES = ['voodoobot.spiders']
NEWSPIDER_MODULE = 'voodoobot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'voodoobot (+http://www.yourdomain.com)'

import sys
sys.path.insert(0, r'C:\xampp\htdocs\Affiliate_sites\bvoodoo')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'bvoodoo.settings'

ITEM_PIPELINES = {
                  'voodoobot.pipelines.VoodoobotPipeline': 1000
                  }

EXTENSIONS = {
    'scrapy.contrib.closespider.CloseSpider':500, # To enable timeout for crawling
    }
CLOSESPIDER_TIMEOUT = 3600  # Max duration for crawling process, in seconds
DEPTH_LIMIT = '1'   # The depth of crawl

