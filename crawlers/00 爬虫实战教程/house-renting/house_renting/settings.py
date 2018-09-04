# -*- coding: utf-8 -*-
from house_renting.spider_settings import lianjia, a58

# 在使用 scrapy startproject 的时候使用的名字
BOT_NAME = 'house_renting'

COMMANDS_MODULE = 'house_renting.commands'
SPIDER_MODULES = ['house_renting.spiders']
NEWSPIDER_MODULE = 'house_renting.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 ' \
             'Safari/605.1.15 '

# 设置多个 USER_AGENTS 肯定是用来反反爬虫的
USER_AGENTS = (
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',


    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; '
    '.NET CLR 3.0.04506)',

    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR '
    '2.0.50727)',

    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',

    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR '
    '3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',

    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; '
    '.NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',

    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR '
    '3.0.04506.30)',

    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 ('
    'Change: 287 c9dfb30)',

    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',

    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',

    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',

    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',

    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',

    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 '
    'Safari/535.20',

    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 '
    'Safari/605.1.15',

    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',

)

# 如果设置为了 True，那么在爬取网络的时候，爬虫会遵守 robots.txt 的策略。
# 但是我这里并不想遵守，于是设置为了 False
# 默认创建的时候被设置为了 True
ROBOTSTXT_OBEY = False

# 下载下一个页面前需要等待的时间，这个可以用来限制爬取的速度，减轻服务器压力。
# 单位是秒，支持小数
# 设置延迟下载是反反爬虫的一种策略，通常设置为2秒或者更高
DOWNLOAD_DELAY = 1

# CONCURRENT_REQUESTS_PER_DOMAIN = 1

# 是否启用 cookie，下面将 cookie 禁用，禁用 cookie 是反反爬虫的一种策略。
COOKIES_ENABLED = False

# TELNETCONSOLE_ENABLED = False

# scrapy 默认发送的 http 头部
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# SPIDER_MIDDLEWARES = {
# }


# 下载中间件是位于引擎和下载器之间的一层组件
# 可以有多个下载中间件被加载运行
# 它们可以对 request 和 response 做额外的处理
# 设置下载中间件也是反反爬虫的一种策略
# 下面的设置中，key 是中间件的路径，value 是中间件执行的顺序
# DOWNLOADER_MIDDLEWARES_BASE 中的中间件默认是被执行的，如果想要禁用这些中间件
# 就要在 DOWNLOADER_MIDDLEWARES 中将这些中间件的 value 设置为 None
# 所以下面的 value 为 None 的中间件是不会被调用的
# DOWNLOADER_MIDDLEWARES = {
#     'house_renting.middlewares.HouseRentingAgentMiddleware': 100,
#     'house_renting.middlewares.HouseRentingProxyMiddleware': 200,
#     'house_renting.middlewares.HouseRentingRetryMiddleware': 300,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
# }

# 用于处理 item 的 pipeline，后面设置的数字越小，pipeline 的优先级越高，越先用这个 pipeline 来处理数据
# 所有的 pipeline 都会被用到来处理 item
ITEM_PIPELINES = {
    'house_renting.pipelines.HouseRentingPipeline': 100,
    'house_renting.pipelines.DuplicatesPipeline': 200,
    # 'scrapy.pipelines.images.ImagesPipeline': 300,
    'house_renting.pipelines.ESPipeline': 400,
}

# IMAGES_STORE = '/house-renting/data/images'

# MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 10
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = True

# 下载超时时间
DOWNLOAD_TIMEOUT = 10
# 重新下载最多次数
RETRY_TIMES = 3

# log 的最低级别。默认是 DEBUG。
# LOG_LEVEL = 'INFO'

SPIDER_SETTINGS = {
    'lianjia': {
        'cities': lianjia.cities,
        'available_cities': lianjia.available_cities,
        'available_cities_map': lianjia.available_cities_map,
    },
    '58': {
        'cities': a58.cities,
        'available_cities': a58.available_cities,
        'available_cities_map': a58.available_cities_map,
    },
}

# ES 节点, 可以配置多个节点(集群), 默认为 None, 不会存储到 ES
# ELASTIC_HOSTS = [
#     {'host': 'elastic', 'port': 9200},
#]

# REDIS_HOST = 'redis'  # 默认为 None, 不会去重
# REDIS_PORT = 6379  # 默认 6379
