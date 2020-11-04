from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from App.page.Minepage import minepage
from App.page.Workbenchpage import workbenchpage
from App.page.basepage import basefuc
from App.page.contractpage import contractpage


# APP主页
class mainpage(basefuc):
    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        caps["dontStopAppOnReset"] = "true"
        caps['skipDeviceInitialization'] = 'true'
        caps['newCommandTimeout'] = "120"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        return self

    def goto_main(self):
        return self

    def goto_contract(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return contractpage(self.driver)

    def goto_work(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        return workbenchpage(self.driver)

    def goto_mine(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='我']").click()
        return minepage(self.driver)

    def goback(self):
        self.driver.back()
