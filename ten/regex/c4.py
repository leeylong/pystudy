""" 
* 匹配0次或多次
+ 匹配1次或多次
? 匹配0次或1次
 """
import re

s = 'pythow3r55435python34543pythonnn323'
r1 = re.findall('python*',s)
r2 = re.findall('python+',s)
r3 = re.findall('python?',s)

print(r1)
print(r2)
print(r3)

