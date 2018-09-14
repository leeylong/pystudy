#概括字符集
import re

#\d \D 数字与非数字
#\w \W 单词字符非单词字符
#\s \S 空 非空
s = 'python848944php89java'

r = re.findall('[a-z]{3,6}',s)#数量词控制字符数量
print(r)


#贪婪与非贪婪
r1 = re.findall('[a-z]{3,6}?',s)#范围后加?进入非贪婪模式
print(r1)

