import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:

    def setup_class(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # cookies = self.driver.get_cookies()
        # db = shelve.open('cookie')
        # db['cookie'] = cookies
        # db.close()
        # db = shelve.open('cookie')
        # cookies = db['cookie']
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.refresh()
        # sleep(3)
        # db.close()

    def test_addcontract(self):
        username = str('测试') + str(random.randint(1, 100))
        account = str('CES') + str(random.randint(1, 100))
        phone = str('1501234') + str(random.randint(1000, 9999))

        # 点击进入添加联系人页面
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        # 输入联系人名字
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        #输入账号
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(account)
        # 选择男性
        self.driver.find_element(By.XPATH, "//input[@class='ww_radio' and @value='1' ]").click()
        # 选择女性
        # self.driver.find_element(By.ID, "//input[@class='ww_radio' and @value='2' ]").click()
        # 输入手机号
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        # 点击保存
        self.driver.find_element(By.XPATH, '//*[@class="js_member_editor_form"]/div[1]/a[2]').click()
        sleep(3)
        #查找所有成员姓名,记住：find_elements
        names = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        print(names)
        titlelist = [element.get_attribute("title") for element in names]
        print(f'所有成员列表{titlelist}')
        # 检查新增成员是否在列表
        assert username in titlelist







