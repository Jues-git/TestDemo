import random

import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from App.page.basepage import Base_func

# @allure.title("输入成员信息")
class contractinputpage(Base_func):

    # @allure.story('添加成员')
    def addcontract(self):
        name = str('测试') + str(random.randint(1, 999))
        gender = '女'
        phone = str(1501234) + str(random.randint(1000, 9999))
        with allure.step("输入姓名"):
            self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        with allure.step("选择性别"):
            self.find(MobileBy.ID, "com.tencent.wework:id/ehf").click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            if gender == '男':
                self.find(MobileBy.XPATH, "//*[@text='男']").click()
            elif gender == '女':
                self.find(MobileBy.XPATH, "//*[@text='女']").click()
        with allure.step("输入手机号"):
            self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        with allure.step("点击保存"):
            self.find(MobileBy.XPATH, "//*[@text='保存']").click()
            # 局部调用，返回添加联系人页面
            from App.page.addcontractpage import addcontractpage
            return addcontractpage(self.driver)
