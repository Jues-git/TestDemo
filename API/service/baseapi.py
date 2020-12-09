import requests
import yaml
from string import Template


class BaseApi:
    def __init__(self, sec):
        self.token = self.get_token(sec)

    # 根据不同应用秘钥获取token
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

    def yaml_call(self, interface_name, **kwargs):
        with open(r'C:\Users\Jues\PycharmProjects\pythonProject\API\service\set.yml', encoding='utf-8') as f:
            # 引入模板替换yaml文件的变量（$标识），其中Template方法需要传入一个字符串，
            # substitute方法传入关键字参数或者字典，注意key与yaml文件中的变量要对应
            temp = Template(f.read()).substitute(kwargs)
            para_list = yaml.safe_load(temp)
            data = {"method": para_list[interface_name]['method'],
                    "url": para_list['host']['test'] + para_list[interface_name]['path'],
                    "params": para_list[interface_name]['params']
                    }
            if para_list[interface_name]['method'] == 'get':
                res = self.send(data)
            elif para_list[interface_name]['method'] == 'post':
                data['json'] = para_list[interface_name]['json']
                res = self.send(data)
            else:
                res = self.send(data)

            return res
