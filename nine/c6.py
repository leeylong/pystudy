class Student():
    sum = 0
    name = ''
    age = 0

    def __init__(self,name,age):
        #初始化
        self.name = name
        self.age  = age
    #定义一个类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('班级总人数'+str(cls.sum))
    
    #定义一个静态方法
    @staticmethod
    def add(x=4,y=6):
        print('a static method')

# student1 = Student('mika',89)
# Student.plus_sum()
# student2 = Student('nika',89)
# Student.plus_sum()
# student3 = Student('vlo',89)
# Student.plus_sum()
student1 = Student('mika',89)
student1.add()