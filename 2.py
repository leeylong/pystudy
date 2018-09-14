""" 
    a tiny code
 """
ACCOUNT = 'lee'
password = '123456'

print('please input account')
user_account = input()
print('please input password')
user_password = input()

if user_account == ACCOUNT and user_password == password:
    print('Success')
else:
    print("failed")