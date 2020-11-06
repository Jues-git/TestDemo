from appium.webdriver.common.mobileby import MobileBy

from App.page.Editpage import editpage
from App.page.basepage import basefuc

# 个人信息页面
class Personinfo(basefuc):
    # 点击进入编辑成员页面
    def goto_editpage(self):
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hxm').click()
        return editpage(self.driver)
    # 设置备注
    def setnote(self):
        pass
