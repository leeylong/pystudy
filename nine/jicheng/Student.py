#定义一个Student子类
from HumanClass import Human

class Student(Human):
    school = ''
    banji  = ''

    def __init__(self,school,banji,name,age):
        self.school = school
        self.banji  = banji
        super(Student, self).__init__(name,age)
    
    def do_work(self):
        print('This is a son method')
        super(Student,self).do_work()

student1 = Student('锦城中学','三年级','张三',16) 

student1.do_work()
    