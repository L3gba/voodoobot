# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field

from voodoo.models import NewsItem


class VoodooItem(DjangoItem):
    django_model = NewsItem