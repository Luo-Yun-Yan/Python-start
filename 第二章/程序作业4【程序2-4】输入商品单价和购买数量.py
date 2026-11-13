price=float(input('请输入商品单价:'))
quantity=int(input('请输入购买数量:'))
total=price*quantity
if total>100:
    discount=total*0.1
else:
    discount=0
print(f'购买{quantity}件单价{price:.2f}元的商品:')
print(f'原价:{total:.2f}元')
print(f'折扣:{discount:.2f}元(满100减10%)')
print(f'实付:{total-discount:.2f}元')