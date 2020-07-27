# https://www.baidu.com/s?wd=%E5%B8%85%E5%93%A5&rsv_spt=1&rsv_iqid=0xc4329225000fe4ea&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=man&rsv_btype=t&inputT=9672&rsv_t=28e4ZToLpmyZJ5zfT71rMHAtoHcGrYhWc43FAXFIvqpo%2F5ttbgjqHo%2B4yJkdfwrWQzN5&rsv_pq=a8c14c49000a7e96&rsv_sug3=75&rsv_sug1=73&rsv_sug7=100&rsv_sug2=0&rsv_sug4=9672

import requests
# 参数会自动 转码，转译（帅哥）
url = 'https://www.baidu.com/s?'
# 传参  也不需要转码，转译
params = {
    'wd':'帅哥'
}
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

}
response = requests.get(url,headers=headers,params=params)  #将字典自动转码
data = response.content.decode('utf-8')

with open('04-3requests.html','w',encoding='utf-8') as f:
    f.write(data)


# 发送 post 和添加参数
requests.post(url,data=(参数{})，json=(参数{}))