import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor('white')
width, height = screen.window_width(), screen.window_height()

colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'cyan', 'magenta']

for _ in range(20):
    r = random.randint(10, 40)

    # 计算安全边界，确保圆不出界
    max_x = (width / 2) - r - 20
    max_y = (height / 2) - r - 20

    x = random.randint(-int(max_x), int(max_x))
    y = random.randint(-int(max_y), int(max_y))

    color = random.choice(colors)

    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

turtle.done()