s={'Python','C++','C'}
s.add('Java')
print('add()添加一个元素后:',s)
s.update({1,3},[2,4],(2,5),'cube')
print('update()添加元素后:',s)
t=s.copy()
print('复制集合s:',t)

