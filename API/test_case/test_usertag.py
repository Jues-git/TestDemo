import json
import random

from jsonpath import jsonpath

from API.service.UserTag import user_tag


class Test_usertag:

    def setup_class(self):
        self.usertag = user_tag()

    # 获取客户标签列表
    def test_get_usertag_list(self):
        res = self.usertag.get_user_tag_list()
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 创建标签
    def test_create_usertag(self):
        tag_name = '技术部' + str(random.randint(1, 10000))
        res = self.usertag.create_tag(tag_name)
        if res.json()['errcode'] == 0:
            print("创建标签成功")
            # 断言新增标签在标签列表
            list_res = self.usertag.get_user_tag_list()
            print(json.dumps(list_res.json(), indent=2, ensure_ascii=False))
            name_list = jsonpath(list_res.json(), "$..tagname")
            # print(name_list)
            assert tag_name in name_list
        else:
            print("标签创建失败")
            print(res.json()['errmsg'])

    # 删除标签
    def test_del_usertag(self):
        # 根据标签名称获取tag_id
        tag_name = '技术部786'
        tag_id = self.usertag.get_tagid_by_tagname(tag_name)
        print(tag_id)
        # 删除标签
        del_res = self.usertag.del_user_tag(tag_id)
        if del_res.json()['errcode'] == 0:
            print("删除标签成功")
            # 断言删除标签不在标签列表
            list_res = self.usertag.get_user_tag_list()
            tagid_list = jsonpath(list_res.json(), '$..tagid')
            assert tag_id not in tagid_list
        else:
            print("删除标签失败,报错信息: %s" % del_res.json())

    # 获取标签成员
    def test_get_usertag_contract(self):
        # 根据标签名称获取tag_id
        tag_name = '技术部8708'
        tag_id = self.usertag.get_tagid_by_tagname(tag_name)
        # 根据tag_id获取标签成员
        con_res = self.usertag.get_user_tag_contract(tag_id)
        print(con_res.json())
        # assert con_res.json()['errcode'] == 0
