from appium.webdriver.common.mobileby import MobileBy

from App.page.basepage import basefuc


class delpage(basefuc):

    def delmenber(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        # 点击确定删除成员
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()



