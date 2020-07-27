"""
正则表达式
"""
import re

one = 'm12d3737nddllkdkkn'

# 1
pattern = re.compile('m(.)n')  #这种默认的是m和n之间只有一个字符 如 msn  result='s'
result = pattern.findall(one)
print(result)

# 贪婪模式 从开头匹配到结尾 默认 *代表彼此多次，'.'代表匹配任意字符
pattern = re.compile('m(.*)n')
result = pattern.findall(one)
print(result)

# 非贪婪 '?' 匹配前面子表达式0次或1次  ‘+’代表至少一次
pattern = re.compile('m(.*?)n')
result = pattern.findall(one)
print(result)

