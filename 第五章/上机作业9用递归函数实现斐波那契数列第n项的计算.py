def fibonacci(n):
    # 终止条件：如果是第1项或第2项，直接返回 1
    if n == 1 or n == 2:
        return 1
    # 递归规则：第 n 项 = 第 n-1 项 + 第 n-2 项
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 按照题目要求，验证 n=10 的结果
result = fibonacci(10)
print(f"当 n=10 时，斐波那契数列的结果为: {result}")