n=input('请输入一个正整数:')
total=0
for i in range(1,int(n)+1):
    total+=i
average=total/int(n)
print(f'总和为:{total}')
print(f'平均值为:{average:.1f}')