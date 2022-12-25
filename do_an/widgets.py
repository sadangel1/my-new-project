from tkinter import *
import tkinter
from obj import User,Users
import tkinter as tk
from tkinter import messagebox
import config
import helpers


class Table:
    def __init__(self,data,columns,root,key = ""):
        self.columns = columns
        self.root = root
        self.key = key
        self.load_table(data)
      
    def load_table(self,data):
        for widget in self.root.winfo_children():
            widget.destroy()
        temp_col = 0
        for idx, c in enumerate(self.columns):
            Label(self.root,font="arial 10 bold",width=20,text=c['value']).grid(row= 0, column =idx)
            temp_col = idx
        
        for idi, item in enumerate(data):
            temp_col = 0
            if ((item['name'] == self.key or item['username'] == self.key or item['name'] == self.key or  item['address'] == self.key or  item['email'] == self.key) or self.key == ""): 
                for idx, c in enumerate(self.columns):
                    Label(self.root,width=20,text=item[c['key']]).grid(row =idi + 1, column =idx)
                    temp_col = idx
                Button(self.root, text="View",width=8,command=  lambda username= item['username']:  self.open_popup_view(self.root,username)).grid(row =idi + 1, column =temp_col+1)
                Button(self.root, text="Edit",width=8,command=  lambda username= item['username']:  self.open_popup_edit(self.root,username)).grid(row =idi + 1, column =temp_col+2)
                Button(self.root, text="Delete",width=8,command=  lambda username= item['username']: self.btn_delete(username)).grid(row =idi + 1, column =temp_col+3)
    def open_popup_edit(self,w,username):
        popup_update = form_update(w,self.root) 
        popup_update.key = self.key
        user = User()
        user.get(username)
        popup_update.open_popup(user.username,user.name,user.password,user.email,user.tel,user.address,user.image,user.role) 
    def open_popup_view(self,w,username):
        popup_view = form_view(w,self.root) 
        user = User()
        user.get(username)
        popup_view.open_popup(user.username,user.name,user.password,user.email,user.tel,user.address,user.image,user.role)
    def btn_delete(self,username):
        msg_box = messagebox.askquestion('Xóa phần mềm', 'Bạn có muốn xóa không',icon='warning')
        if msg_box == 'yes':
            user = User()
            user.username = username
            user.remove()
            data = helpers.get_users_from_file()
            Table(data,self.columns,self.root,self.key)
            for widget in self.root.winfo_children():
                widget.destroy()
            self.load_table(data)

   
class form_create :
    def __init__(self,w,frame_table):
        self.w = w
        self.frame_table = frame_table
        self.username = StringVar()
        self.name = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.tel = StringVar()
        self.address = StringVar()
        self.role = StringVar()
        self.key = ""

    def close_window(self):
        data = helpers.get_users_from_file()
        columns = config.columns
        for widget in self.frame_table.winfo_children():
                widget.destroy()
        Table(data,columns,self.frame_table,self.key)
        self.window.destroy()
        

    def btn_save(self):
        message = ""
        if self.username.get() == "":
            message = "Chưa nhập username "
        elif self.name.get() == "":
            message = "Chưa nhập họ tên " 
        elif self.password.get() == "":
            message = "Chưa nhập password " 
        elif self.email.get() == "":
            message = "Chưa nhập email " 
        elif self.tel.get() == "":
            message = "Chưa nhập số điện thoại "
        elif self.address.get() == "":
            message = "Chưa nhập số địa chỉ "
        elif self.role.get() == "":
            message = "Chưa chọn phân quyền "
        else:
            user = User()
            if user.get_index_by_user_name(self.username.get()) != -1:
                message = "User đã tồn tại";
            else:
                user.set(self.username.get(),self.name.get(),self.password.get(),self.email.get(),self.tel.get(),self.address.get(),"",self.role.get())
                user.add()
                self.close_window()
        if(message != ""):
            messagebox.showerror(message=message)

    def open_popup(self):
        self.window = tk.Toplevel(self.w)
        self.window.grab_set()
        frame_nhap_thong_tin = Frame(self.window)
        frame_nhap_thong_tin.pack(anchor=W,padx=(10,10),pady=(10,10))
    
        self.role.set("Chọn phân quyền")

        Label(frame_nhap_thong_tin,text="UserName",font="arial 10 bold", anchor='w',width=20).grid(row=0,column=0,pady=(0, 5))
        Entry(frame_nhap_thong_tin,textvariable=self.username,width=50).grid(row=0,column=1, pady=(0, 5))

        Label(frame_nhap_thong_tin,text="Họ Tên",font="arial 10 bold", anchor='w',width=20).grid(row=1,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.name,width=50).grid(row=1,column=1, pady=(0, 5))

        Label(frame_nhap_thong_tin,text="Password",font="arial 10 bold", anchor='w',width=20).grid(row=2,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.password,width=50).grid(row=2,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Email",font="arial 10 bold", anchor='w',width=20).grid(row=3,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.email,width=50).grid(row=3,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Điện thoại",font="arial 10 bold", anchor='w',width=20).grid(row=4,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.tel,width=50).grid(row=4,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Địa chỉ",font="arial 10 bold", anchor='w',width=20).grid(row=5,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.address,width=50).grid(row=5,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Phân quyền",font="arial 10 bold", anchor='w',width=20).grid(row=6,column=0,pady=(0, 10))
        OptionMenu(frame_nhap_thong_tin, self.role, *config.roles).grid(row=6,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="").grid(row=7,column=0,pady=(0, 10))
        Button(frame_nhap_thong_tin, text="Save",width=8,command=self.btn_save).grid(row=7,column=1,pady=(0, 10))

        

