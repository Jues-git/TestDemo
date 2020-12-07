from API.service.baseapi import BaseApi


class contract(BaseApi):
    # 创建成员
    def create_contract(self, name, phone):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
                "params": {"access_token": self.token},
                "json": {
                    "userid": "test" + name,
                    "name": name,
                    "alias": "jack" + name,
                    "mobile": phone,
                    "position": "软件测试工程师",
                    "gender": "1",
                    "department": "3",
                    "email": name + "@gzdev.com"
                }}
        res = self.send(data)
        # res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
        #                     params={"access_token": self.token},
        #                     headers={'Content-Type': 'application/json; charset=UTF-8', 'Connection': 'keep-alive'},
        #                     json={
        #                         "userid": "test" + name,
        #                         "name": name,
        #                         "alias": "jack" + name,
        #                         "mobile": phone,
        #                         "position": "测试工程师",
        #                         "gender": "1",
        #                         "department": "2",
        #                         "email": name + "@gzdev.com"
        #                     })
        return res

    # 根据userid读取成员
    def get_contract(self, userid):
        data = {"method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
                "params": {"access_token": self.token, "userid": userid}}
        # res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/get',
        #                    params={"access_token": self.token, "userid": userid})
        res = self.send(data)
        return res

    # 根据userid更新成员信息
    def update_contract(self, userid, name):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
                "params": {"access_token": self.token},
                "json": {"userid": userid,
                         "name": name
                         }}
        res = self.send(data)
        # res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",
        #                     params={"access_token": self.token},
        #                     json={"userid": userid,
        #                           "name": "李四",
        #                           "position": "后台工程师",
        #                           "mobile": "13800000000",
        #                           "gender": "1",
        #                           "email": "zhangsan@gzdev.com"})
        return res

    def del_contract(self, userid):
        data = {"method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                "params": {"access_token": self.token, "userid": userid}
                }
        # res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
        #                    params={"access_token": self.token, "userid": userid})
        res = self.send(data)
        return res

    def batchdel_contract(self, args):
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",
                "params": {"access_token": self.token},
                "json": {"useridlist": args}
                }
        res = self.send(data)

        # res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",
        #                     params={"access_token": self.token},
        #                     json={"useridlist": args})
        return res
