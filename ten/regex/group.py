import re
s = 'life is short,i use python,i love python'

r = re.match('life(.*)python(.*)python',s)
r1 = re.search('life(.*)python(.*)python',s)

print(r.groups())
print(r1.groups())