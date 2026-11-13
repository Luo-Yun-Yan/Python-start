discount=eval(input('请输入路程，单位为km:'))
if discount>=36:
    cost=7
elif discount>=25:
    cost=6
elif discount>=16:
    cost=5
elif discount>=9:
    cost=4
elif discount>=4:
    cost=3
else:
    cost=2
print(f'票价为{cost}元')