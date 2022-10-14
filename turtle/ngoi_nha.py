import turtle



turtle.penup()
turtle.goto(-350,-350)
turtle.pendown()

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.left(-90)
for i in range(0,4):
    turtle.left(90)
    turtle.forward(200)

turtle.end_fill()

turtle.penup()
turtle.goto(-350,-150)
turtle.pendown()
turtle.fillcolor("#ff00ff")

turtle.begin_fill()
turtle.goto(-250,-50)

turtle.goto(-150,-150)
turtle.goto(-350,-150)
turtle.end_fill()

turtle.penup()
turtle.goto(-250,-50)
turtle.pendown()
turtle.fillcolor("#ffa500")
turtle.begin_fill()
turtle.goto(-150,50)
turtle.goto(-50,-50)
turtle.goto(-150,-150)
turtle.goto(-250,-50)

turtle.end_fill()

turtle.penup()
turtle.goto(-150,-150)
turtle.pendown()
turtle.fillcolor("#feff02")
turtle.begin_fill()
turtle.goto(-150,-350)
turtle.goto(-50,-250)
turtle.goto(-50,-50)
turtle.goto(-150,-150)

turtle.end_fill()

turtle.penup()
turtle.goto(-300,-225)
turtle.pendown()
turtle.fillcolor("#90f08f")
turtle.begin_fill()
turtle.goto(-200,-225)
turtle.goto(-200,-350)
turtle.goto(-300,-350)
turtle.goto(-300,-225)

turtle.end_fill()

turtle.penup()
turtle.goto(-125,-200)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.goto(-75,-150)
turtle.goto(-75,-200)
turtle.goto(-125,-250)
turtle.goto(-125,-200)

turtle.end_fill()

turtle.penup()
turtle.goto(200,350)
turtle.pendown()
turtle.goto(200,150)

turtle.penup()
turtle.goto(100,250)
turtle.pendown()
turtle.goto(300,250)

turtle.penup()
turtle.goto(125,325)
turtle.pendown()
turtle.goto(275,175)

turtle.penup()
turtle.goto(275,325)
turtle.pendown()
turtle.goto(125,175)

turtle.fillcolor("yellow")
turtle.penup()
turtle.goto(125,250)
turtle.pendown()
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()

turtle.penup()
turtle.goto(125,-225)
turtle.pendown()
turtle.fillcolor("#90f08f")
turtle.begin_fill()
turtle.goto(225,-150)
turtle.goto(325,-225)
turtle.goto(125,-225)
turtle.end_fill()

turtle.penup()
turtle.goto(145,-175)
turtle.pendown()
turtle.fillcolor("#90f08f")
turtle.begin_fill()
turtle.goto(225,-100)
turtle.goto(310,-175)
turtle.goto(145,-175)
turtle.end_fill()

turtle.penup()
turtle.goto(150,-125)
turtle.pendown()
turtle.fillcolor("#90f08f")
turtle.begin_fill()
turtle.goto(225,-50)
turtle.goto(300,-125)
turtle.goto(150,-125)
turtle.end_fill()

turtle.penup()
turtle.goto(200,-300)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.goto(200,-225)
turtle.goto(250,-225)
turtle.goto(250,-300)
turtle.goto(200,-300)

turtle.end_fill()

turtle.done()