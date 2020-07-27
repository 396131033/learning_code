import urllib.request
import random

def proxy_user():

    url = 'https://blog.csdn.net/wangqing84411433/article/details/89600335'

    proxy_list = [
        {'http':'120.77.249.46:8080'},
        {'http':'106.75.226.36:808'},
        {'http':'61.135.217.7:80'},
        {'http':'118.190.95.35:0001'},
        {'http':'125.70.13.77:8080'}

    ]

    for proxy in proxy_list:

        print(proxy)
        # first step: 创建代理处理器
        proxy_headler = urllib.request.ProxyHandler(proxy)

        opener = urllib.request.build_opener(proxy_headler)
        # data = opener.open(url).read()
        # print(data)
    #     有可能有的ip地址不能进行访问，使用try
        try:
            opener.open(url,timeout=1)    #时间间隔为1S
            print('============')
        except Exception as e:
            print(e)






    # # ============使用random.choice函数==============
    # # 创建代理服务器
    # random_proxy = random.choice(proxy_list)
    # print('the proxy ip is: ',random_proxy)
    # proxy_headler = urllib.request.ProxyHandler(random_proxy)
    # # 创建自己的opener
    # opener = urllib.request.build_opener(proxy_headler)
    # # 用自己创建的opener去访问数据
    # data = opener.open(url).read()
    # print(data)

proxy_user()