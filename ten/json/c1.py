import json

json_str = '{"name":"lee","age":18}'

stu = json.loads(json_str) #反序列化

stu1info = [
            {'name':'mark','age':56,'sex':'male'},
            {'name':'nike','age':36,'sex':'famale'},
        ]
#序列化你
stu1 = json.dumps(stu1info)

print(stu)
print(stu1)