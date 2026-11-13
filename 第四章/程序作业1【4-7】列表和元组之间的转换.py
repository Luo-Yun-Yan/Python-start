scores=[85,92,78,90,65,88,72,95,81,87]
total=0
count=0
for score in scores:
    total+=score
    count+=1
ave=total/count
exls=[]
for score in scores:
    if score>ave*1.1:
        exls.append(score)
extp=tuple(exls)
print('原始分数',scores)
print('平均分:',ave)
print('高出平均分10%的分数:',extp)