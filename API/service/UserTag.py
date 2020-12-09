from API.service.baseapi import BaseApi


class user_tag(BaseApi):
    def __init__(self):
        sec = 'nh0T_jDjYFssVFdqmzr34g-2vbZTocIKR5dvPUkjX8A'
        super(user_tag, self).__init__(sec)

    # 创建标签
    def create_tag(self, tag_name):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
                "params": {"access_token": self.token},
                "json": {"tagname": tag_name
                         }}
        res = self.send(data)
        return res

    # 获取标签列表
    def get_user_tag_list(self):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
                "params": {"access_token": self.token}}
        res = self.send(data)
        return res

    # 根据标签名称获取tag_id
    def get_tagid_by_tagname(self, tag_name):
        list_res = self.get_user_tag_list()
        name_list = list_res.json()['taglist']
        for name in name_list:
            if tag_name == name['tagname']:
                return name['tagid']

    # 更新标签名称
    def update_user_tag_name(self, tag_id, tag_name):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
                "params": {"access_token": self.token},
                "json": {"tagname": tag_name,
                         "tagid": tag_id
                         }}
        res = self.send(data)
        return res

    # 删除标签
    def del_user_tag(self, tag_id):
        data = {"method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
                "params": {"access_token": self.token},
                "json": {
                    "tagid": tag_id
                }}
        res = self.send(data)
        return res

    # 获取标签成员
    def get_user_tag_contract(self, tag_id):
        data = {"method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
                "params": {"access_token": self.token},
                "json": {
                    "tagid": tag_id
                }}
        res = self.send(data)
        return res

    # 增加标签成员
    def add_user_tag_contract(self, tag_id, user_list=None, party_list=None):
        # user_list、party_list不能同时为空
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
                "params": {"access_token": self.token},
                "json": {
                    "tagid": tag_id,
                    "userlist": user_list,
                    "partylist": party_list
                }}
        res = self.send(data)
        return res

    # 删除标签成员
    def del_user_tag_contract(self, tag_id, user_list=None, party_list=None):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
                "params": {"access_token": self.token},
                "json": {
                    "tagid": tag_id,
                    "userlist": user_list,
                    "partylist": party_list
                }}
        res = self.send(data)
        return res
