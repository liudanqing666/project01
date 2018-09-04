# -*- coding: utf-8 -*-
from __future__ import print_function
from scrapy.spiders import CrawlSpider


class BaseCrawlSpider(CrawlSpider):
	# 58 和链家有多个城市的租房信息，对这两个网站，会针对支持的每个城市发送请求来获得租房信息
    # 所有的租房网站的爬虫都会继承这个爬虫，但是我们会在具体的爬虫中通过限制域名来限制每个爬虫具体爬取的网站
    # 这样的话每个爬虫就不会爬取所有网站的链接了
    def start_requests(self):
        cities = self.settings.get('cities', [])
        city_url_mappings = self.settings.get('available_cities_map', {})

        # 获得每个城市的租房信息
        for city in cities:
            city_url = city_url_mappings[city]
            if city_url is None:
                print('Cannot crawl house renting data from city: ', city)
            else:
                # 向指定城市发送租房请求链接
                yield self.make_requests_from_url(city_url)
