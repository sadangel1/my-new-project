import turtle

d = 100
l = 0
tt = turtle.Turtle()
tt.hideturtle()
while tt.distance(0,0) < d:
    l+=0.1
    tt.forward(l)
    tt.left(15)
    
turtle.done()
