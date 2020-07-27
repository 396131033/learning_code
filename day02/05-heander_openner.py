import urllib.request

def  handler_openner():
    # 系统的urlopen并没有添加代理的功能所以需要我们自定义这个功能
    #安全 套接层 SSL 第三方的CA数字证书
    # http80端口 和 https443端口
    # urlopen为什么要请求数据 handler处理器
    # 自己的openner请求数据

    # urllib.request.urlopen()

    url = 'https://blog.csdn.net/wangqing84411433/article/details/89600335'
    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的openner
    opener = urllib.request.build_opener(handler)
    # 用自己创建的open方法请求数据
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)

handler_openner()
