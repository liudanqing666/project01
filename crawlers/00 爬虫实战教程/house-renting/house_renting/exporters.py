# -*- coding: utf-8 -*-

# elasticsearch 是一个搜索引擎，它的可扩展性和速度都十分优越
# 在查询大批量数据的时候，它的速度能比 MySQL 快 1000 倍
# 基本教程可以参考：https://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/
# from elasticsearch import Elasticsearch
# from scrapy.conf import settings
from scrapy.exporters import BaseItemExporter


class ESItemExporter(BaseItemExporter):
    index = 'house_renting'
    doc_type = 'Post'

    def __init__(self, **kwargs):
        super(ESItemExporter, self).__init__(**kwargs)

        # self.elastic_hosts = settings.get('ELASTIC_HOSTS')

        # if self.elastic_hosts is not None:
        #     self.client = Elasticsearch(hosts=self.elastic_hosts)

    def start_exporting(self):
        pass

    def finish_exporting(self):
        pass

    def export_item(self, item):
        print('export item in ESItemExporter'.center(60, '*'))
        # 如果没有设置 elasticsearch，那么就直接返回 item
        if self.client is None:
            print(item)
            return item

        # item 在经过第一个 pipeline，也就是 HouseRentingPipeline 的时候，会被设置 item_id
        item_id = item['item_id']
        # 在 elasticsearch 中，一个 Elastic 实例可以有多个 index，这个 index 就相当于 database
        # 一个 index 可以有多个不同的 document type，相当于 table
        # indexing 一个 document 就相当于把这个 document 存储起来
        # 下面的 body 就是 document 的具体内容， id 是 document 的 ID
        self.client.index(index=self.index, doc_type=self.doc_type, body=dict(item), id=item_id)
        print(item)
        return item
