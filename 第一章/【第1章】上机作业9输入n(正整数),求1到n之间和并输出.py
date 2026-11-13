n=int(input('请输入一个正整数:'))
sum=0
for i in range(n+1):
    sum+=i
print('前{}个正整数之和:{}'.format(n,sum))