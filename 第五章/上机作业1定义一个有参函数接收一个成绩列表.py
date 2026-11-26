from typing import List


def calculate_average(scores: List[float]) -> float:
    """
    计算成绩列表的平均分。

    :param scores: 包含成绩的列表
    :return: 平均分（保留两位小数），若列表为空则返回 0.0
    """
    if not scores:  # 防御性编程：处理空列表
        return 0.0

    # 计算平均值
    avg = sum(scores) / len(scores)
    return round(avg, 2)


# 调用该函数计算成绩
scores_list = [85, 90, 78, 92]
average_result = calculate_average(scores_list)

# 输出结果
print(f"成绩列表：{scores_list}")
print(f"该成绩的平均分为：{average_result:.2f}")