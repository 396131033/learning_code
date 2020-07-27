import urllib.request

# 1 数据url
url = 'https://www.zhihu.com/'
# 2 添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# 3 构建请求对象
request = urllib.request.Request(url,headers=headers)

# 4 发送请求
response = urllib.request.urlopen(request)

# 5 读取数据、数据解码
data = response.read().decode('utf-8')
print(data)

# 6 保存数据
with open('01cook.html','w',encoding = 'utf-8') as f:
    f.write(data)
