import random
import string
import pymysql


class meth_sql:
    def setup(self):
        self.con = pymysql.Connect('localhost', user="root", passwd="123456", db="mysql")
        self.cur = self.con.cursor()
        return self.cur

    def query_sql(self):
        sql = "select * from test_demo where id='1'"
        self.cur.execute(sql)
        # 获取全部结果
        rows = self.cur.fetchall()
        # 获取对象的描述信息
        print(self.cur.description)
        for i in rows:
            print(i)

        # 获取单条结果
        res = self.cur.fetchone()
        print("查询结果是：%s" % res)

        # 打印影响多少行
        print(self.cur.rowcount)

    def insert_sql(self):
        sql = "insert into test_demo values('2','','')"
        self.cur.execute(sql)
        print(self.cur.rowcount)
        self.con.commit()

    def del_sql(self):
        sql = "del from test_demo where id = '1'"
        self.cur.execute(sql)
        print(self.cur.rowcount)

    def teardown(self):
        self.cur.close()
        self.con.close()

    # 随机生成7位字符
    def rand_str(self, num, length=7):
        f = open('code.txt', 'w')
        for i in range(num):
            # string.ascii_letters 生成所有字母 ，string.digits生成所有数字
            # string.ascii_uppercase 生成大写字母， string.ascii_lowercase生成小写字母
            chars = string.ascii_letters + string.digits
            # random.choice(chars)从chars随机选取一个字符
            s = [random.choice(chars) for i in range(length)]
            f.write('{0}\n'.format(''.join(s)))
        f.close()
        # 另一种方法
        word = list(string.ascii_letters)
        # 随机排序
        random.shuffle(word)
        # 组合随机生成的7个字母
        st = ''.join(word[:7])
        print(st)
