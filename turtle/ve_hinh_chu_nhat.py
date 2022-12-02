import turtle
t =  turtle.Turtle()

m =100
n = 150

turtle.pencolor('blue')
turtle.fillcolor('red')
turtle.pensize (5)

turtle.begin_fill()
turtle.forward(n)
turtle.left(90)
turtle.forward(m)
turtle.left(90)
turtle.forward(n)
turtle.left(90)
turtle.forward(m)
turtle.left(90)
turtle.end_fill()

turtle.done()