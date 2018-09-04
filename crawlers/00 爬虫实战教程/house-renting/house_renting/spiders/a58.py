# -*- coding: utf-8 -*-
# LinkExtractor 是用来提取链接的
from scrapy.linkextractors import LinkExtractor
# Items 为抓取的数据提供了容器，而 ItemLoader 则是用于产生这样的容器的
from scrapy.loader import ItemLoader
# Rule 定义爬取网站的动作，如果多个 Rule 匹配了相同的链接，那么会执行第一个定义的 Rule
from scrapy.spiders import Rule

from house_renting.base_spider import BaseCrawlSpider
from house_renting.items import HouseRenting58Item



class A58Spider(BaseCrawlSpider):
    name = '58'
    allowed_domains = ['58.com']

    rules = (
    	# LinkExtractor：
    	#		allow：提取满足正则表达式的链接
    	#		restrict_css：最后会被转换到 restrict_xpaths 参数中，和 allow 共同过滤链接
    	# Rule：
    	#		follow: 是否跟进提取的链接。如果 callback 为 None，那么 follow 默认就是 True，否则是 False
    	#		callback: 用于处理 response，注意，不能是 parse 函数，否则 crawl spider 不能工作。
        #                   因为 CrawlSpider 使用 parse 来实现逻辑。这是官方文档说明。

        # 下面没有设置 callback 函数，因此会跟进匹配到的链接的子链接
        # (pn\d+/)? 指的是匹配 0 次或者 1 次
        # 在匹配了 allow 限定的 URL 之后，会对筛选后的 URL 继续用 restrict_css 筛选
        # 下面的这些筛选条件都是可以直接在网页中查看源代码看到的
        Rule(LinkExtractor(allow=(r'/zufang/(pn\d+/)?', r'/hezu/(pn\d+/)?', r'/chuzu/(pn\d+/)?'),
                           restrict_css='div.main > div.content > div.listBox > ul.listUl > li')),
        # \d+x\.shtml 用于匹配具体的房源页面
        Rule(LinkExtractor(allow=(r'/zufang/\d+x\.shtml', r'/hezu/\d+x\.shtml', r'/chuzu/\d+x\.shtml')),
             callback='parse_item'),
    )

    # 对用 rules 筛选出来的 response 进行处理
    def parse_item(self, response):
        print('parse_item'.center(60, '*'))
    	# 选择器简介：https://www.jianshu.com/p/1afa6ab6561d
        # 筛选 class 为 main-wrap 的 div
        item_loader = ItemLoader(item=HouseRenting58Item(), selector=response.css('div.main-wrap'), response=response)

        # 下面的 add_css、add_value，以及没有用到的 add_xpath 都是使用对应的方式来提取数据的函数
        # add_css，第一个参数是要提取的 Field 的名字，和 items.py 中的 item 定义的 Field 对象的变量名是一样的
        # 第二个参数是 css 表达式，用于过滤信息，提取符合表达式的内容
        # add_value，第一个参数同上，第二个参数并不用表达式，而是直接给第一个参数对应的 Field 对象赋值
        # 在上面的筛选的结果的基础之上继续进行筛选
        # 提取页面中的房源标题
        item_loader.add_css(field_name='title', css='div.house-title > h1::text')
        # 设置 source 为类中的 name，这里就是 58
        item_loader.add_value(field_name='source', value=self.name)
        # 提取页面中的发布房源的人的姓名
        item_loader.add_css(field_name='author', css='div.house-basic-info div.house-agent-info p.agent-name > a::text')
        # item_loader.add_css(field_name='image_urls', css='div.basic-pic-list > ul > li > img::attr(data-src)',
                            # re=r'(.*)\?.*')
        # 获取页面中的发布房源的人的链接
        item_loader.add_css(field_name='author_link',
                            css='div.house-basic-info div.house-agent-info p.agent-name > a::attr(href)')
        # 提取房源描述性信息
        item_loader.add_css(field_name='content', css='ul.introduce-item *::text')
        # 提取 response 的 URL
        item_loader.add_value(field_name='source_url', value=response.url)
        # 提取房源发布时间
        item_loader.add_css(field_name='publish_time', css='p.house-update-info::text')
        # 提取房租
        item_loader.add_css(field_name='price', css='div.house-pay-way *::text')
        # 提取房源具体信息，例如合租-主卧-男女不限、3室1厅1卫......
        item_loader.add_css(field_name='detail', css='div.house-desc-item > ul > li > span::text')

        # load_item 函数将用之前提取到的数据产生一个 item，在这里也就是 HouseRenting58Item。
        returnedItem = item_loader.load_item()
        print('打印item：', returnedItem)
        # yield item_loader.load_item()
        print('end parse item'.center(60, '*'))
        yield returnedItem
