from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

class Testclock():

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        caps["dontStopAppOnReset"] = "true"
        caps['skipDeviceInitialization'] = 'true'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_clock(self):
        # 点击工作台
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动查找打卡，点击进入
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # 切换到外出打卡
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 打卡操作
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        time.sleep(2)
        assert "外出打卡成功" in self.driver.page_source