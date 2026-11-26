def append_num(lst):
    lst.append(4)  # 修改形参 lst（直接操作原列表）
    # 把打印移进函数内部，此时 lst 是存在的
    print(f"函数内 lst 的值：{lst}（内存地址：{id(lst)}）")

my_list = [1, 2, 3]
print(f"调用前 my_list 的值：{my_list}（内存地址：{id(my_list)}）")  # 输出原列表

append_num(my_list)  # 传递 my_list 的引用（指向列表[1, 2, 3]）
print(f"调用后 my_list 的值：{my_list}（内存地址：{id(my_list)}）")  # my_list 被修改
print()
def append_num(lst):
    lst.append(4)  # 修改形参 lst（直接操作原列表）

my_list = [1, 2, 3]
print(f"调用前 my_list 的值：{my_list}（内存地址：{id(my_list)}）")

append_num(my_list)  # 传递 my_list 的引用

# 这里会输出 [1, 2, 3, 4]，证明内部修改影响了外部
print(f"调用后 my_list 的值：{my_list}（内存地址：{id(my_list)}）")