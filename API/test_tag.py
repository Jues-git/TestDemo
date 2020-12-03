import json
import jsonpath
import pytest

from API.service.tag import Tag


class Test_tag:
    def setup_class(self):
        self.main = Tag()

    # 新增标签参数化
    @pytest.mark.parametrize('tag_name_1, tag_name_2, tag_name_3', [
        ('tag1', 'tag2', 'tag3'), ('中文4', '中文5', '中文6'), ('中英文tag#7', '中英文tag#8', '中英文tag#9')
    ])
    def test_add_tag(self, tag_name_1, tag_name_2, tag_name_3):
        add_res = self.main.add_tag(tag_name_1, tag_name_2, tag_name_3)
        assert add_res.status_code == 200
        assert add_res.json()['errcode'] == 0
        list = self.main.get_tag_list()
        assert "中文4" in jsonpath.jsonpath(list.json(), '$..name')

    # 编辑标签
    def test_edit_tag(self):
        edit_res = self.main.edit_tag('etVUKCDwAAziERiSUWRpKWBuUu2l96WA', 'tag1_new_name')
        print(json.dumps(edit_res.json(), indent=2))
        assert edit_res.status_code == 200
        assert edit_res.json()['errcode'] == 0
        list = self.main.get_tag_list()
        assert 'tag1_new_name' in jsonpath.jsonpath(list.json(), '$..name')

    # 数据清理
    def test_clean_tag(self):
        list = self.main.get_tag_list()
        for tag_id in jsonpath.jsonpath(list.json(), '$..id'):
            del_res = self.main.del_tag(tag_id)
            assert del_res.status_code == 200
            assert del_res.json()['errcode'] == 0
