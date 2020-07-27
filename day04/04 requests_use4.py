# https://www.baidu.com/s?wd=%E5%B8%85%E5%93%A5&rsv_spt=1&rsv_iqid=0xc4329225000fe4ea&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=man&rsv_btype=t&inputT=9672&rsv_t=28e4ZToLpmyZJ5zfT71rMHAtoHcGrYhWc43FAXFIvqpo%2F5ttbgjqHo%2B4yJkdfwrWQzN5&rsv_pq=a8c14c49000a7e96&rsv_sug3=75&rsv_sug1=73&rsv_sug7=100&rsv_sug2=0&rsv_sug4=9672

import requests
# # 发送 post 和添加参数
# requests.post(url,data=(参数{})，json=(参数{}))
url = 'https://api.github.com/user'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

}
response = requests.get(url,headers=headers)

# 转化成字符
data = response.content.decode('utf-8')
print(data)
print(type(data))
print('---------------')

import json
# str--dict json.loads 可以将字符串转化为字典格式
data_dict = json.loads(data)
print(data_dict)
print(type(data_dict))
print(data_dict['message'])
print('=================')

# 注意括号 .json() 同时json 自动将其转化成字典
data1 = response.json()
print(data1)
print(type(data1))
print(data1['message'])