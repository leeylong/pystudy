"""  """
from c1 import Student


#实例化
student = Student('tony','男',18)
print(student.print_file())
#由此可见__init__方法在实例化对象执行时可以自动调用构造函数，并且可以被显示调用