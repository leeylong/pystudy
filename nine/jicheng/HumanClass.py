#定义一个Human父类，对人类共有属性去重
class Human():
    name = ''
    age  = 0

    def __init__(self,name,age):
        self.name = name
        self.age  = age
    
    def do_work(self):
        print('This is a parrent method')