num=(input('请输入一个三位的整数'))
if int(num)==int(num[0])**3+int(num[1])**3+int(num[2])**3:
    print(f'{num}是水仙花数')
else:
    print(f'{num}不是水仙花数')