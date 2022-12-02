import turtle
import luoi
import thu_vien_hinh

leaves_w_1_a = 100
leaves_c_1 = "#4e6028"
leaves_c_2 = "#76923c"
leaves_c_3 = "#c2d59b"

#f = turtle.Turtle() 
#luoi.make_grid(f)


def leaves(x,y,width,color):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width) # draw base
    t.left(120)
    t.forward(width)
    t.left(120)
    t.forward(width)
    t.end_fill()
    
 
def tree(x,y):

    leaves(-250 + x,-100 + y,100,leaves_c_1)
    leaves(-240 + x,-15 + y,80,leaves_c_2)
    leaves(-230 + x,50 + y, 60 ,leaves_c_3) 
    stem(-250 +30 + x ,-100 + y)


def stem(x,y):
    t = turtle.Turtle()
    t.penup()
    t.goto(x,y)
    t.fillcolor("#808080")
    t.pendown()
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.end_fill()
def house():
    thu_vien_hinh.chu_nhat(-160,0,200,120,"red",1)
    thu_vien_hinh.chu_nhat(-60,120,20,160,"yellow",1)
    thu_vien_hinh.tam_giac_deu(-160,120,150,"blue",1)
    thu_vien_hinh.chu_nhat(-80,0,40,80,"yellow",1)

tree(-100,0)
tree(400,0)
house()

turtle.done()