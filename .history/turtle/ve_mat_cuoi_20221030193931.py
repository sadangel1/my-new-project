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
by_noise = "yellow"

turtle.penup()
turtle.goto(-100,50)

turtle.fillcolor(bg_eye)

turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

turtle.penup()
turtle.goto(100,50)

turtle.fillcolor(bg_eye)

turtle.pendown()

turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()



turtle.done()