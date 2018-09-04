# -*- coding: utf-8 -*-

import datetime
import re
import time

import scrapy
# 查看源代码了解下面的模块的功能
# Join 相当于 python 中自带的 join 方法，用于将列表中的每个元素进行连接
# MapCompose 的参数是函数列表，MapCompose 处理的数据必须是序列，比如说列表、元组
# MapCompose 会将数据传入所有的函数进行处理，上一个函数的处理结果作为下一个函数的输入，相当于是对数据的多重处理
# Compose 的参数也是函数列表，但是 Compose 处理的数据没有要求是序列
# Compose 对数据的处理和 MapCompose 是一样的
# TakeFirst 用于获取第一个元素
from scrapy.loader.processors import Join, MapCompose, Compose, TakeFirst


def filter_title(value):
    return value.strip() if value != u'标题：' else None


# 如果 value 不为空，则返回 value，否则返回 None
def filter_content(value):
    return value if len(value) > 0 else None


# 返回时间的浮点表示方式
def publish_time_serializer_douban(value):
    # datetime.datetime.strptime 用于将时间从字符串类型转换为时间类型
    # time.mktime 用于将人能看得懂的时间转换为一个浮点类型的数据
    return int(time.mktime(datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S").timetuple()))


# 返回信息发布时间的浮点表示方式
def publish_time_serializer(value):
    # 获取具体的分钟、小时、天、日期
    minutes_ago = re.compile(u'.*?(\d+)分钟前.*').search(value)
    hours_ago = re.compile(u'.*?(\d+)小时前.*').search(value)
    days_ago = re.compile(u'.*?(\d+)天前.*').search(value)
    date = re.compile(u'.*?(\d+)-(\d+).*').search(value)

    # 根据当前时间和前面获得的时间信息计算租房信息的发布时间
    if minutes_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(minutes=int(minutes_ago.group(1)))
    elif hours_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(hours=int(hours_ago.group(1)))
    elif days_ago:
        publish_time = datetime.datetime.today() - datetime.timedelta(days=int(days_ago.group(1)))
    else:
        publish_time = datetime.datetime.today().replace(month=int(date.group(1)), day=int(date.group(2)))

    if publish_time is not None:
        return int(time.mktime(publish_time.timetuple()))


# 返回 58 网站的租房价格
def price_serializer_58(value):
    price = re.compile(u'\s*(\d+)\s*元/月.*').search(value)
    if price:
        return int(price.group(1))
    return None


# 租房基类
class HouseRentingBaseItem(scrapy.Item):
    item_id = scrapy.Field()
    title = scrapy.Field(input_processor=MapCompose(str.strip, filter_title),
                         output_processor=Compose(TakeFirst(), str.strip))
    # title = scrapy.Field()
    source = scrapy.Field(output_processor=Join())
    # source = scrapy.Field()
    author = scrapy.Field(input_processor=MapCompose(str.strip),
                          output_processor=Compose(Join(), str.strip))
    # author = scrapy.Field()
    # # image_urls = scrapy.Field()
    # # images = scrapy.Field()
    author_link = scrapy.Field(output_processor=Join())
    # author_link = scrapy.Field()
    # # 输出用换行连接，而不是默认的空格
    content = scrapy.Field(input_processor=MapCompose(str.strip, filter_content),
                           output_processor=Compose(Join(separator=u'\n')))
    # content = scrapy.Field()
    source_url = scrapy.Field(output_processor=Join())
    # source_url = scrapy.Field()
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip))
    # publish_time = scrapy.Field()


# 豆瓣租房类
class HouseRentingDoubanItem(HouseRentingBaseItem):
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip, publish_time_serializer_douban))
    # publish_time = scrapy.Field()


# 58租房类
class HouseRenting58Item(HouseRentingBaseItem):
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip, publish_time_serializer))
    # publish_time = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(str.strip),
                         output_processor=Compose(Join(), str.strip, price_serializer_58))
    # price = scrapy.Field()
    detail = scrapy.Field(input_processor=MapCompose(str.strip),
                          output_processor=Compose(Join(), str.strip))
    # detail = scrapy.Field()


# 链家租房类
class HouseRentingLianjiaItem(HouseRentingBaseItem):
    publish_time = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=Compose(Join(), str.strip, publish_time_serializer))
    # publish_time = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=Compose(Join(), str.strip))
    # price = scrapy.Field()
    detail = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=Compose(Join(), str.strip))
    # detail = scrapy.Field()
