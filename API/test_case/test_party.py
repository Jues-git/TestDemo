import json

import jsonpath

from API.service.party import party


# 部门信息测试类
class Test_party:
    def setup_class(self):
        self.man = party()

    def test_create_party(self):
        name = '北京研发中心'
        res = self.man.create_party(name)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        assert res.status_code == 200
        assert res.json()['errcode'] == 0
        # 断言新创建部门在部门列表
        id_res = self.man.get_partyid()
        name_list = jsonpath.jsonpath(id_res.json(), '$..name')
        assert name in name_list

    # 获取部门列表
    def test_get_partyid(self):
        res = self.man.get_partyid()
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        assert res.status_code == 200
        assert res.json()['errcode'] == 0

    # 根据部门ID获取成员列表
    def test_get_contract_list(self):
        res = self.man.get_party_list(3)
        print(json.dumps(res.json(), indent=2))
        assert res.status_code == 200
        assert res.json()['errcode'] == 0

    # 根据名字查找userid
    def test_get_userid_by_name(self):
        name = "Li8950"
        res = self.man.get_contract_by_name(name, 3)
        print(res)
