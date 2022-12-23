from tkinter import *


top = Tk()
top.title("Demo")
top.geometry("400x400")

def checkvalue():
    Message( top,text = "Hello Python")

button1 =Button(top,text = "OK",fg= "red")

button1.place(x=100,y=100,width=100,height=100,anchor="center")


mainloop()