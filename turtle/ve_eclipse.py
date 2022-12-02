import turtle
import random



colors = ['red','blue','green','yellow','purple'];

def eclipse(x,y,width,r):
    color = colors[int(random.randrange(5))];
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.right(r)
    t.pencolor(color)
    t.pendown()
    for i in range(2):
        t.circle(width,90)
        t.circle(width//2,90)
step = 0

ws = turtle.Screen()
ws.bgcolor('black')
soVong = 40
for i in range(0,soVong):
    step += float(360/soVong)
    eclipse(0,0,200,step)
turtle.done()