import turtle
t = turtle.Turtle()
t.hideturtle
color = input("Nhap ma  mau: ")
w = float(input("Nhập w:"))
h = float(input("Nhập h:"))

t.color(color)
t.forward(h)
t.right(90)
t.forward(w)
t.right(90)
t.forward(h)
t.right(90)
t.forward(w)
t.right(90)

c = (w+h)*2
v = w*h

print("Chu vi dài = {w}  rộng =  {h} là {c} ".format(w=w, h=h,c=c))
print("Diện tích dài = {w}  rộng =  {h} là {v} ".format(w=w, h=h,v=v))

turtle.done()