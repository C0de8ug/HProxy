TIMEOUT = 5
SLEEP_TIME = 30 * 60
RETRY_TIME = 3
MINNUN_IP_COUNT = 200
TEST_URL = 'http://www.cnblogs.com/'
HEADER = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}

'''
代理网站列表
'''
PROXYWEB_LIST = [
    {
        'url' : ['http://www.kuaidaili.com/free/%s/%s'% (n,m) for n in ['inha','outha'] for m in range(1,15)],
        'pattern': ".//*[@id='list']/table/tbody/tr[position()>0]",
        'position':{'ip':'./td[1]','port':'./td[2]','type':'./td[3]','protocol':'./td[4]'}
    },
    {
        'url': ['http://www.xicidaili.com/%s/%s' % (m, n) for m in ['nn','wn'] for n in range(1, 10)],
        'pattern': ".//*[@id='ip_list']/tr[position()>1]",
        'postion': {'ip': './td[2]', 'port': './td[3]', 'type': './td[5]', 'protocol': './td[6]'}
    }
]