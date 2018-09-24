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