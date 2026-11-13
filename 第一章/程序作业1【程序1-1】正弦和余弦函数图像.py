import numpy as np
import matplotlib.pyplot as plt
def draw(x,y1,y2):
    plt.plot(x,y1,label='sin')
    plt.plot(x,y2,label='cos',linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('sin&cos')
    plt.legend()
value=int(input('请输入一个正整数:'))
print(value)
while(value<=0):
    print('输入错误！！！')
    value = int(input('请输入一个正整数:'))
x=np.arange(0,value,0.1)
y1=np.sin(x)
y2=np.cos(x)
draw(x,y1,y2)
plt.show()
