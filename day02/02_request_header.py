import urllib.request

import urllib.parse
import string


def load_baidu():
    url = "https://www.baidu.com"
    # header = {
    # #     浏览器的版本
    #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    #     "haha":"hehe"
    # }

    #创建请求对象
    request = urllib.request.Request(url)

    #请求网络数据(不在此处增加请求头信息因为此方法系统没有提供)
    # response = urllib.request.urlopen(url)
    response = urllib.request.urlopen(request)
    print(response)

    data = response.read().decode("utf-8")
    # #响应头
    # print(response.headers)

    #获取请求头的信息(打印所有的头的信息)
    # request_headers = request.headers
    # print(request_headers)

    # (2) 第二中方式打印headers的信息
    # 注意点：首字母需要大写，其他字母小写
    # request_headers = request.get_header("User-Agent")
    request_headers = request.get_header("User-agent")
    print(request_headers)
    with open('02header.html','w',encoding='utf-8')as f:
        f.write(data)

load_baidu()