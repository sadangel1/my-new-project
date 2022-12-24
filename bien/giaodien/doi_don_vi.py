from tkinter import *
from tkinter import messagebox


gram = 0
pounds = 0
ounce = 0

def chuyendoi():
    if(dulieu.get().isnumeric() ):
        gram = round(float(dulieu.get()) * 1000,2)
        pounds = round(float(dulieu.get()) * 2.20,2)
        ounce = round(float(dulieu.get())  * 35.27,2)
        lblG.config(text=gram)
        lblP.config(text=pounds)
        lblO.config(text=ounce)
    else:
        messagebox.showerror(message="Số không hợp lệ")    

root = Tk()



Label(root,text="Nhập Kg").grid(row=0,column=0)
dulieu = Entry(root)
dulieu.grid(row=0,column=1)
Button(root,text="Convert",command=chuyendoi).grid(row=0,column=2)
Label(text="Gram").grid(row=1,column=0)
Label(text="Pounds").grid(row=1,column=1)
Label(text="Ounce").grid(row=1,column=2)

Label(text="Gram").grid(row=1,column=0)
Label(text="Pounds").grid(row=1,column=1)
Label(text="Ounce").grid(row=1,column=2)

lblG = Label()
lblG.grid(row=2,column=0)
lblP = Label()
lblP.grid(row=2,column=1)
lblO = Label()
lblO.grid(row=2,column=2)

root.mainloop()