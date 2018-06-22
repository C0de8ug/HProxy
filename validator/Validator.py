import time

import requests
from gevent import monkey

from config import HEADER, TEST_URL, TIMEOUT

monkey.patch_all(thread=False)


class Validator:
    def __init__(self):
        pass

    def validate(self, proxy):
        ip = proxy['ip']
        port = proxy['port']
        proxies = {'http': 'http://%s:%s' % (ip, port)}
        start = time.time()
        try:
            resp = requests.get(url=TEST_URL, headers=HEADER, timeout=TIMEOUT, proxies=proxies)
            if not resp.ok:
                print('fail ip = %s' % ip)
                proxy = None
            else:
                speed = round(time.time() - start, 2)
                proxy['speed'] = speed
                print('success ip = %s,speed = %s' % (ip, speed))

        except Exception as e:
            proxy = None
            print('fail ip = %s' % ip)
        return proxy
