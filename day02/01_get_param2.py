import urllib.request
import urllib.parse
import string

def get_params():
    url = "https://www.baidu.com/s?wd="

    params ={
        "wd":"中文",
        "key":"zhang",
        "value":"san"
    }

    str_params = urllib.parse.urlencode((params))  #这里相当于将“：”转换成等号，
    # 这个方法的作用就是将字典里面所有的键值转化为query-string格式（key=value&key=value），并且将中文转码
    print(str_params)

    fianl_url = url + str_params

#     将带有中文的url 转义成计算机可以识别的url
    end_url = urllib.parse.quote(fianl_url,safe=string.printable)
    response = urllib.request.urlopen(end_url)

    # 二进制的（mac电脑默认解码方式是utf-8)
    # (windows默认解码的方式是gbk)
    data = response.read().decode("utf-8")
    print(data)


get_params()