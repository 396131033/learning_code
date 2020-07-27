"""
     https://www.yaozh.com/
    用户名：hello666  18798726635
    pwd :jxy120110

    直接获取登录后的会员中心界面
    手动粘贴复制，PC 抓包后的cookie
    放在request对象的请求头里面

"""
import urllib.request

url = 'https://www.yaozh.com/member/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie':'acw_tc=707c9f9415955614557305295e56d9bd642d7009c00563c3409373a8c25b2b; PHPSESSID=fb7qu2pu6vh1moiuemd3vqo710; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1595561383; _ga=GA1.2.785450063.1595561383; _gid=GA1.2.1241469696.1595561383; yaozh_userId=958830; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1595561499; yaozh_uidhas=1; yaozh_mylogin=1595561577; acw_tc=707c9f9415955614557305295e56d9bd642d7009c00563c3409373a8c25b2b; UtzD_f52b_saltkey=tj3dm4ty; UtzD_f52b_lastvisit=1595558115; _ga=GA1.1.673055285.1595561644; _gid=GA1.1.693917819.1595561644; yaozh_logintime=1595561741; yaozh_user=958830%09hello6666; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaabJ1tmJSHnKZxanJT1qeSoMZYoNdzcJtamsjRztCampdth3DYnp6bVaOWq6XArZqgxlig13NokXJUlJq4f37c5dBA3bfC3F0bA643D6931c01335blpmakmycZoef2JtncVesms6eU27UcJaXc1mSbWuYmpiSm5iTbZpnh5%2Fi335c6a6b7cf6146ceac73e344e564e95; db_w_auth=801686%09hello6666; UtzD_f52b_lastact=1595561742%09uc.php%09; UtzD_f52b_auth=8b9cKG52lypaZzr%2FTubYx5MDDopU6zpxE5MEOXSlIPpmZE%2FMZLhCROoZ2XZA9VoF4UVvyeKtwVUFAO5B948VXBbW8qA'

}

request = urllib.request.Request(url,headers = headers)

response = urllib.request.urlopen(request)

data = response.read().decode('utf-8')

with open('02-2cookie.html','w',encoding='utf-8') as f:
    f.write(data)