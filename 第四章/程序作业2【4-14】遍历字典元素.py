prov = {"省份": "云南", "省会": "昆明", "面积（万km²）": 39.41, "人口（万）": 4655}

print("仅遍历字典的键：")
for key in prov.keys():
    print(key)

print("仅遍历字典的值：")
for value in prov.values():
    print(value)

print("遍历字典的键值对：")
for key, value in prov.items():
    print(f"{key}: {value}")