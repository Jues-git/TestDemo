import requests


class BaseApi:
    def __init__(self, sec):
        self.token = self.get_token(sec)

    def get_token(self, secret):
        data = {"method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                "params": {'corpid': 'wwaef6630ed323a16a',
                           'corpsecret': secret}}
        res = self.send(data)
        return res.json()['access_token']

    def send(self, kwargs):
        res = requests.request(**kwargs)
        return res
