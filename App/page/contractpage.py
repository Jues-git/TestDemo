from appium.webdriver.common.mobileby import MobileBy

from App.page.addcontractpage import addcontractpage
from App.page.basepage import basefuc

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

