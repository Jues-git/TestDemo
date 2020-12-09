from API.service.baseapi import BaseApi


# 部门信息类
class party(BaseApi):
    def __init__(self):
        sec = 'nh0T_jDjYFssVFdqmzr34g-2vbZTocIKR5dvPUkjX8A'
        super(party, self).__init__(sec)

    # 创建部门
    def create_party(self, name):
        # data = {"method": "post",
        #         "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
        #         "params": {"access_token": self.token},
        #         "json": {
        #             "name": name,
        #             "parentid": 1
        #         }}
        data = {"token": self.token,
                "value": name}
        # res = self.send(data)
        res = self.yaml_call('create_party', **data)
        return res

    # 获取部门列表
    def get_partyid(self, par_id=None):
        # par_id 为空时，获取所有部门信息
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
                "params": {"access_token": self.token, "id": par_id}}
        res = self.send(data)
        # res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/list",
        #                     params={"access_token": self.token})
        return res

    # 根据部门id获取部门成员列表
    def get_party_list(self, party_id):
        # data = {"method": "get",
        #         "url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
        #         "params": {"access_token": self.token,
        #                    "department_id": party_id}}
        # res = self.send(data)
        res = self.yaml_call('get_party_list', token=self.token, value=party_id)
        # res = self.get('https://qyapi.weixin.qq.com/cgi-bin/user/simplelist',
        #                    params={"access_token": self.token, "department_id": partyid})
        return res

    # 根据名字查找userid
    def get_contract_by_name(self, name, par_id=2):
        # 获取部门成员列表
        list_res = self.get_party_list(par_id)
        user_list = list_res.json()['userlist']
        try:
            for user in user_list:
                if name == user['name']:
                    return user['userid']

        except ValueError:
            print("根据名字没有找到成员")

    # 删除部门
    def del_party(self, party_id):
        data = {"method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                "params": {"access_token": self.token,
                           "id": party_id}}
        res = self.send(data)
        return res

    def department_list(self, par_id):
        # data = {'token': self.token,
        #         'value': par_id}
        res = self.yaml_call('department_list', token=self.token, value=par_id)
        return res
