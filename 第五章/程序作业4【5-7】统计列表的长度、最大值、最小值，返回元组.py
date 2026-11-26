def list_stats(lst):
    """统计列表的长度、最大值、最小值，返回元组(长度, 最大值, 最小值)"""
    if not lst:
        return (0, None, None)  # 处理空列表

    length = len(lst)
    max_val = max(lst)
    min_val = min(lst)

    # 多值返回（自动打包为元组）
    return (length, max_val, min_val)


# 调用函数并解包返回值
stats = list_stats([5, 2, 9, 1, 7])

# 解包元组到变量
length, max_val, min_val = stats

print(f"长度: {length}, 最大值: {max_val}, 最小值: {min_val}")