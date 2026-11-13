#1
dic = {"云南": "昆明", "四川": "成都", "陕西": "西安"}
print(dic)
print()
#2
dic1 = dict(云南="昆明", 四川="成都", 陕西="西安")
print(dic1)

dic2 = dict([("湖南", "长沙"), ("江苏", "南京"), ("山东", "济南")])
print(dic2)
#3
dic3 = {i: i * i for i in range(1, 4)}
print(dic3)