from math import sqrt
a,b,c=map(float,input('请输入系数a,b,c:(用英文逗号分隔):').split(','))
delta=b**2-4*a*c
if delta>0:
    root1=(-b+sqrt(delta))/(2*a)
    root2=(-b-sqrt(delta))/(2*a)
    print(f'方程有两个不相等的实根{root1}和{root2}')
elif delta==0:
    root=(-b+sqrt(delta))/(2*a)
    print(f'方程有两个相等的实根{root}')
else:
    real_part=-b/(2*a)
    imag_part=sqrt(-delta)/(2*a)
    print(f'方程有两个共轭复根:({real_part}+{imag_part}i)和({real_part}-{imag_part}i)')