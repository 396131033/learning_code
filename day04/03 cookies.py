"""
    https://www.yaozh.com/
    用户名：hello666  18798726635
    pwd :jxy120110
    获取 登录后的页面

    1、代码登录 登录成功 cookie（有效）
    2、 自动带着cookie 去请求登录后的页面
    cookiejar 自动保存这个Cookie
"""
import urllib.request
from http import cookiejar
from urllib import parse
# 1. 代码登录
#     1.1 登录的网址
# 登录之前的 登录页的网址 https://www.yaozh.com/login/ 找登录 参数
#  后台 根据你发送的请求方式来判断的 如果你是get（登录页面），如果POST（登录结果）
login_url ='https://www.yaozh.com/login/'
#     1.2 登录的参数（即：用户名和密码）
login_form_data = {

    "username" : "hello6666",
    "pwd" : "jxy120110",
    "formhash" : "635D7203C4",
    "backurl" : "https%3A%2F%2Fwww.yaozh.com%2F"
}

# 1. 参数 将 需要转译，转码；2 post的 data要求是bytes,所以要encode('utf-8')
login_str = parse.urlencode(login_form_data).encode('utf-8')

#     1.3 发送登录的请求 (POST)
cook_jar = cookiejar.CookieJar()
# 定义有添加 cookie 功能的 处理器
cook_hanlder = urllib.request.HTTPCookieProcessor(cook_jar)
# 根据处理器 生成 opener
opener =  urllib.request.build_opener(cook_hanlder)

# 带着参数 发送post请求
# 添加请求头 这里没有cookie 因为还没有登录，登录成功才有cookie
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
login_request = urllib.request.Request(login_url,headers = headers,data = login_str)
# 如果登录成功，cookie自动保存cookie,不用管返回什么，只用登录成功，cookiejar自动获取并保存cookie
opener.open(login_request)


# 2. 代码带着cookie去访问 登录后的页面
center_url = 'https://www.yaozh.com/member/'
center_request = urllib.request.Request(center_url,headers=headers)
respose = opener.open(center_request)
# byte-->utf-8
data = respose.read().decode('utf-8')

with open('03cookie.html','w',encoding='utf-8') as f:
    f.write(data)



# 一个用户 在不同的地点（IP(福建，上海，杭州，河南） 不同的浏览器 上面 不停的登录 非人为操作
# 这样就可能 封你的账号
#  N 个账号，N个ip，N个浏览器