import urllib.request
import random

def load_baidu():
    url = "https://www.baidu.com"
    user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
                  ]
#     每次请求的浏览器都是不一样的
    random_user_agent = random.choice(user_agent_list)
    request = urllib.request.Request(url)

#     增加对应的请求头信息（user-agent)
    request.add_header("User-Agent",random_user_agent)

#     请求数据
    response = urllib.request.urlopen(request)
    # 获取请求头的信息
    print(request.get_header("User-agent"))



load_baidu()