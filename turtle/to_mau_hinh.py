import turtle
import random

num = int(random.uniform(0,3))

wn = turtle.Screen()
wn.bgcolor("black")

color = "";
if num == 0:
    color = "blue"
elif num == 1:
    color = "yellow"   
elif num == 2:
    color = "red"   
t = turtle.Turtle()    
t.shape('circle')
t.color(color)
turtle.done()
