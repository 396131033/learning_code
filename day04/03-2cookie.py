import urllib.request

# 自动获取cookie
login_url = 'https://www.yaozh.com/login'
login_form_data = {
    'username':'18798726635',
    'pwd':'jxy120110',
    'formhash':'E39BAC2B38',
    'backurl':'"https%3A%2F%2Fwww.yaozh.com%2F"'
}
from urllib import parse
login_str =parse.urlencode(login_form_data).encode('utf-8')

# ==============================
from http import cookiejar
# cookiejar 实例化  注意这里C和J都是大写
cook = cookiejar.CookieJar()
# cookie处理器
cook_handler = urllib.request.HTTPCookieProcessor(cook)
# 创建opener
opener = urllib.request.build_opener(cook_handler)
# ==============================
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
# 创建请求
login_request = urllib.request.Request(login_url,headers = headers,data = login_str)
# 发送请求  不用管获取什么内容，cookiejar会自动获取并保存cookie
opener.open(login_request)

# 2. 自动获取cookie后可以模拟用户登录
center_url = 'https://www.yaozh.com/member/'
center_request = urllib.request.Request(center_url)
response = opener.open(center_request)
data = response.read().decode('utf-8')

with open('03-2cookie.html','w',encoding='utf-8') as f:
    f.write(data)
