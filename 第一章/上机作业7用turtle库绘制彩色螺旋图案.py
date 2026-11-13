import turtle as t
t.speed(0)
t.bgcolor('black')
colors = ['white','red','magenta','orange','yellow','green','cyan','blue','purple','violet']
for x in range(720):
    t.pencolor(colors[x%10])
    t.width(int(x/100+1))
    t.forward(x/2)
    t.left(x)
t.done()