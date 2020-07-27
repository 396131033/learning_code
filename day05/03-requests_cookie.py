import requests

url = 'https://www.yaozh.com/member/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# cookie 的字符串
# cookie = 'PHPSESSID=hd1npfq9t4m83euv2chh879k17; _ga=GA1.2.1151652258.1595580730; UtzD_f52b_saltkey=Nxm3n13l; UtzD_f52b_lastvisit=1595577220; acw_tc=2f624a4315957688360898456e641a6e2649512a7797784fb729cf85563a38; _gid=GA1.2.1475209724.1595768762; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1595768765; yaozh_logintime=1595768943; yaozh_user=958830%09hello6666; yaozh_userId=958830; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaabJ1tmJSHnKZxanJT1qeSoMZYoNdzcJtamsjRztCampdth3DYnp6bVaOWq6XArZqgxlig13NokXJUlJq53CEd138Bd147951285379Df4cf24D23blpmckW6daYef2JtncVesms6eU27UcJaXc1mSbWuYnJiZnZiVbJxnh5%2Fif83995555b69ead48c4d897f91502c65; db_w_auth=801686%09hello6666; UtzD_f52b_lastact=1595768944%09uc.php%09; UtzD_f52b_auth=2432YjhGOJ%2BqmDzjji2DVYN0opAUsSCW9yB1f3vwcvZ9HC6lSicB2a6YPXxVuFrx1SZUF4lilXSnoGcglkTcKay6pEs; yaozh_uidhas=1; yaozh_mylogin=1595768946; acw_tc=2f624a4315957688360898456e641a6e2649512a7797784fb729cf85563a38; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1595562171%2C1595575968%2C1595580730%2C1595768762'
cookie = 'PHPSESSID=hd1npfq9t4m83euv2chh879k17; _ga=GA1.2.1151652258.1595580730; UtzD_f52b_saltkey=Nxm3n13l; UtzD_f52b_lastvisit=1595577220; _gid=GA1.2.1475209724.1595768762; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1595768765; yaozh_userId=958830; yaozh_uidhas=1; yaozh_mylogin=1595768946; acw_tc=2f624a4315957688360898456e641a6e2649512a7797784fb729cf85563a38; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1595562171%2C1595575968%2C1595580730%2C1595768762; UtzD_f52b_ulastactivity=1595561571%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D801686; UtzD_f52b_creditbase=0D0D2D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; _ga=GA1.1.2067154072.1595770560; _gid=GA1.1.527354405.1595770560; yaozh_logintime=1595770773; yaozh_user=958830%09hello6666; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaabJ1tmJSHnKZxanJT1qeSoMZYoNdzcJtamsjRztCampdth3DYnp6bVaOWq6XArZqgxlig13NokXJUlJq98EF3b2CE3724dC16504D63C0327369DblpuamXCZaIef2JtncVesms6eU27UcJaXc1mSbWuYnJmRm5uVapZph5%2Fib0b25878d842a2bc06a41f0fcb480d47; db_w_auth=801686%09hello6666; UtzD_f52b_lastact=1595770774%09uc.php%09; UtzD_f52b_auth=5544ku%2B6w48gHWXMwETbF4BqJXNDQST7EH8AqgQAIveMrVqUaQk9UkWHOJotsUBCFofvswDRJw%2F2x17Y38U31lj1yO8; _gat=1'

cookie_list = cookie.split('; ')  #以冒号和空格拆分  "； "

# 需要 字典
cookie_dict = {}
for cook in cookie_list:
    # =====================错误 bug====================
    # # cookie_dict = {cook.split('=')[0]:cook.split('=')[1]}
    # # # 这样不行，这样dict只剩最后一次的拆分结果，前面的都会被覆盖，所以这样行不通，除非为字典推导形式，即内部循环
    # # cookie_dict = {cook.split('=')[0]:cook.split("=")[1]}
    # =================================================

    # cookie_dict[cook.split('=')[0]]=cook.split('=')[1]


# 字典推导
cookie_dict = {cook.split('=')[0]:cook.split("=")[1] for cook in cookie_list}

# 注意这里的cookies参数是复数，要加's'
response = requests.get(url,headers=headers,cookies=cookie_dict)  #这里的cookie只接受字典型或cookiejar

data = response.content.decode('utf-8')

with open('03-cookie.html','w',encoding='utf-8')as f:
    f.write(data)