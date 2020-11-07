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
        self.driver.find_element(By.XPATH, '//*[@id="menu_apps"]/span').click()

    def test_addapp(self):
        name = str('My app') + str(random.randint(5,100))
        # 进入应用管理页面
        self.driver.find_element(By.XPATH, '//*[@id="menu_apps"]/span').click()
        # 查找创建应用元素
        app_el = self.driver.find_element(By.XPATH, '//*[@id="js_apps_createApiApp"]/div[2]')
        sleep(2)
        # 滚动查找元素
        self.driver.execute_script("arguments[0].scrollIntoView()", app_el)
        # 点击元素
        self.driver.execute_script("arguments[0].click()", app_el)
        sleep(2)
        # 点击上传logo
        self.driver.find_element(By.XPATH, '//*[@class="ww_updatePic"]/a').click()
        sleep(2)
        # 选择图片上传,“\””在Python中表示转义.
        # 解决方法当然就是不让“\”代表转义 ,加r 或者 R
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[2]/div/div[1]/div[2]/a/input'). \
            send_keys(r"C:\Users\Jues\PycharmProjects\pythonProject\webwx\timg.jpg")
        # 点击保存logo
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[3]/a[1]').click()
        # 输入应用名称
        self.driver.find_element(By.XPATH, '//*[@name="name"]'). send_keys(name)
        sleep(2)
        # 选择可见范围
        self.driver.find_element(By.XPATH, '//a[@class="apiApp_create_scopeItem_btn js_show_visible_add"]').click()
        # 选择成员
        sleep(3)
        el = self.driver.find_elements(By.XPATH, '//div[@class="multiPickerDlg_left_cnt"]//a[@id="1688851230578371_1688851230566654_anchor"]')
        for i in el:
            print(i.is_displayed())
            if i.is_displayed() == True:
                i.click()

        # 点击确认
        sure = self.driver.find_elements(By.XPATH, '//div[@class="qui_dialog_foot ww_dialog_foot"]/a[1]')
        for j in sure:
            print(j.is_displayed())
            if j.is_displayed() == True:
                j.click()
        sleep(2)
        # 点击创建应用
        self.driver.find_element(By.XPATH, '//a[@class="qui_btn ww_btn ww_btn_Blue ww_btn_Large apiApp_create_submitBtn js_create_app"]').click()

        sleep(2)
        meg = self.driver.find_element(By.XPATH, '//div[@id="js_tips"]').text
        assert "创建成功" in meg

        app_name = self.driver.find_element(By.XPATH, '//span[@id="js_app_name"]').text
        assert app_name == name

    def test_addcontract(self):
        username = str('测试') + str(random.randint(1, 100))
        account = str('CES') + str(random.randint(1, 100))
        phone = str('1501234') + str(random.randint(1000, 9999))
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 点击进入添加联系人页面
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        # 输入联系人名字
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        # 输入账号
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(account)
        # 选择男性
        self.driver.find_element(By.XPATH, "//input[@class='ww_radio' and @value='1' ]").click()
        # 选择女性
        # self.driver.find_element(By.ID, "//input[@class='ww_radio' and @value='2' ]").click()
        # 输入手机号
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        # 点击保存
        self.driver.find_element(By.XPATH, '//*[@class="js_member_editor_form"]/div[1]/a[2]').click()
        sleep(1)
        message = self.driver.find_element(By.ID, 'js_tips').text
        assert message == '保存成功'
        # 查找所有成员姓名,记住：find_elements
        names = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        print(names)
        titlelist = [element.get_attribute("title") for element in names]
        print(f'所有成员列表{titlelist}')
        # 检查新增成员是否在列表
        assert username in titlelist
