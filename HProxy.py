import threading

from spider.Spider import Spider

class HProxy:
    def startSpider(self):
        spider = Spider()
        spider.run()

if __name__=='__main__':
    hproxy = HProxy()
    spider = threading.Thread(target=hproxy.startSpider)
    spider.start()
    # hproxy.startSpider()