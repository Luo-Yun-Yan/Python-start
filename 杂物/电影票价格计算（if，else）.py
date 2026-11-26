age=int(input('请输入您的年龄:'))
vip=input('是否输入您的会员(y表示是，n表示否):')
if age<6:
    price=0
    print('年龄小于6岁，免票')
elif age<=17:
    price=25
    print('初始票价需要25元')
elif age<60:
    price=50
    print('初始票价需要50元')
else:
    price=30
    print('参数票价需要30元')
if vip.lower()=='y'and price>0:
    price=price-5
print(f'您的最终应付金额为:{price}元')