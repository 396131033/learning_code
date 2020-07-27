import requests

url = 'http://www.baidu.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

}

# 免费代理
free_proxy = {
              'http':'120.77.249.46:8080'}   #这个ip可能失效  百度爬取免费ip代码
respose = requests.get(url,headers = headers,proxies=free_proxy)

print(respose.status_code)