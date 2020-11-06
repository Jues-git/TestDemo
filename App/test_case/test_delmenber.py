from App.page.Mainpage import mainpage


class TestDelMember:
    def setup(self):
        self.app = mainpage()
        self.main = self.app.start()

    # def teardown(self):
    #     self.app.goback()

    def test_delmember(self):
        self.main.goto_contract().find_and_click('测试B').goto_editpage().goto_delpage().delmenber()
        self.app.goback()
        result = self.main.goto_contract().find_none('测试B')
        assert '删除成功' == result


