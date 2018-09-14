#边界匹配

import re

qq = '543543661'
#判断是不是4-8位的数字

r = re.findall('^\d{4,8}$',qq)  #^ &分别表示开头和结尾

print(r)