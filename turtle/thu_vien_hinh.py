import turtle
def chu_nhat(x,y,w,h,color,hideturtle=0):
    t = turtle.Turtle()
    if hideturtle == 1:
        t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def hinh_vuong(x,y,w,color,hideturtle=0):
    t = turtle.Turtle()
    if hideturtle == 1:
        t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(w)
        t.left(90)
    t.end_fill()

def tam_giac_deu(x,y,w,color,hideturtle=0):
    t = turtle.Turtle()
    if hideturtle == 1:
        t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(w)
        t.left(120)
    t.end_fill()   