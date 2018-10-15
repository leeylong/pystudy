from enum import Enum

class Vip(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN  = 2
    BLACK  = 3
    RED    = 4

# print(type(Vip.YELLOW)) #枚举的类型
# print(type(Vip.YELLOW.name)) #枚举的名字
# print(Vip.YELLOW.value) #枚举的值

# print(Vip['GREEN']) #枚举的值
# for v in Vip.__members__.items(): #枚举类可以循环成员出来
#     print(v)

result = Vip.YELLOW is Vip.YELLOW
result1 = Vip.YELLOW == Vip.YELLOW
print(result)
print(result1)
#闭包概念

def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve

b = curve_pre()
a = 1000
ret = b(4)
print(type(b))
print(ret)

