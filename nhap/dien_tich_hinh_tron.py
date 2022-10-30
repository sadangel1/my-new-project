import re
import turtle
import math
t =turtle.Turtle()
r = float(input("Nhập chu vi: "))
t.hideturtle()
t.pensize(1)
t.color("red")
t.circle(r)
c = 2 * math.pi * r
s= math.pi * r *r


print("Chu vi = {r}  là {c}".format(r=r,c =c))
print("Dien tich = {r}  là {s}".format(r=r,s =s))
turtle.done()

