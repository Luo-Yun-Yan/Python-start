def factorial(n):
    # 终止条件：n=0 时直接返回 1
    if n == 0:
        return 1
    else:
        # 递归：n! = n * (n-1)!，调用自身计算(n-1)!
        return n * factorial(n - 1)

# 测试：计算 5 的阶乘
print(f"5!={factorial(5)}")  # 输出: 120 (5! = 5*4*3*2*1*1 = 120)