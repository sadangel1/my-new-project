from tkinter import *
login_window = Tk()  
login_window.geometry("400x250")
login_window.title("Login")

username = Label(login_window, text = "Username:").place(x = 30,y = 50)  
email = Label(login_window, text = "Email:").place(x = 30, y = 90)  
password = Label(login_window, text = "Password:").place(x = 30, y = 130)

entry1 = Entry(login_window).place(x = 100, y = 50)  
entry2 = Entry(login_window).place(x = 100, y = 90)  
entry3 = Entry(login_window).place(x = 100, y = 130)

aa = entry1.get()

login_window.mainloop() 