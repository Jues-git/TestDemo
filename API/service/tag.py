import random
import requests


class Tag:
    def __init__(self):
        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                           params={'corpid': 'wwaef6630ed323a16a',
                                   'corpsecret': 'wQO_AiGh5DBW0Rubyg80YT5Zl1IF_PMKgfOupIcHP6o'})
        assert res.status_code == 200
        assert res.json()['errcode'] == 0
        self.token = res.json()['access_token']

    # 新增标签
    def add_tag(self, tag1, tag2, tag3=None):
        group_name = '中文标签' + str(random.randint(1, 1000))
        res = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                            params={'access_token': self.token},
                            json={
                                "group_id": None,
                                "group_name": group_name,
                                "order": 3,
                                "tag": [{
                                    "name": tag1,
                                    "order": 1
                                },
                                    {
                                        "name": tag2,
                                        "order": 2
                                    },
                                    {
                                        "name": tag3,
                                        "order": 3
                                    }
                                ]
                            })
        return res

    # 获取tag列表
    def get_tag_list(self):
        res = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                            params={'access_token': self.token})
        return res

    # 编辑tag标签
    def edit_tag(self, tag_id, new_tag_name):
        res = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                            params={'access_token': self.token},
                            json={
                                "id": tag_id,
                                "name": new_tag_name,
                                "order": 1
                            })
        return res

    # 删除tag标签
    def del_tag(self, tag_id):
        res = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                            params={'access_token': self.token},
                            json={"tag_id": tag_id})
        return res
