from tkinter import *
import qrcode
from PIL import Image,ImageTk

class Qrcode:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x600+200+50")
        self.root.title("OrCodeGenerate|developed by nisha patel")
        self.root.resizable(False,False)
        title=Label(self.root,text="Or Code Generator",font=("times new roman",40),bg="#053246",fg="white").place(x=0,y=0,relwidth=1)
        #employedeatil
        #variables
        self.var_empcode=StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_des = StringVar()
        empframe=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        empframe.place(x=50,y=100,width=500,height=380)
        title1=Label(empframe,text="Employe Details",font=("times new roman",30,"bold"),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)
        empid=Label(empframe,text="Emloye Id",font=("times new roman",15),bg="white").place(x=20,y=60)

        empnm=Label(empframe,text="Emloye Name",font=("times new roman",15,"bold"),bg="white").place(x=20,y=100)
        empdept=Label(empframe,text="Department",font=("times new roman",15,"bold"),bg="white").place(x=20,y=140)
        empdes=Label(empframe,text="Designation",font=("times new roman",15,"bold"),bg="white").place(x=20,y=180)

        txtempid=Entry(empframe,font=("times new roman",15),textvariable=self.var_empcode,bg="lightyellow").place(x=200,y=60)

        txtnm=Entry(empframe, font=("times new roman", 15),textvariable=self.var_name, bg="lightyellow").place(x=200, y=100)
        txtdept=Entry(empframe,  font=("times new roman", 15),textvariable=self.var_dept, bg="lightyellow").place(x=200, y=140)

        txtdes=Entry(empframe,  font=("times new roman", 15),textvariable=self.var_des, bg="lightyellow").place(x=200, y=180)
        btn=Button(empframe,text="Or-Generator",command=self.generate,font=("times new roman",18,"bold"),bg="#2196f3",fg="white").place(x=90,y=250,width=200,height=30)
        btnclr=Button(empframe,text="Clear",command=self.clear,font=("times new roman",18,"bold"),bg="#607d8b",fg="white").place(x=282,y=250,width=120,height=30)
        self.msg="Or code generated successfully"
        self.lbl_msg=Label(empframe,text=self.msg,font=("times new roman",15,"bold"),fg="green",bg="white")
        self.lbl_msg.place(x=0,y=320,relwidth=1)
        # employeOrcode
        qrframe = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qrframe.place(x=600, y=100, width=250, height=380)
        qrtitle = Label(qrframe, text="Employe Or Code", font=("times new roman", 20, "bold"), bg="#043256",fg="white").place(x=0, y=0, relwidth=1)
        self.qr_code=Label(qrframe,text="no Or code \n availabe",font=("times new roman", 15, "bold"),bg="#3f51b5",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
    def clear(self):
        self.var_empcode.set('')
        self.var_name.set('')
        self.var_dept.set('')
        self.var_des.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_des.get()==''or self.var_empcode.get()=='' or self.var_dept.get()=='' or self.var_name.get()=='':
            self.msg="All fileds are required"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(f"Employe Id:{self.var_empcode.get()}\nEmploye name:{self.var_name.get()}\nEmploye Department:{self.var_dept.get()}\nEmploye Designtion:{self.var_des.get()})")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)

            qr_code.save("empQr/Emp_"+str(self.var_empcode.get())+".png")

            #image updating
            self.img=ImageTk.PhotoImage(file="empQr/Emp_"+str(self.var_empcode.get())+".png")

            self.qr_code.config(image=self.img)
            #updating notification

            self.msg = "or code generate successfully"
            self.lbl_msg.config(text=self.msg, fg="green")




    pass
root=Tk()
obj=Qrcode(root)
root.mainloop()

