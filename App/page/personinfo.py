from appium.webdriver.common.mobileby import MobileBy

from App.page.Editpage import editpage
from App.page.basepage import Base_func

# 个人信息页面
class Personinfo(Base_func):
    # 点击进入编辑成员页面
    def goto_editpage(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/hxm').click()
        return editpage(self.driver)
    # 设置备注
    def setnote(self):
        pass
