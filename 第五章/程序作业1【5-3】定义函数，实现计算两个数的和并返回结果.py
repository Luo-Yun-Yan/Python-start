def calculate_sum(num1, num2):
    """
    计算两个数的和，并返回结果
    参数：
    num1 (float/int)：第一个加数
    num2 (float/int)：第二个加数
    返回：
    float/int：两个数的和
    """
    total = num1 + num2  # 计算和
    return total         # 返回结果

# 调用有参函数，输入整数
sum1 = calculate_sum(3, 5)
print(sum1)

# 调用有参函数，输入浮点数
sum2 = calculate_sum(2.5, 4.7)
print(sum2)

print(f"输出函数说明文档: \n{calculate_sum.__doc__}")