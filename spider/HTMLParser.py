#coding:utf-8
from lxml import etree

class HTMLParser():
    def __init__(self):
        pass

    @classmethod
    def parse(self, item, resp):

        list = []
        root = etree.HTML(resp.text)
        proxys = root.xpath(item['pattern'])
        for proxy in proxys:
            ip = proxy.xpath(item['position']['ip'])[0].text
            port = proxy.xpath(item['position']['port'])[0].text
            type = proxy.xpath(item['position']['type'])[0].text
            # print(ip,port)
            if type.find(u'高匿') != -1:
                proxy = {'ip':ip,'port':port}
                list.append(proxy)
        return list

