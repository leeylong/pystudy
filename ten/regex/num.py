#替换字符串中的数字，并根据范围进行不同替换
import re

str = 'fdasf435t4rtfwaaser34534w35r'

def convert(val):
    num = int(val.group()) #val.group()类型是字符串
    if(num >= 5):
        return '9'
    else:
        return '0'

r = re.sub('\d',convert,str)
print(r)