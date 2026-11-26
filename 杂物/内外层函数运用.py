def create_counter():
    current_value = 0            # 外层函数的变量
    def counter():
        nonlocal current_value   # 声明 current_value 不是当前函数的局部变量
        current_value += 1       # 修改外层变量
        return current_value     # 返回当前计数值
    return counter               # 外层函数返回内层函数
counter1 = create_counter()
print(counter1())   # 1
print(counter1())   # 2
print(counter1())   # 3

counter2 = create_counter()
print(counter2())   # 1  —— 与 counter1 无关