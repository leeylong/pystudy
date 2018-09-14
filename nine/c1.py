""" 类的学习 """
#类、对象   各自的意义，关系

#定义一个对象
#类名首字母大写
#驼峰法命名
#可传参数
class Student():
#可以定义变量
    name = ''
    sex = ''
    age = 0  
#类变量：和类关联
# 示例变量：和对象关联
    def __init__(self,name,sex,age):
        #构造函数
        self.name = name
        self.age  = age
        self.sex  = sex
# 可以定义函数
    def print_file(self):
        # print('我是类下的print_file函数')
        print('name:'+self.name)
        print('sex:'+self.sex)
        print('age:'+str(self.age))


#1、类下不能出现空形参？必须指定一个参数？  什么shiself参数？
#2、类下定义的方法必须加一个self关键字