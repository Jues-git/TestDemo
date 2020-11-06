import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class basepage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def reusebrowser(self):
        # 复用浏览器
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def get_cookies(self):
        # 获取当前页面cookies
        cookies = self.driver.get_cookies()
        print(f"企业微信的cookies是{cookies}")
        return cookies

    def save_cookies(self):
        #     # shelve 是Python 内置模块，专门对数据持久化存储，相当于小型数据库
        #     # 可以通过key , value 保存或者读取内容
        #     # 保存cookies 到 shelve
        cookies = self.get_cookies()
        db = shelve.open('cookie')
        db['cookie'] = cookies
        db.close()


    def read_cookies(self):
        # 读取shelve cookie免登录
        db = shelve.open('cookie')
        cookies = db['cookie']

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(3)
        db.close()
