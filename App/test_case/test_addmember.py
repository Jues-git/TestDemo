# import pytest
from App.page.Mainpage import mainpage


class TestAddmember():
    def setup(self):
        self.app = mainpage()
        self.man = self.app.start()

    def teardown(self):
        self.app.goback()

    # @pytest.mark.parametrize("name,gender,phone", [('测试M', '女', '15034324332'), ('测试B', '男', '15032337322')])
    def test_addmember(self):

        result = self.man.goto_contract().goto_addcontract().goto_input().\
            addcontract().get_toast_text()
        assert result == "添加成功"

