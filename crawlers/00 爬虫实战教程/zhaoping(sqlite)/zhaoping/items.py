# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    name = scrapy.Field()
    # 职位分类
    catalog = scrapy.Field()
    # 招聘人数
    numbers = scrapy.Field()
    # 职位低点
    location = scrapy.Field()
    # 职位发布日期
    dates = scrapy.Field()
