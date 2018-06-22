from config import RETRY_TIME, HEADER, TIMEOUT
import requests


class HTMLDownloader:
    @classmethod
    def download(self, url):
        count = 0
        try:
            resp = requests.get(url=url, headers=HEADER, timeout=TIMEOUT)
            resp.encoding = 'utf8'
            'if the reponse is not ok ,it could be baned by the host '
            if resp.ok:
                resp.encoding = 'utf8'
                return resp
            else:
                while count < RETRY_TIME:
                    'get proxy from redis'
                    proxy = {}
                    resp = requests.get(url=url, headers=HEADER, timeout=TIMEOUT, proxies=proxy)
                    if (resp.ok):
                        resp.encoding = 'utf8'
                        return resp
                    count += 1
        except Exception as e:
            print(e)
            while count < RETRY_TIME:
                proxy = {}
                # todo to test what will happen when this throws a exception
                try:
                    resp = requests.get(url=url, headers=HEADER, timeout=TIMEOUT, proxies=proxy)
                    if (resp.ok):
                        resp.encoding = 'utf8'
                        return resp
                    count += 1
                except Exception as e:
                    print(e)
                    count += 1
