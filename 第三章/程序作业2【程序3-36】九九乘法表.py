#for循环
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={j*i:<3}',end='')
    print()
print()
#while循环
i=1
while i<=9:
    j=1
    while j<=i:
        print(f'{i}*{j}={i*j:<3}',end='')
        j+=1
    print()
    i+=1


