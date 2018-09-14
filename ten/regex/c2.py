#正则表达式
# 一种字符串的模式
#应用：快速批量操作同类字符串
#组成  普通字符+元字符
import re

s = 'abc, acc, adc, aec, afc, agc,ahc'

# r = re.findall('a[cf]c',s)#表示中间字母是c或f的

r = re.findall('a[^cf]c',s)#表示中间字母不是c或f的

r = re.findall('a[c-f]c',s)#表示中间字母是c到f的

print(r)