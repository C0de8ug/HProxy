import pymysql

from config import DB_URL, DB_PASSWORD, DB_USERNAME, DB_HOST


class MysqlHelper:
    def __init__(self):
        self.conn = pymysql.connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_URL)
        self.cursor = self.conn.cursor()

    def save(self, value):
        sql = 'INSERT INTO proxy(ip,port) VALUES(%s,%s)'
        proxy = [value['ip'],value['port']]
        self.cursor.execute(sql,proxy)
        self.commit()

    def update(self):
        pass

    def delete(self, proxy):
        sql = 'DELETE FROM proxy WHERE ip="%s" AND port="%s"'
        self.cursor.execute(sql%(proxy['ip'], proxy['port']))
        self.commit()
    def selectAll(self):
        sql = 'SELECT DISTINCT * FROM proxy'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def selectOne(self):
        sql = 'SELECT DISTINCT * FROM proxy'
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def selectByProxy(self, proxy):
        sql = 'SELECT * FROM proxy WHERE ip="%s" AND port="%s"'
        self.cursor.execute(sql %(proxy['ip'], proxy['port']))
        return self.cursor.fetchone()

    def batch_save(self, proxies):
        for proxy in proxies:
            if proxy != None:
                ret = self.selectByProxy(proxy)
                if(ret == None):
                    self.save(proxy)
        self.commit()

    def commit(self):
        self.conn.commit()


if __name__ == "__main__":
    DBHelper = MysqlHelper()
    proxy = {'ip': '192.168.1.2', 'port': '20'}
    # DBHelper.delete(proxy)
    ret = DBHelper.selectByProxy(proxy)
    ret2 = DBHelper.selectOne()
    ret3 = DBHelper.selectAll()
    DBHelper.save(proxy)
    # print(DBHelper.selectOne())
