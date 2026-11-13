tiangan=['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
dizhi=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
jiazi=[]
tg=0
dz=0
while tg<len(tiangan)or dz<len(dizhi):
    if tg==len(tiangan):
        tg=0
    if dz==len(dizhi):
        dz=0
    jiazi.append(tiangan[tg]+dizhi[dz])
    tg+=1
    dz+=1
for i in range (len(jiazi)):
    print(f'{i+1:2d}.{jiazi[i]}',end='')
    if (i+1)%6==0:
        print()