#正则表达式
# 一种字符串的模式
#应用：快速批量操作同类字符串
#组成  普通字符+元字符
import re

a = 'C|C++|C#|Python|Javascript|Python2'

r = re.findall('\D',a)

print(r)