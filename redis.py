import redis


class meth_redis:
    def setup(self):
        self.con = redis.Redis(host='localhost', port=6379, db=0)

    def set_redis(self):
        self.con.set('phone', '15012341234')

    def get_redis(self):
        self.con.get('phone')

    # 点击数的增加使用redis的INCR命令
    def incr_redis(self):
        self.con.incr('values')
    # 批量添加values
    def sadd_redis(self):
        self.con.sadd('circle', 'luo', 'xu', 'leo')
        # 查看circle成员
        self.con.smembers('circle')
        # 集合
        self.con.sunion('value1', 'value2')

    # 当有大量类型文档的对象，文档的内容都不一样时，（即“表”没有固定的列），可以使用hash来表达
    def hash_redis(self):
        self.con.hset('user:luo', 'phone', '1801232323')
        self.con.hset('user:luo', 'email', '123456@qq.com')
        self.con.hgetall('user:luo')
        # 返回{'phone', '1801232323' ,'email', '123456@qq.com'}



