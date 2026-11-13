score=eval(input('请输入百分制成绩(将会转换为等级制):'))
if score>100 or score<0:
    print('输入数据无效')
elif score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')