import yaml
from appium.webdriver.common.mobileby import MobileBy
import random
from App.page.MyDecorator import find_main_black


class Base_func:

    main_black = [(MobileBy.XPATH, '//*[@text="跳过"]')]
    # contract_black = [(MobileBy.XPATH, '//*'), (MobileBy.XPATH, '//*')]
    max_num = 3
    error_num = 0
    screenshot_name = str('screenshot') + str(random.randint(1, 100))

    def __init__(self, driver):
        self.driver = driver

    # 添加黑名单装饰器
    @find_main_black
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
    def parse_yaml(self, func_name):
        with open('./page/action.yaml', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            steps = data[func_name]
            for step in steps:
                if 'click' == step["action"]:
                    self.find(step["By"], step["locator"]).click()
                elif 'send' == step["action"]:
                    self.find(step["By"], step["locator"]).send_keys(step["content"])