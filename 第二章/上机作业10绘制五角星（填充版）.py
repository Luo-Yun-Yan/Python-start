import turtle
import math

t = turtle.Turtle()
t.speed(1)

# 1. 先偷偷画一个半径合适的实心金色圆盘垫在下面
# 为什么是 58？因为 150 * sin(18°) 刚好约等于 46，稍微大一点（58）刚好能完美填满中间的缝隙
t.penup()
t.goto(0, -58)  # 移动到圆的底部
t.pendown()
t.color('gold', 'gold')
t.begin_fill()
t.circle(58)
t.end_fill()

# 2. 开始画你的五角星
t.begin_fill()
for i in range(5):
    angle = math.radians(i * 144 + 90)#角度转弧度
    x = 150 * math.cos(angle)
    y = 150 * math.sin(angle)

    if i == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

# 回到起点闭合图形
t.goto(150 * math.cos(math.radians(90)), 150 * math.sin(math.radians(90)))
t.end_fill()

t.hideturtle()
turtle.done()