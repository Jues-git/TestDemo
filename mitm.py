import json

from mitmproxy import http


# 第一种方式
def request(flow: http.HTTPFlow):
    print(flow.request.url)
    if 'quote.json' in flow.request.url:
        with open(r'C:\Users\Jues\Desktop\json.txt', encoding='utf-8') as f:
            flow.response = http.HTTPResponse.make(200, f.read(), {'Content-Type': 'Application/json'})


# 第二种方式
def response(flow: http.HTTPFlow):
    print(flow.request.url)
    if 'quote.json' in flow.request.url and 'x=' in flow.request.url:
        data = json.loads(flow.response.content)
        second_name = data['data']['items'][1]['quote']['name']
        data['data']['items'][1]['quote']['name'] = second_name * 2
        data['data']['items'][2]['quote']['name'] = ''
        flow.response.text = json.dumps(data)
