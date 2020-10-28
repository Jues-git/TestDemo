import allure
import pytest
import yaml


def get_data():
    with open("./data.yml") as y:
        datas = yaml.safe_load(y)
        add_data = datas['add']['data']
        sub_data = datas['sub']['data']
        mul_data = datas['mul']['data']
        div_data = datas['div']['data']
        print(f"加法数据：{add_data}")
        print(f"减法数据：{sub_data}")
        print(f"乘法数据：{mul_data}")
        print(f"除法数据：{div_data}")
        return [add_data, sub_data, mul_data, div_data]


class Testcalc:

    def setup_class(self):
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @allure.title("加法运算")
    @pytest.mark.parametrize('a,b,expect', get_data()[0])
    def test_add(self, a, b, expect):
        result = a + b
        assert expect == result

    @allure.title("减法运算")
    @pytest.mark.parametrize('a,b,expect', get_data()[1])
    def test_sub(self, a, b, expect):
        result = a - b
        assert expect == result

    @allure.title("乘法运算")
    @pytest.mark.parametrize('a,b,expect', get_data()[2])
    def test_mul(self, a, b, expect):
        result = a * b
        assert expect == result

    @allure.title("除法运算")
    @pytest.mark.parametrize('a,b,expect', get_data()[3])
    def test_div(self, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                print("除数不能为0")

        else:
            result = a / b
            assert expect == result
