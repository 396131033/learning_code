# 1 记得安装 第三方 模块 requests
# pip install requests

import requests

class RequestSpider(object):
    def __init__(self):
        url = 'http://www.baidu.com'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        self.response = requests.get(url,headers=headers)
    def run(self):
        data = self.response.content

        # 1.获取请求头
        request_headers = self.response.request.headers
        print(request_headers)
        print('++++++++++')
        # 2.获取响应头
        request_headers = self.response.headers
        print(request_headers)
        print('++++++++++')

        # 3.获取响应状态码
        code = self.response.status_code
        print(code)
        print('++++++++++')

        # 4.请求的cookie  注意cookies前面有下划线'_'  _cookies
        cookie = self.response.request._cookies
        print(cookie)
        print('++++++++++')

        # 5.响应的cookie  注意这里的cookies 没有下划线
        cookie1 = self.response.cookies
        print(cookie1)
RequestSpider().run()