from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from App.page.basepage import Base_func

# 添加联系人页面
class addcontractpage(Base_func):

    def goto_input(self):
        self.parse_yaml('goto_input')
        # self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 局部调用,点击进入输入成员信息页面
        from App.page.contractinputpage import contractinputpage
        return contractinputpage(self.driver)
