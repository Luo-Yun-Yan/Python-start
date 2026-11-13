import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 画黄色的脸
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# 画眼睛 (黑色实心圆)
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

draw_eye(-35, 30)
draw_eye(35, 30)

# 画嘴巴 (半圆弧)
t.penup()
t.goto(-40, 0)
t.pendown()
t.pensize(3)
t.setheading(-60) # 调整海龟朝向，画出微笑弧度
t.circle(50, 120) # 画半径为50的圆弧，跨度120度

turtle.done()