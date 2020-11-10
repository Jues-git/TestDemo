from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from App.page.addcontractpage import addcontractpage
from App.page.basepage import Base_func
from App.page.personinfo import Personinfo

# 联系人页面
class contractpage(Base_func):

    def goto_addcontract(self):
        self.find(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        # self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return addcontractpage(self.driver)

    def goto_presoninfo(self, name):
        self.find(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text({name}).instance(0));').click()
        return Personinfo(self.driver)

    def find_and_click(self, name):
        # 点击搜索框
        self.find(MobileBy.ID, 'com.tencent.wework:id/hxw').click()
        # 向搜索框输入成员名字
        self.find(MobileBy.ID, 'com.tencent.wework:id/ghu').send_keys(name)
        # 显示等待查询结果
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.ID, "com.tencent.wework:id/ebx"))
        try:
            element = self.find(MobileBy.ID, 'com.tencent.wework:id/ebx')
        except NoSuchElementException as E:
            print("查找的元素不存在")
        else:
            element.click()
         # self.find(MobileBy.ID, 'com.tencent.wework:id/ebx').click()

        return Personinfo(self.driver)

    def find_none(self, member):
        # 点击搜索框
        self.find(MobileBy.ID, 'com.tencent.wework:id/hxw').click()
        # 向搜索框输入成员名字
        self.find(MobileBy.ID, 'com.tencent.wework:id/ghu').send_keys(member)
        # 查无结果
        ele_none = self.find(MobileBy.ID, 'com.tencent.wework:id/ca0')
        # 判断元素是否存在
        try:
            ele_none
        except:
            print("删除失败")
        else:
            print("删除成功")
        # 判断元素是否存在
        if ele_none is True:
            print('查询的成员不存在')
            return '删除成功'
        else:
            print("删除失败")

