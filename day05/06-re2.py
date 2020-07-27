"""
正则表达式
"""
import re

one = """
    mdkdldkdjfdiln
    12345678910111n
"""

# 贪婪模式 从开头匹配到结尾 默认 *代表彼此多次，'.'代表匹配任意字符
# '.' 除了换行符 '\n' 之外的 匹配  所以数字并不能输出。
pattern = re.compile('m(.*)n')
result = pattern.findall(one)
print(result)

