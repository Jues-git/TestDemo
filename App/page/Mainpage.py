from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from App.page.Minepage import minepage
from App.page.Workbenchpage import workbenchpage
from App.page.basepage import Base_func
from App.page.contractpage import contractpage


# APP主页
class mainpage(Base_func):

    def __init__(self):

        caps = {"platformName": "Android", "deviceName": "127.0.0.1:7555", "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity", "noReset": "True", "dontStopAppOnReset": "true",
                'skipDeviceInitialization': 'true', 'newCommandTimeout': "120"}

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)


    def start(self):
        self.driver.launch_app()
        return self

    def goto_contract(self):
        self.parse_yaml('goto_contract')
        # self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return contractpage(self.driver)


    def goto_work(self):
        self.parse_yaml('goto_work')
        # self.find(MobileBy.XPATH, "//*[@text='工作台']").click()
        return workbenchpage(self.driver)

    def goto_mine(self):
        self.parse_yaml('goto_mine')
        # self.find(MobileBy.XPATH, "//*[@text='我']").click()
        return minepage(self.driver)

    def goback(self):
            self.driver.back()


