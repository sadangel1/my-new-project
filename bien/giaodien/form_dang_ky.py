from tkinter import *


datas = []

index = -1

def update_book():
    select.delete(0,END)
    for n in datas:
        select.insert(END,n['name'])


def add():
    datas.append({'name':Name.get(),'phone':Phone.get(),'address':address.get(1.0, "end-1c")})
    update_book()
    reset()

    
def reset():
    Name.set('')
    Phone.set('')
    address.delete(1.0, "end-1c")
    btEdit['state'] ='inactive'

def view():
    item = datas[select.curselection()[0]]
    Name.set(item['name'])
    Phone.set(item['phone'])
    address.insert(END,item['address'])
    index = select.curselection()[0]
    btEdit['state'] ='normal'

def edit():
     datas[index] = {'name':Name.get(),'phone':Phone.get(),'address':address.get(1.0, "end-1c")}
     update_book()
     reset()

def delete():
    del datas[select.curselection()[0]]
    update_book()

root = Tk()

Name = StringVar()
Phone = StringVar()

root.geometry("520x500")

frame1 = Frame()
frame1.pack(pady=1,anchor=W)
frame2 = Frame()
frame2.pack(pady=2,anchor=W)
frame3 = Frame()
frame3.pack(pady=3,anchor=W)

Label(frame1,text="Họ Tên",font="arial 12 bold", anchor='w',width=20).pack(side=LEFT)
Entry(frame1,textvariable=Name,width=50).pack()

Label(frame2,text="Phone No",font="arial 12 bold", anchor='w',width=20).pack(side=LEFT)
Entry(frame2,textvariable=Phone,width=50).pack()

Label(frame3,text="Adress",font="arial 12 bold", anchor='w',width=20).pack(side=LEFT)
address =  Text(frame3,width=37,height=10)
address.pack()

Button(root, text="Add",width=8,command=add).place(x=100,y=270)
Button(root, text="View",width=8,command=view).place(x=100,y=310)
btEdit = Button(root, text="Edit",width=8,command=edit, state="disabled")
btEdit.place(x=100,y=350)
Button(root, text="Delete",width=8,command=delete).place(x=100,y=390)
Button(root, text="Reset",width=8,command=reset).place(x=100,y=420)

scroll = Scrollbar(root, orient="vertical")
select = Listbox(root,width=51,height=12,yscrollcommand=scroll.set)

scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)
root.mainloop()
