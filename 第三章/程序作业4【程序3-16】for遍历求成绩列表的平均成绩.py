grades=[80,92,64,70,88]
total=0
for grade in grades:
    total+=grade
average=total/len(grades)
print(f'平均成绩:{average:.1f}')