import pytest
import allure
import yaml


@pytest.fixture(scope=module)
def start_fixture():
    print:"开始运算"

class test_calce:

    @allure.title("加法运算")
    def test_add(self, a, b, expect):
        rusult = a + b
        assert expect == result

    @allure.title("减法运算")
    def test_sub(self, a, b, expect):
        result = a - b
        assert expect == result

    @allure.title("乘法运算")
    def test_mul(self, a, b, expect):
        result = a * b
        assert expect == result

    @allure.title("除法运算")
    def test_div(self, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                result = a / b
                print("除数不能为0")
        else:
            result = a / b
            assert expect == result
