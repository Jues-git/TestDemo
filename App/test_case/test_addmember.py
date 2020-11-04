from App.page.Mainpage import mainpage


class TestAddmember:
    def test_addmember(self):
        self.app = mainpage()
        result = self.app.goto_contract().goto_addcontract().goto_input().\
            addcontract(name='测试一', gender='女', phone='15012349990').get_toast_text()

        assert result == "添加成功"

