import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(5)

colors = ['blue', 'black', 'red', 'yellow', 'green']
positions = [(-110, 0), (0, 0), (110, 0), (-55, -55), (55, -55)]

# 使用 zip 函数同步遍历颜色和坐标
for color, (x, y) in zip(colors, positions):
    t.penup()
    t.goto(x, y - 50)
    t.pendown()
    t.color(color)
    t.circle(50)

turtle.done()