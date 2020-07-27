import urllib.request
#用于汉字转义
import urllib.parse
import string

def get_method_params():
    url = "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word="
    # 拼接字符串（汉字）
    # python可以接受的数据
    # https: // image.baidu.com / search / detail?ct = 503316480 & z = 0 & ipn = false & word = 美女
    # https: // image.baidu.com / search / detail?ct = 503316480 & z = 0 & ipn = false & word = % E7 % BE % 8
    # E % E5 % A5 % B3
    name = "美女"
    final_url = url+name
    print(final_url)
    # 代码发送了请求
    # 网址里面包含了汉字，ascii是没有汉字的；url转义
#     使用代码发送网络请求
#     将帮韩汉字的网址进行转义
    encode_new_url = urllib.parse.quote(final_url,safe=string.printable)
    print(encode_new_url)

    response = urllib.request.urlopen(encode_new_url)
    print(response)
    # UnicodeEncodeError: 'ascii'
    # codec can't encode characters in position 51-52: ordinal not in range(128)
#      python：是解释性语言；解析器只支持 ascii 0-127
#       即：不支持中文
    data = response.read().decode()  #解码
    print(data)

    with open ("02-encode.html","w",encoding="utf-8") as f:
        f.write(data)


get_method_params()
