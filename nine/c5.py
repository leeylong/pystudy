class Student():
    name = ''
    sex = ''
    age = 0  
    total = 58
    def __init__(self,name,sex,age):
        #构造函数
        self.name = name*2
        self.sex  = sex*2
        self.age  = age*2

        
        #测试
        print(name)
        print(sex)
        print(age)
        self.total += 1
        print(Student.total)

# 可以定义函数
    def intro(self):
        print('name:'+self.name)
        print('sex:'+self.sex)
        print('age:'+str(self.age))

student1 = Student('mark','male',23)
student1.intro()