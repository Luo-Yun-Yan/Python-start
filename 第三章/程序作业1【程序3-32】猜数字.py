from random import randint
goal=randint(0,100)
cnt=0
while cnt<7:
    guess=eval(input('请输入一个0~100之间的数:'))
    cnt+=1
    if guess==goal:
        print(f'恭喜，第{cnt}次猜对了!')
        break
    elif guess>goal:
        print('遗憾，猜大了。')
    elif guess<goal:
        print('遗憾，猜小了。')
else:
    print(f'不好意思，7次机会用完了，所猜数字是{goal}')
