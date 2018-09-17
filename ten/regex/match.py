#mach特性
import re

str = '4gFefe934rt'

r = re.match('\d',str)
r1 = re.search('\d',str)

print(r)
print(r1)