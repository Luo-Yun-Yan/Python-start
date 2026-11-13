s={'Python','Java','C++','C','computer','123'}
t=s.pop
print('弹出的元素是:',t)
print('弹出元素后,集合是:',s)
s.discard('123')
print('移出元素后,集合是:',s)
s.clear()
print('清除集合后:',s)
