import turtle


turtle.color('red')
for i in range (0,5):
    turtle.forward(100)
    turtle.right(144)

turtle.penup() 
turtle.goto(200,200)
turtle.pendown()   
turtle.color('#0f9d58')



for i in range (0,4):
    turtle.forward(50)
    turtle.right(90)
   
    
  


turtle.penup() 
turtle.goto(-400,-400)  
turtle.pendown()   
turtle.color('blue') 

turtle.pensize(10)
turtle.fillcolor('#0f9d58')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup() 
turtle.goto(-400,0)  
turtle.pendown() 

turtle.pensize(1)
turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()


turtle.done()