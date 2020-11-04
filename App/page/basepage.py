from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class basefuc:
    def __init__(self, driver: webdriver = None):
        self.driver = driver

    def get_toast_text(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result