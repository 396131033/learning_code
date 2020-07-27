# 1 记得安装 第三方 模块 requests
# pip install requests

import requests
url = 'http://www.baidu.com'
response = requests.get(url)
print(response)

# content属性 返回的类型 是bytes
data = response.content
print(data)
print(type(data))

print('============')
# 转码，转译，将字节数据转化成字符型
data1 = response.content.decode('utf-8')
print(data)
print(type(data1))

print('****************')

# text 属性 返回的类型 是文本str
data_text = response.text
print(data_text)
print(type(data_text))

