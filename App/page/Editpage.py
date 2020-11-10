from appium.webdriver.common.mobileby import MobileBy

from App.page.Delpage import delpage
from App.page.basepage import Base_func


class editpage(Base_func):
    # 点击进入删除成员页面
    def goto_delpage(self):
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return delpage(self.driver)
    # 推荐给他人
    def recommendother(self):
        pass
