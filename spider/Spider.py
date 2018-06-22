import time

from gevent import monkey
from gevent.pool import Pool
from config import PROXYWEB_LIST, SLEEP_TIME, THREADNUM
from spider.HTMLParser import HTMLParser
from spider.HTMLDownloader import HTMLDownloader
from validator.Validator import Validator
from db.MysqlHelper import MysqlHelper

monkey.patch_all(thread=False)


class Spider():
    def __init__(self):
        self.poll = Pool(THREADNUM)

    def run(self):
        while True:
            print('*****************Spider Begin****************')
            pool = Pool(THREADNUM)
            proxyList = pool.map(self.crawl, PROXYWEB_LIST)

            temp = []
            for proxies in proxyList:
                temp.extend(proxies)
                # remove duplicates
            temp = [dict(x) for x in set([tuple(proxy.items()) for proxy in temp])]
            print('*****************Validator begin****************')
            validator = Validator()
            # todo i dont know whether this is efficient when i put two function in one pool
            proxys = pool.map(validator.validate, temp)
            proxys = [x for x in proxys if x is not None]

            dbHelper = MysqlHelper()
            dbHelper.batch_save(proxys)
            print('*****************Validator stop****************')

            print('*****************Spider are Pausing****************')
            time.sleep(SLEEP_TIME)

    def crawl(self, website):
        print('*****************Crawling From %s****************' % website['web'])
        proxies = []
        # this step will parse urls from a website to get proxies
        for url in website['urls']:
            resp = HTMLDownloader.download(url)
            if resp != None:
                proxyList = HTMLParser.parse(website, resp)
                proxies.extend(proxyList)
        print('*****************Crawling From %s Finish****************' % website['web'])
        return proxies

