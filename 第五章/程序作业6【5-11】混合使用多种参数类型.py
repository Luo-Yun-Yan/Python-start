def func(a, b=0, *args, c, **kwargs):
    print(f"位置参数 a: {a}")
    print(f"默认参数 b: {b}")
    print(f"可变参数 args: {args}")
    print(f"命名关键字参数 c: {c}")
    print(f"关键字参数 kwargs: {kwargs}")

# 调用函数
func(1, 2, 3, 4, c=5, d=6, e=7)