#密码为:python123
i=0
while i<3:
    password=input('请输入你的密码:')
    i+=1
    if password=='python123':
        break
else:
    print('不好意思，3次机会用完了')
