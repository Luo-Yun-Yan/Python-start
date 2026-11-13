ls=['Python','C++','C','Java','SQL','Rust','C++']
print('ls的初始值:',ls)
del ls[3]
print('删除3号元素后的ls:',ls)
ls.remove('C++')
print('删除列表中第一次出现的C++:',ls)
str=ls.pop(1)
print('取出的1号元素:',str)
print('取出元素后的ls:',ls)
ls.clear()
print('清空后的ls:',ls)