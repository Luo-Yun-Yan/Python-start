names=['张三','李四','王五']
scores=[90,85,100]
# result=zip(names,scores)
# print(list(result))

# for name,score in zip(names,scores):
#     print(f'{name}考了{score}分')

matrix=[
    [1,2,3],
    [4,5,6]
]
transposed=list(zip(*matrix))
print(transposed) 