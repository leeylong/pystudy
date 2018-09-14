#设置成员的可见性
# 命名前面双下划线表示成员的私有属性
class Student():
    name = ''
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age  = age

        self.__score = 0
    
    #设置score
    def __marking(self,score):
        self.__score = score

        print(self.name + '同学的成绩是：'+str(self.__score))
    # def __

student1 = Student('张三',18)
student1.__score = -55
print(student1.__dict__)