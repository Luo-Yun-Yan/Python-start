print("\n--- 基础练习 ---")
#基础练习
#简洁版
def make_multiplier(factor):
    def multiply(num):
        return num * factor
    return multiply
fn = make_multiplier(3)
print(fn(5))
print()
#高级版
# 题目要求：make_multiplier(3) 里的数字乘以 factor 等于 15
# 这其实就是一个最简单的闭包实现

def make_multiplier(factor):
    def multiply(num):
        return num * factor

    return multiply

# 创建一个“乘以3”的专属工具
multiply_by_3 = make_multiplier(3)
# 传入 5，计算结果
result = multiply_by_3(5)
print(f"5 乘以 factor(3) 的结果是: {result}")

print()
print("\n--- 进阶练习 ---")
def create_cart():
    # 准备一个购物车，记录总价（初始为0）
    total_price = 0

    # 定义内部函数，负责添加商品
    def add_item(item, price):
        # nonlocal 关键字：告诉 Python 这个 total_price 是外面函数的，我要修改它
        nonlocal total_price
        total_price += price
        print(f"已添加: {item}, 价格: {price}元, 当前总价: {total_price}元")

    # 把内部函数当做“物品”返回出去
    return add_item

# ===== 测试代码（按照题目要求） =====
print("--- 测试闭包 ---")
# 1. 创建一个专属购物车（执行 create_cart 函数）
my_cart = create_cart()

# 2. 开始测试：随意调用几次 add_item 添加商品
my_cart("苹果", 10)
my_cart("香蕉", 20)
my_cart("西瓜", 25)

