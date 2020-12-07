import requests


class BaseApi:
    def __init__(self):
        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                           params={'corpid': 'wwaef6630ed323a16a',
                                   'corpsecret': 'nh0T_jDjYFssVFdqmzr34g-2vbZTocIKR5dvPUkjX8A'})
        self.token = res.json()['access_token']

    def send(self, kwargs):
        res = requests.request(**kwargs)
        return res
