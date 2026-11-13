length,width,height=eval(input('请输入长方形的长、宽、高,以英文逗号分离:'))
c=4*(length+width+height)
s=2*length*width+2*length*height+2*width*height
v=length*width*height
print(f'周长为{c:.2f},表面积为{s:.2f},体积为{v:.2f}')