# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

# from redis import Redis
# from scrapy.conf import settings
# RetryMiddleware 用于尝试那些因为暂时性的问题而失败的请求，例如连接超时和 http500 错误
from scrapy.downloadermiddlewares.retry import RetryMiddleware

from house_renting import proxies

# 下面的中间件是按照 settings.py 中执行的顺序来定义的


# 该中间件用于随机选择一个 User--Agent 来发送 request，是反反爬虫的一个策略
class HouseRentingAgentMiddleware(object):
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        # 使用了上面的 @classmethod 之后，下面的 cls 就是指 HouseRentingAgentMiddleware
        # 使用了@classmethod 之后，创建 HouseRentingAgentMiddleware 对象就可以用 @classmethod 下面定义的方法
        # 在这里就是 from_crawler，例如： m1 = HouseRentingAgentMiddleware.from_crawle(c1)，其中的 c1 就是参数 crawler
        return cls(crawler.settings.getlist('USER_AGENTS'))

    # 随机设置 request 中的 User-Agent
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.user_agents))


# 该中间件用于随机选择一个代理来发送 request
# 随机代理是反反爬虫的一个策略
class HouseRentingProxyMiddleware(object):
    def __init__(self):
        # redis_host = settings.get('REDIS_HOST')
        # redis_port = settings.get('REDIS_PORT', default=6379)

        # if redis_host is not None:
        #    self.r_client = Redis(host=redis_host, port=redis_port)

        self.proxies = proxies.proxies

    def process_request(self, request, spider):
        if len(self.proxies) > 0:
            request.meta['proxy'] = random.choice(self.proxies)


# 下面随机选择一个代理来发送失败的 request
class HouseRentingRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        super(HouseRentingRetryMiddleware, self).__init__(settings)
        self.proxies = proxies.proxies

    def process_exception(self, request, exception, spider):
        # 如果设置了代理，那么随机选择一个代理来发送 request
        if len(self.proxies) > 0:
            request.meta['proxy'] = random.choice(self.proxies)
        return super(HouseRentingRetryMiddleware, self).process_exception(request, exception, spider)
