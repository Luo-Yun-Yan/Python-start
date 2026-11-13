import turtle

def draw_triangle(t, size, fill_color):
    """画一个等边三角形（做房顶和树）"""
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_square(t, size, fill_color):
    """画一个正方形（做房子主体）"""
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# 初始化画布
screen = turtle.Screen()
screen.title("图2-10 样例")
t = turtle.Turtle()
t.speed(0) # 极速绘制

# 绘制房子
t.penup()
t.goto(-50, -100)
t.pendown()
draw_square(t, 100, "white")     # 房子主体

t.penup()
t.goto(-50, 0)
t.pendown()
draw_triangle(t, 100, "black")   # 房子屋顶

t.penup()
t.goto(-15, -50)
t.pendown()
draw_square(t, 30, "black")      # 门

# 画树（复杂点用函数封装一下，这里简单画个树干和树冠）
t.penup()
t.goto(120, -100)
t.pendown()
t.pensize(5)
t.left(90)
t.forward(30) # 树干
t.right(90)
draw_triangle(t, 40, "white")    # 树冠

t.hideturtle()
screen.mainloop()