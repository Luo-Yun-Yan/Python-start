import turtle
import math

t = turtle.Turtle()
t.speed(0)

# 设置填充颜色
t.color('gold', 'gold')
t.begin_fill()

# 每次步进 2 个顶点（即隔一个点连），这样就能自动画出五角星的穿插效果。
for i in range(5):
    # i * 144 是因为五角星每次跨越的圆心角是 144 度 (即 360/5 * 2)
    angle = math.radians(i * 144 + 90)
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