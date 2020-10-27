from time import sleep
import allure
import pytest
from selenium import webdriver


@allure.feature("百度搜索")
@pytest.mark.parametrize('data', ['python', 'selenium', 'java'])
@allure.story("百度搜索测试用例")
def test_demo(data):
    driver = webdriver.Chrome()
    with allure.step("打开百度网址"):
        driver.get("http://www.baidu.com")
    sleep(2)
    with allure.step(f"搜素关键字:{data}"):
        driver.find_element_by_id("kw").send_keys(data)
        driver.find_element_by_id("su").click()
    sleep(2)
    with allure.step(f"保存{data}搜索截图"):
        driver.save_screenshot(f'./image/{data}.png')
        sleep(2)
        allure.attach(f"./image/{data}.png", name=f'{data}图片', attachment_type=allure.attachment_type.JPG)
    with allure.step("关闭浏览器"):
        driver.close()


# if __name__ == "__main__":
#     test_demo(data='ios')

# @allure.feature("登录模块")
#
# @allure.story("登录成功")
#
# @allure.title("")
#
# @allure.step("")
#
# with allure.step("步骤")
