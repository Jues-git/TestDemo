import pytest


@pytest.fixture(scope="module")
def start_calc():
    print("开始运算fix")
    yield
    print("结束运算fix")