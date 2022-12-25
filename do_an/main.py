
from obj import Users
from tkinter import *
from widgets import Table,form_create
import config
import helpers



data = helpers.get_users_from_file()
columns = config.columns

def open_add(root,frame_table):
    popup_create = form_create(root,frame_table)
    popup_create.open_popup()
    popup_create.key = key.get()
def search():
    Table(data,columns,frame_table,key.get())

root = Tk()
root.title("Quản lý tài khoản")
key = StringVar()



frame_control = Frame()
frame_table = Frame()
frame_control.pack(pady=2,anchor=W)

Button(frame_control, text="Add",width=8,command=  lambda:  open_add(root,frame_table)).pack()

frame_filter = Frame()

frame_filter.pack(pady=3,anchor=W)

Label(frame_filter,text="Nhập từ khóa tìm kiếm",font="arial 10 bold", anchor='w',width=20).grid(row=0,column=0)
Entry(frame_filter,textvariable=key,width=50).grid(row=0,column=1)
Button(frame_filter, text="Search",width=8,command= search).grid(row=0,column=2)



frame_table.pack(anchor=W,padx=(10,10),pady=(10,10))
Table(data,columns,frame_table,key.get())



root.mainloop()
