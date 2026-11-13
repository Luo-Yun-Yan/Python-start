n=eval(input('请输入一个整数:'))
s=0
for i in range(1,n+1):
    factorial=1
    for j in range(1,i):
        factorial=factorial*j
    s=s+factorial
print(f'阶乘{n}的和为{s}')