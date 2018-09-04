import scrapy

from zhaoping.items import ZhaopingItem

class bbcSpider(scrapy.Spider):
    # name、start_urls和parse都是必须要定义的
    # name用于标识这个爬虫
    # start_urls指定爬虫开始抓取的起始链接
    # 爬虫开始抓取网页后，会把服务器发送过来的响应消息发送给parse
    name = "TencentZhaoping"
    start_urls = ["https://hr.tencent.com/position.php?&start=0#a",
                    "https://hr.tencent.com/position.php?&start=10#a",
                    "https://hr.tencent.com/position.php?&start=20#a",
                    "https://hr.tencent.com/position.php?&start=30#a",
                    "https://hr.tencent.com/position.php?&start=40#a"
    ]

    # xpath语法参考文档链接：
    # https://www.w3schools.com/xml/xpath_intro.asp
    # 定义如何解析爬取的数据
    def parse(self, response):
        print('parse item'.center(60, '*'))
        for sel in response.xpath('//table[@class="tablelist"]'):
            item = ZhaopingItem()
            item['name'] = sel.xpath('tr[@class!="h"]/td[1]/a/text()').extract()
            item['catalog'] = sel.xpath('tr[@class!="h"]/td[2]/text()').extract()
            item['numbers'] = sel.xpath('tr[@class!="h"]/td[3]/text()').extract()
            item['location'] = sel.xpath('tr[@class!="h"]/td[4]/text()').extract()
            item['dates'] = sel.xpath('tr[@class!="h"]/td[5]/text()').extract()
            print('来看看爬取的item：', item['name'], item['catalog'], item['numbers'], item['location'], item['dates'])
            yield item