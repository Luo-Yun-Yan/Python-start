import math
x1,y1=map(float,input('请输入第一个点的坐标(x,y),用英文逗号隔开且全部使用英文符号:').split(','))
x2,y2=map(float,input('请输入第二个点的坐标(x,y),用英文逗号隔开且全部使用英文符号:').split(','))
x_square=(x1-x2)**2
y_square=(y1-y2)**2
distance=math.sqrt(x_square+y_square)
print(f'两点之间的距离是{distance:.2f}')
