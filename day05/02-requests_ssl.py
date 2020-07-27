import requests

url = 'https://www.12306.cn/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

}

# 因为https 是有第三方 CA证书认证的
# 但是 12606 虽然是https 但是 它不是CA证书，他是自己 颁发的证书
# 解决办法 是：告诉web 忽略证书 访问  使verify=False 默认是true
response = requests.get(url,headers=headers,verify=False)
data = response.content.decode('utf-8')

with open('02-ssl.html','w',encoding='utf-8') as f:
    f.write(data)
