# 函数定义
def rectangle_area(length, width):
    """
    计算矩形的面积
    参数：
    length (float)：矩形的长
    width (float)：矩形的宽
    返回：
    float：矩形的面积（长 × 宽）
    """
    area = length * width
    return area

# 调用函数
a = rectangle_area(5.0, 3.0)
print("矩形的面积是：", a)