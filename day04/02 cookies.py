"""
    直接获取 登录后的页面
    手动粘贴 复制 PC 抓包的 cookies
    放在 request对象的请求头里面

    https://www.yaozh.com/
    用户名：hello666  18798726635
    pwd :jxy120110
"""
import urllib.request
# 1 数据url
url = 'https://www.zhihu.com/'

# 2 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie':'_zap=a7ab9263-2663-4433-bb3e-eeee1d0416f6; d_c0="ACBdHOavIBGPTooRqIgXA57YWOBFDJAoXr8=|1587031370"; _ga=GA1.2.671036469.1587031327; _xsrf=4b9c161b-ec54-4dfc-97eb-feef11a3c3f8; _gid=GA1.2.1652059331.1593861104; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1592296096,1592650182,1592825011,1593861106; SESSIONID=ghXgMkjGQGRKquPEgMeZW4sCxGcBpNiSuEauO8WE7Pi; JOID=VVwdAExmWB4FBDmlGmLrytCGSCAEAjxNZklRw1Y3HEBFcUz2U1I7EV4HNqIVbKzfg5lHWp5samHHxeLjzUpDQ-8=; osd=UVwUC09iWBcOBz2lE2noztCPQyMAAjVGZU1Ryl00GEBMek_yU1swEloHP6kWaKzWiJpDWpdnaWXHzOngyUpKSOw=; capsion_ticket="2|1:0|10:1593861197|14:capsion_ticket|44:YTJkZmNjZThiNDBlNGZkNmI4ODEwZjlhNWZmMTA0NDM=|47534b3bdf81533c7d8e503c88e395e883d2773190f2d76e730f401ff9417095"; z_c0="2|1:0|10:1593861224|4:z_c0|92:Mi4xMmM2eEd3QUFBQUFBSUYwYzVxOGdFU1lBQUFCZ0FsVk5hTEx0WHdCX1VCRVpwNW4zZUxUVlBIdWV3R1p2d25tLVZR|db9fc5221a73fb1c1c462f8d1a16c181342b45b0fbaa2decd04da1332147524e"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1593861158; KLBRSID=b33d76655747159914ef8c32323d16fd|1593861228|1593861170'
}

# 3 创建请求对象
request = urllib.request.Request(url,headers=headers)

# 4 发送请求
response = urllib.request.urlopen(request)

# 5 read datas
data = response.read().decode('utf-8')

# 6 save datas  注意保存的时候要转码
with open('02cookie.html','w',encoding='utf-8') as f:
    f.write(data)

