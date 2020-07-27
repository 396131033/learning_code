import urllib.request

def auth_nei_wang():
    # 1.用户密码(内网（nei_wang)
    user = 'admin'
    pwd = '123456'
    nei_url = 'http://192.168.179.66'

    # 2. 创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwd_manager.add_password(None,nei_url,user,pwd)

    # 3.利用密码管理器创建可以验证的ip代理处理器(平时常用requests)
    auth_hander = urllib.request.HTTPBasicAuthHandler(pwd_manager)

    opener = urllib.request.build_opener(auth_hander)
    response = opener.open(nei_url)
    print(response)

auth_nei_wang()