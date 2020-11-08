import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from App.single import find_mainblack


class basefuc:

    main_black = [(MobileBy.ID, '#id'), (MobileBy.ID, '.class')]
    contract_black = [(MobileBy.XPATH, '//*'), (MobileBy.XPATH, '//*')]
    max_num = 3
    error_num = 0

    def __init__(self, driver: webdriver = None):
        if self.driver is None:
            caps = {"platformName": "Android", "deviceName": "127.0.0.1:7555", "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.LaunchSplashActivity", "noReset": "True", "dontStopAppOnReset": "true",
                    'skipDeviceInitialization': 'true', 'newCommandTimeout': "60"}

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    # 添加黑名单装饰器
    @find_mainblack
    def find(self, by, locator=None):
        if locator is None:
            # 只有一个传参((By.ID , ".class"))
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator):
        if locator is None:
            # 只有一个传参((By.ID , ".class"))
            result = self.driver.find_elements(*by)
        else:
            result = self.driver.find_elements(by, locator)
        return result

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

    # 测试步骤yaml封装
    def parse_yaml(self, fucname):
        with open('action.yaml', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            steps = data[f"{fucname}"]
            for step in steps:
                if 'click' == step["action"]:
                    self.find(step["MobileBy"], step["locator"]).click()
                elif 'send' == step["action"]:
                    self.find(step["MobileBy"], step["locator"]).send_keys(step["content"])