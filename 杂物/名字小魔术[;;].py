name=input('请输入一个英文名字:')
x=0
for i in name:
    x+=1
if x!=0:
    print(f'名字的第一个字母{name[0]}')
    print(f'名字的第一个字母{name[-1]}')
    print(f'把名字整个倒过来{name[::-1]}')
    print(f'名字里一共有{x}个字母')
    print(f'名字里一共有{len(name)}个字母')
else:
    print('英文名字不能为空!')
