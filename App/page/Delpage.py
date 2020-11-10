from appium.webdriver.common.mobileby import MobileBy

from App.page.basepage import Base_func


class delpage(Base_func):

    def delmenber(self):
        self.find(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        # 点击确定删除成员
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()



