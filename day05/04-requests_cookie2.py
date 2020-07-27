import requests

url = 'https://www.yaozh.com/member/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


# 1. 代码登录
login_url = 'https://www.yaozh.com/login'
login_form_data ={
    "username":"18798726635",
    "pwd":"jxy120110",
    "formhash":"1D147B3F75",
    "backurl":"https%3A%2F%2Fwww.yaozh.com%2F",
}

# session 类 可以自动保存cookies  相当于 cookiejar
session = requests.session()

login_response = session.post(login_url,headers = headers,data = login_form_data)

# 2. 登录成功之后，带着有效的cookie 去访问 请求目标数据
response = session.get(url,headers=headers)  #session 自动保存了cookie
data = response.content.decode('utf-8')

with open('04-cookie.html','w',encoding='utf-8')as f:
    f.write(data)