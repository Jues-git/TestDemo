from App.page.basepage import Base_func

# 工作台页面
class workbenchpage(Base_func):
    def goto_clock(self):
        # 点击工作台
        self.find(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动查找打卡，点击进入
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # 切换到外出打卡
        self.find(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 打卡操作
        self.find(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
