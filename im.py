""" 
测试包的导入
"""

#import xunhuan.t.t1    简单的import导入
# print(xunhuan.t.t1.x1)

# import xunhuan.t.t1 as m1  通过别名引入，减少了路径的出现次数
# print(m1.x1)

"""from import 格式导入 """
# from xunhuan.t.t1 import x1   直接导入变量
# print(x1)

# from xunhuan.t import t1   从包下导入模块
# print(t1.x1)

# from xunhuan.t.t1 import *  此举可以导入t1模块下所有的变量，或者是被导入模块下 __all__ = ['var1','var2'....]这个变量所限定的变量
# print(x1)
# print(x2)
# print(x3)

# from xunhuan.t import *  此举可以导入t包下所有的模块，或者是被导入包下 __all__ = ['module1','module2'....]这个变量所限定的模块
# print(t1.x1)
# print(t2.a1)f

