import turtle

turtle.pensize(5)
turtle.color('blue')
face_size = 200
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(face_size)

eye_size = 17.5
bg_eye = "red"
bg_noise = "yellow"
by_smile = "purple"

turtle.penup()
turtle.goto(-100,50)

turtle.fillcolor(bg_eye)

turtle.begin_fill()
turtle.pendown()
turtle.circle(eye_size)


turtle.penup()
turtle.goto(100,50)
turtle.fillcolor(bg_eye)
turtle.pendown()
turtle.circle(eye_size)
turtle.end_fill()
turtle.begin_fill()
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.circle(-70, steps=3)
turtle.fillcolor(bg_noise)
turtle.pendown()
turtle.end_fill()


turtle.begin_fill()
turtle.penup()
turtle.goto(-100, -70)
turtle.right(90)
turtle.fillcolor(by_smile)
turtle.pendown()
turtle.circle(100,180)


turtle.end_fill()



turtle.done()