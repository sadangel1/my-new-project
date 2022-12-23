from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Form registration")
fullName_lbl= Label(window,text="Full name")
email_lbl= Label(window,text="Email")
address_lbl= Label(window,text="Address")
fullname_txt = Entry(window)
email_txt = Entry(window)
address_txt = Entry(window)
submit_btn = Button(window,text="Submit")

#fullName_lbl.pack()
#fullname_txt.pack()
#email_lbl.pack()
#email_txt.pack()
#address_lbl.pack()
#address_txt.pack()
#submit_btn.pack()


#fullName_lbl.grid(row =0,column= 0)
#fullname_txt.grid(row =0,column= 1)
#email_lbl.grid(row =1,column=0)
#email_txt.grid(row =1,column= 1)
#address_lbl.grid(row =2,column= 0)
#address_txt.grid(row =2,column= 1)
#submit_btn.grid(row =3,column= 1)

fullName_lbl.place(x=10,y =10,width =50)
fullname_txt.place(x=100,y =10,width =200)
email_lbl.place(x=10,y =40,width =50)
email_txt.place(x=100,y =40,width =200)
address_lbl.place(x=10,y =80,width =50)
address_txt.place(x=100,y =80,width =200)
submit_btn.place(x=100,y =120,width =100)

window.mainloop()