class form_update :
    def __init__(self,w,frame_table):
        self.w = w
        self.frame_table = frame_table
        self.name = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.tel = StringVar()
        self.address = StringVar()
        self.role = StringVar()
        self.key = ""
    def close_window(self):
        data = helpers.get_users_from_file()
        for widget in self.frame_table.winfo_children():
                widget.destroy()
        columns = config.columns
        Table(data,columns,self.frame_table,self.key)
        self.window.destroy()
        

    def btn_save(self):
        message = ""
        if self.name.get() == "":
            message = "Chưa nhập họ tên " 
        elif self.password.get() == "":
            message = "Chưa nhập password " 
        elif self.email.get() == "":
            message = "Chưa nhập email " 
        elif self.tel.get() == "":
            message = "Chưa nhập số điện thoại "
        elif self.address.get() == "":
            message = "Chưa nhập số địa chỉ "
        elif self.role.get() == "":
            message = "Chưa chọn phân quyền "
        else:

            user = User()
            index = user.get_index_by_user_name(self.username);
            if index == -1:
                message = "User không đã tồn tại";
            else:
                user.set(self.username,self.name.get(),self.password.get(),self.email.get(),self.tel.get(),self.address.get(),"",self.role.get())
                user.edit(index)
                self.close_window()
        if(message != ""):
            messagebox.showerror(message=message)

    def open_popup(self,username,name,password,email,tel,address,image,role):
        self.window = tk.Toplevel(self.w)
        self.window.grab_set()
        frame_nhap_thong_tin = Frame(self.window)
        frame_nhap_thong_tin.pack(anchor=W,padx=(10,10),pady=(10,10))
    
        self.username = username
        self.name.set(name)
        self.password.set(password)
        self.email.set(email)
        self.tel.set(tel)
        self.address.set(address)
        self.role.set(role)
   

        Label(frame_nhap_thong_tin,text="Họ Tên",font="arial 10 bold", anchor='w',width=20).grid(row=1,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.name,width=50).grid(row=1,column=1, pady=(0, 5))

        Label(frame_nhap_thong_tin,text="Password",font="arial 10 bold", anchor='w',width=20).grid(row=2,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.password,width=50).grid(row=2,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Email",font="arial 10 bold", anchor='w',width=20).grid(row=3,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.email,width=50).grid(row=3,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Điện thoại",font="arial 10 bold", anchor='w',width=20).grid(row=4,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.tel,width=50).grid(row=4,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Địa chỉ",font="arial 10 bold", anchor='w',width=20).grid(row=5,column=0,pady=(0, 10))
        Entry(frame_nhap_thong_tin,textvariable=self.address,width=50).grid(row=5,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Phân quyền",font="arial 10 bold", anchor='w',width=20).grid(row=6,column=0,pady=(0, 10))
        OptionMenu(frame_nhap_thong_tin, self.role, *config.roles).grid(row=6,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="").grid(row=7,column=0,pady=(0, 10))
        Button(frame_nhap_thong_tin, text="Save",width=8,command=self.btn_save).grid(row=7,column=1,pady=(0, 10))
    
class form_view :
    def __init__(self,w,frame_table):
        self.w = w
        self.frame_table = frame_table
        self.name = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.tel = StringVar()
        self.address = StringVar()
        self.role = StringVar()
    def close_window(self):
        data = helpers.get_users_from_file()
        columns = config.columns
        Table(data,columns,self.frame_table)
        self.window.destroy()
        
    def open_popup(self,username,name,password,email,tel,address,image,role):
        self.window = tk.Toplevel(self.w)
        self.window.grab_set()
        frame_nhap_thong_tin = Frame(self.window)
        frame_nhap_thong_tin.pack(anchor=W,padx=(10,10),pady=(10,10))
    
        self.username = username
        self.name.set(name)
        self.password.set(password)
        self.email.set(email)
        self.tel.set(tel)
        self.address.set(address)
        self.role.set(role)


        Label(frame_nhap_thong_tin,text="User Name",font="arial 10 bold", anchor='w',width=20).grid(row=0,column=0,pady=(0, 10))
        Label(frame_nhap_thong_tin,text=username,width=50).grid(row=0,column=1, pady=(0, 5)) 
        Label(frame_nhap_thong_tin,text="Họ Tên",font="arial 10 bold", anchor='w',width=20).grid(row=1,column=0,pady=(0, 10))
        Label(frame_nhap_thong_tin,text=name,width=50).grid(row=1,column=1, pady=(0, 5))

        Label(frame_nhap_thong_tin,text="Password",font="arial 10 bold", anchor='w',width=20).grid(row=2,column=0,pady=(0, 10))
        Label(frame_nhap_thong_tin,text=name,width=50).grid(row=2,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Email",font="arial 10 bold", anchor='w',width=20).grid(row=3,column=0,pady=(0, 10))
        Label(frame_nhap_thong_tin,text=email,width=50).grid(row=3,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Điện thoại",font="arial 10 bold", anchor='w',width=20).grid(row=4,column=0,pady=(0, 10))
        Label(frame_nhap_thong_tin,text=tel,width=50).grid(row=4,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Địa chỉ",font="arial 10 bold", anchor='w',width=20).grid(row=5,column=0,pady=(0, 10))
        Label(frame_nhap_thong_tin,text=address,width=50).grid(row=5,column=1,pady=(0, 10))

        Label(frame_nhap_thong_tin,text="Phân quyền",font="arial 10 bold", anchor='w',width=20).grid(row=6,column=0,pady=(0, 10))
        Label(frame_nhap_thong_tin,text=role,width=50).grid(row=5,column=1,pady=(0, 10))

