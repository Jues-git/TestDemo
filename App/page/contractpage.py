from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from App.page.addcontractpage import addcontractpage
from App.page.basepage import basefuc
from App.page.personinfo import Personinfo

# 联系人页面
class contractpage(basefuc):

    def goto_addcontract(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return addcontractpage(self.driver)

    def goto_presoninfo(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("测试A").instance(0));').click()
        return Personinfo(self.driver)

    def find_and_click(self, name):
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hxw').click()
        # 向搜索框输入成员名字
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ghu').send_keys(name)
        # 显示等待查询结果
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.ID, "com.tencent.wework:id/ebx"))
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ebx').click()

        return Personinfo(self.driver)

    def find_none(self, member):
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hxw').click()
        # 向搜索框输入成员名字
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ghu').send_keys(member)
        # 查无结果
        ele_none = self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ca0')
        if ele_none:
            print('查询的成员不存在')

        return '删除成功'
