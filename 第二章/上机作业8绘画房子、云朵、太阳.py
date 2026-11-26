import turtle

# 1. 初始化设置
screen = turtle.Screen()
screen.setup(700, 450)
screen.bgcolor("#A0A0A0")  # 灰色背景
screen.title("图2-10 样图")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 2. 画太阳 (右上角，橙色实心圆)
t.penup()
t.goto(220, 100)
t.pendown()
t.color("orange", "orange")
t.begin_fill()
t.circle(35)
t.end_fill()


# ================= 核心修改区：盖章法画云朵 =================
# 3. 画云朵 (左上角，实心无缝隙，且绝对水平)
def draw_cloud(x, y):
    t.penup()
    t.color("white", "white")

    # 第一步：盖章左边的小圆
    t.goto(x - 25, y)
    t.pendown()
    t.begin_fill()
    t.circle(18)
    t.end_fill()

    # 第二步：盖章中间的大圆（稍微偏上一点）
    t.penup()
    t.goto(x - 5, y + 15)  # 移动到中间大圆的底部
    t.pendown()
    t.begin_fill()
    t.circle(28)
    t.end_fill()

    # 第三步：盖章右边的小圆
    t.penup()
    t.goto(x + 25, y)
    t.pendown()
    t.begin_fill()
    t.circle(18)
    t.end_fill()

    # 第四步：盖一个底盘，把中间的空隙彻底堵死
    t.penup()
    t.goto(x - 10, y)  # 从最左侧底部开始
    t.pendown()
    t.begin_fill()
    t.circle(15)  # 画个圆垫底
    t.end_fill()


draw_cloud(-220, 90)  # 移动到左上角
# ================= 核心修改区结束 =================

# 4. 画房子的墙壁 (正方形，白墙)
wall_size = 120
t.penup()
t.goto(-60, -60)  # 以 (0,0) 为中心
t.pendown()
t.color("black", "white")
t.begin_fill()
for _ in range(4):
    t.forward(wall_size)
    t.left(90)
t.end_fill()

# 5. 画屋顶 (等腰直角三角形，棕色)
t.penup()
t.goto(-65, 60)
t.pendown()
t.color("black", "brown")
t.begin_fill()
t.goto(0, 125)
t.goto(65, 60)
t.goto(-65, 60)
t.end_fill()

# 6. 画门 (长方形，棕色)
t.penup()
t.goto(-20, -60)
t.pendown()
t.color("black", "brown")
t.begin_fill()
for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

# 画门把手 (白色小圆点)
t.penup()
t.goto(10, -30)
t.pendown()
t.color("white", "white")
t.begin_fill()
t.circle(3)
t.end_fill()

# 7. 写字 ("我的第一个绘画作品")
t.penup()
t.goto(0, -85)
t.color("black")
t.write("我的第一个绘画作品", align="center", font=("Arial", 12, "normal"))

# 8. 结束
turtle.done()