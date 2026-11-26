from typing import Tuple, Union


def min_max(nums: list) -> Tuple[Union[int, float], Union[int, float]]:
    """
    接收一个数字列表，返回最小值和最大值。

    :param nums: 数字列表
    :return: 一个包含 (最小值, 最大值) 的元组
    """
    if not nums:
        raise ValueError("列表不能为空！")

    # Pythonic 写法：直接返回元组，自动打包
    return min(nums), max(nums)


# 待处理的数据
data = [3, 1, 4, 1, 5, 9]

print(f"原始列表：{data}")

# 方式一：位置参数调用 (直接把列表传进去)
result_pos = min_max(data)
print(f"位置参数调用结果: {result_pos}")

# 方式二：关键字参数调用 (显式指定参数名 nums=)
result_kw = min_max(nums=data)
print(f"关键字参数调用结果: {result_kw}")

# 演示"解包"（这是题目要求的核心考点）
# 把返回的元组直接拆分成两个独立的变量
min_val, max_val = min_max(data)
print(f"解包输出: 最小值是 {min_val}，最大值是 {max_val}，两者是否相等: {result_pos == result_kw}")