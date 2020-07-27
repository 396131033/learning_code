import urllib.request

def create_proxy_headler():
    url = 'https://blog.csdn.net/wangqing84411433/article/details/89600335'

    # 添加代理
    proxy = {
    #     免费的写法
    #     'http':'http://120.77.249.46:8080'
        'http':'120.77.249.46:8080'
    #     付费ip,要注册
    #     'http':'xiaoming':123@115
    }
    # 代理处理器
    proxy_headler = urllib.request.ProxyHandler(proxy)

    # 创建自己的opener
    opener = urllib.request.build_opener(proxy_headler)

    # 拿着代理IP去发送请求
    data = opener.open(url).read()
    print(data)

create_proxy_headler()