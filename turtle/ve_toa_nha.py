import turtle

def chu_nhat(x,y,w,h,color,hideturtle=0):
    t = turtle.Turtle()
    t.speed(0)
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

def toa_nha(x,y):
    t = chu_nhat(x,y,200,400,"green",1)
    cua_so = chu_nhat(x +50,y +100,100,200,"yellow",1)

def toa_nha_chinh(x,y):
    t = chu_nhat(x,y,400,400,"green",1)
    cua_so = chu_nhat(x +100,y ,200,200,"red",1)

toa_nha(-400,-400)
toa_nha(-200,-400)
toa_nha(-200,0)
toa_nha(-400,0)
toa_nha_chinh(0,-400)

turtle.done()