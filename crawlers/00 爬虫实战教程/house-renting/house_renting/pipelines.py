# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

# redis 是将数据存储在内存中的 DB
# import redis
# 并没有在 scrapy.conf 中看到 settings 模块
# from scrapy.conf import settings
# DropItem 用于丢弃 pipeline 中的 item
from scrapy.exceptions import DropItem

from house_renting.exporters import ESItemExporter

# 注意，pipeline 中的 print 信息在控制是打印不出来的，spider 中的 print 信息是可以打印出来的

# 设置 item 的 item_id
class HouseRentingPipeline(object):
    def process_item(self, item, spider):
        print('process item in HouseRentingPipeline'.center(60, '*'))
        total = len(item.get('title', ''))
        for i in range(total):
            print('*'*100)
            print(item.get('title', '')[i])
            print(item.get('source', '')[i])
            print(item.get('author', '')[i])
            print(item.get('author_link', '')[i])
            print(item.get('content', '')[i])
            print(item.get('source_url', '')[i])
            print(item.get('publish_time', '')[i])
            print('*'*100)

        m = hashlib.md5()
        m.update(item['source_url'].encode('utf-8'))
        # 将 item 的 item_id 设置为 source_url 的摘要值
        item['item_id'] = m.hexdigest()
        print(item)
        return item


# 检查 item 是否重复
class DuplicatesPipeline(object):
    def __init__(self):
        pass
        # redis_host = settings.get('REDIS_HOST')
        # redis_port = settings.get('REDIS_PORT', default=6379)

        # if redis_host is not None:
        #     self.r_client = redis.Redis(host=redis_host, port=redis_port)

    # 检查 item 是否已经存在，如果不存在，则返回 item，如果存在，则抛出异常
    def process_item(self, item, spider):
        print('process item in DuplicatesPipeline'.center(60, '*'))
        if self.r_client is None:
            print(item)
            return item

        if 'item_id' in item:
            item_id = item['item_id']
            existed_id = self.r_client.get(item_id)
            if existed_id is not None:
                raise DropItem("Duplicate item found: %s" % item)
            self.r_client.set(item_id, 'SEEN')

        print(item)
        return item


# 通过 elasticsearch 导出 item，这样速度会非常快
# elasticsearch 是一个非常快的搜索引擎，非常适合处理网页这样的数据
class ESPipeline(object):
    # 当 spider 被开启时，这个方法会被调用
    # 对应的还有 close_spider(self, spider) 函数
    # 当 spider 被关闭时，该方法会被调用
    # def open_spider(self, spider):
        # self.exporter = ESItemExporter()

    def process_item(self, item, spider):
        print('process item in ESPipeline'.center(60, '*'))
        self.exporter = ESItemExporter()
        self.exporter.export_item(item)
        # ESItemExporter 的 export_item 已经 return item，所以下面的代码可以直接注释掉
        # return item
