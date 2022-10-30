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
turtle.begin_fill()
turtle.fillcolor(bg_eye)
turtle.end_fill()
turtle.pendown()

turtle.circle(eye_size)





turtle.done()