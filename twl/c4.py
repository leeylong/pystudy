import time

# def decorator(func):
#     def wrapper():
#         print(time.time())
#         func()
#     return wrapper

# @decorator
# def f1():
#     print('this is a sencente')
# f1()


# 如何解决多参数的函数装饰？
def decorator1(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator1
def f2(a1,a2):
    print('this is a '+str(a1)+str(a2))

f2('java','php')