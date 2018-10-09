from functools import reduce

list_x = [1,2,3,4,5,6,7,8]
ret = reduce(lambda x,y:x+y,list_x)

print(ret)