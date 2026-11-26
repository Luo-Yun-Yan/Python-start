import turtle
import random

# random 内置库包含生成随机数的各种函数，如 random.random() 会返回 0.0~1.0 的浮点数
turtle.setup(650, 350, 200, 200)  # 设置画布尺寸与位置
turtle.penup()                    # 抬起画笔，接下来画笔将不会在画布上留下轨迹
turtle.backward(250)              # 后退 250 像素，方向不变
turtle.pendown()                  # 放下画笔，开始绘制
turtle.pensize(25)                # 画笔的粗细设为 25 像素
turtle.seth(-40)                  # 画笔朝东南方向转 40 度

# 循环语句，画每段蟒蛇
for i in range(4):
    # 设置画笔颜色，为一个随机色
    turtle.pencolor(random.random(), random.random(), random.random())
    turtle.circle(40, 80)
    turtle.pencolor(random.random(), random.random(), random.random())
    turtle.circle(-40, 80)
turtle.pencolor(random.random(), random.random(), random.random())
turtle.circle(40, 80 / 2)
turtle.pencolor(random.random(), random.random(), random.random())
turtle.forward(40)
turtle.pencolor(random.random(), random.random(), random.random())
turtle.circle(16, 180)
turtle.pencolor(random.random(), random.random(), random.random())
turtle.forward(40 * 2 / 3)
turtle.done()