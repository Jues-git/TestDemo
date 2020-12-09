import json
import random
import jsonpath

from API.service.contract import contract
from API.service.party import party


class Test_contract:
    def setup_class(self):
        self.man = contract()
        self.pa = party()

    # 添加成员
    def test_add_contract(self):
        phone = '133' + str(random.randint(10000000, 99999999))
        name = 'Li' + str(random.randint(1, 10000))
        res = self.man.create_contract(name, phone)
        print(json.dumps(res.json(), indent=2))
        assert res.status_code == 200
        assert res.json()['errcode'] == 0
        # 断言新增成员在部门列表
        list_res = self.pa.get_party_list(4)
        name_list = jsonpath.jsonpath(list_res.json(), '$..name')
        assert name in name_list

    # 根据userid获取成员信息
    def test_get_contract(self):
        name = 'cc21'
        # 根据名字查找userid
        userid = self.pa.get_contract_by_name(name)
        # 根据userid查找成员信息
        con_res = self.man.get_contract(userid)
        print(json.dumps(con_res.json(), indent=2, ensure_ascii=False))
        assert con_res.status_code == 200
        assert con_res.json()['errcode'] == 0
        assert name == con_res.json()['name']

    # 删除成员
    def test_del_contract(self):
        # 根据名字查找userid
        userid = self.pa.get_contract_by_name('cc')
        # 根据userid删除成员
        del_res = self.man.del_contract(userid)
        print(json.dumps(del_res.json(), indent=2, ensure_ascii=False))
        # 断言删除成员不在userid列表
        res = self.pa.get_party_list(2)
        userid_list = jsonpath.jsonpath(res.json(), '$..userid')
        assert res.status_code == 200
        assert res.json()['errcode'] == 0
        assert userid not in userid_list

    def test_update_contract(self):
        new_name = "new_cc"
        # 根据名字查找userid
        userid = self.pa.get_contract_by_name('cc1')
        # 根据userid更新成员
        update_res = self.man.update_contract(userid, new_name)
        print(json.dumps(update_res.json(), indent=2))
        # 断言更新成员信息
        res = self.pa.get_party_list(2)
        name_list = jsonpath.jsonpath(res.json(), '$..name')
        assert res.status_code == 200
        assert res.json()['errcode'] == 0
        assert new_name in name_list

    def test_batch_delete_contract(self):
        # 根据部门id获取userid列表
        res = self.pa.get_party_list(3)
        userid_list = jsonpath.jsonpath(res.json(), '$..userid')
        # 根据userid列表批量删除成员
        batch_res = self.man.batchdel_contract(userid_list)
        print(batch_res.json())
        assert batch_res.status_code == 200
        assert batch_res.json()['errcode'] == 0
