num1,num2=map(int,input('请输入两个整数(用空格隔开):').split())
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
if num2!=0:
    print(f'{num1}/{num2}={num1/num2:.2f}')
else:
    print('除数不能为0,无法计算商')