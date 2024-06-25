import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import LabelFrame
import mysql.connector
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from time import strftime
from datetime import datetime
import tkinter as tk
from tkcalendar import dateentry, Calendar
import qrcode


class Employe:
    def __init__(self, root):
        self.root = root

        self.root.title("hotel managment system")
        self.root.geometry("1295x550+230+220")
        self.var_empid = StringVar()
        self.var_empname = StringVar()
        self.var_empdept = StringVar()
        self.var_empgen = StringVar()
        self.var_empmail = StringVar()
        self.var_empadd = StringVar()


        # title
        title = Label(self.root, text="Employe detail", font=("times new roman", 20, "bold"), fg="gold",
                      bg="black").place(x=0, y=0, width=1295, height=50)
        self.bg11 = ImageTk.PhotoImage(file="images/logo2.jpg")
        self.bg11_image = Label(self.root, image=self.bg11, bd=4, relief=RIDGE).place(x=0, y=0, width=100, height=40)
        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Employees details", padx=2,
                                  font=("times new roman", 20, "bold"))
        lblframeleft.place(x=5, y=50, width=425, height=490)

        # labels and entry
        # lbl_cust_ref=Label(root,bd=2,relief=RIDGE,text="customer ref",padx=5,pady=7,font=("times new roman", 15, "bold")).place(x=5,y=50,width=425,height=490)
        # Label(root, text="").pack()
        lbl_con = Label(root, text="Employe name", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=90, width=170, height=25)

        Entry(root, textvariable=self.var_empname,font=("times new roman", 15)).place(x=200, y=90, width=130, height=25)


        # emp dept
        empdept = Label(root, text="Employe Department", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                           bd=1, relief=RIDGE).place(x=20, y=130, width=170, height=25)
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select empdept from empdetail1")
        rows = mycur.fetchall()
        combo2 = ttk.Combobox(root, textvariable=self.var_empdept,font=("times new roman", 15), width=27)
        combo2["value"] = rows
        combo2.current()
        combo2.place(x=200, y=130, width=170, height=25)


        # emp gender
        gender = Label(root, text="Gender", font=("times new roman", 15), pady=-200, fg="black",
                            bg="white",
                            bd=1, relief=RIDGE).place(x=20, y=170, width=170, height=25)
        combo = ttk.Combobox(root, textvariable=self.var_empgen,font=("times new roman", 15,),  width=27)
        combo["value"] = ("male", "female")
        combo.current(0)
        combo.place(x=200, y=170, width=170, height=25)

        # address
        address = Label(root, text="Address", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=210, width=170, height=25)
        Entry(root,textvariable=self.var_empadd, font=("times new roman", 15)).place(x=200, y=210, width=130, height=25)


        # email
        email = Label(root, text="Email", font=("times new roman", 15), pady=-200, fg="black",
                            bg="white",
                            bd=1, relief=RIDGE).place(x=20, y=250, width=170, height=25)
        Entry(root,textvariable=self.var_empmail, font=("times new roman", 15)).place(x=200, y=250, width=130, height=25)
        # email
        id = Label(root, text="Id", font=("times new roman", 15), pady=-200, fg="black",
                      bg="white",
                      bd=1, relief=RIDGE).place(x=20, y=300, width=170, height=25)
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select empcon from empdetail1")
        rows = mycur.fetchall()
        combo2 = ttk.Combobox(root, textvariable=self.var_empid, font=("times new roman", 15), width=27)
        combo2["value"] = rows
        combo2.current()
        combo2.place(x=200, y=300, width=170, height=25)




        # buttons
        btn_frame = Frame(root, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=490, width=480, height=40)
        # bill button

        btnadd = Button(btn_frame, command=self.add_data,text="ADD", font=("times new roman", 12, "bold"), bg="black",
                        fg="gold", width=8)
        btnadd.grid(row=0, column=0, padx=1)
        btnupdate = Button(btn_frame, command=self.update, text="UPDATE", font=("times new roman", 12, "bold"),
                           bg="black", fg="gold", width=8)
        btnupdate.grid(row=0, column=1, padx=1)
        btndel = Button(btn_frame, command=self.deletebook, text="DELETE", font=("times new roman", 12, "bold"),
                        bg="black", fg="gold", width=8)
        btndel.grid(row=0, column=2, padx=1)
        btnre = Button(btn_frame,command=self.reset, text="RESET", font=("times new roman", 12, "bold"), bg="black",
                       fg="gold", width=8)
        btnre.grid(row=0, column=3, padx=1)
        btnem = Button(btn_frame, command=self.orcode, text="Card", font=("times new roman", 12, "bold"), bg="black",
                       fg="gold", width=8)
        btnem.grid(row=0, column=4, padx=1)
        # image
        self.bg11 = ImageTk.PhotoImage(file="images/img4.jpg")

        self.bg11_image = Label(self.root, image=self.bg11, bd=4, relief=RIDGE).place(x=760, y=55, width=350,
                                                                                      height=190)
        # TABLE FRAME search system
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System ", padx=2,
                                 font=("times new roman", 15, "bold"))
        table_frame.place(x=435, y=280, width=860, height=260)
        lblsaerch = Label(table_frame, text="Search By", font=("times new roman", 15, "bold"), bg="red", fg="white",
                          width=8)
        lblsaerch.grid(row=0, column=0, padx=1, sticky=W)
        self.search_var = StringVar()
        combosearch = ttk.Combobox(table_frame, font=("times new roman", 12), width=20,
                                   state="readonly")
        combosearch["value"] = ("Contact", "Room")
        combosearch.current(0)
        combosearch.grid(row=0, column=1)
        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame, font=("arial", 12, "bold"), width=20)
        txtsearch.grid(row=0, column=2)

        btnsearch = Button(table_frame, text="Search", font=("times new roman", 12, "bold"),
                           bg="black", fg="gold", width=8)
        btnsearch.grid(row=0, column=3, padx=1)
        btnshow = Button(table_frame, text="Show all", font=("times new roman", 12, "bold"),
                         bg="black", fg="gold", width=8)
        btnshow.grid(row=0, column=4, padx=1)

        # shoe data table
        deatilframe = Frame(table_frame, bd=2, relief=RIDGE)
        deatilframe.place(x=0, y=50, width=860, height=180)
        scroll_x = ttk.Scrollbar(deatilframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(deatilframe, orient=VERTICAL)
        self.emptbl = ttk.Treeview(deatilframe, column=(
            "emp_id","emp_name", "emp_dept", "emp_add","emp_gen", "emp_mail"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.emptbl.xview)
        scroll_y.config(command=self.emptbl.yview)

        self.emptbl.heading("emp_name", text="Employe Name")
        self.emptbl.heading("emp_dept", text="Department")
        self.emptbl.heading("emp_add", text="Address")
        self.emptbl.heading("emp_gen", text="Gender")
        self.emptbl.heading("emp_mail", text="Email")
        self.emptbl.heading("emp_id", text="Contact")



        self.emptbl["show"] = "headings"
        self.emptbl.column("emp_name", width=100)
        self.emptbl.column("emp_dept", width=100)
        self.emptbl.column("emp_add", width=100)
        self.emptbl.column("emp_gen", width=100)
        self.emptbl.column("emp_mail", width=100)
        self.emptbl.column("emp_id", width=100)


        self.emptbl.pack(fill=BOTH, expand=1)
        self.emptbl.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

        # add data
    def add_data(self):

        if self.var_empgen.get() == "" or self.var_empmail.get() == "":
            messagebox.showerror("error", "all field are required", parent=self.root)
        else:
            try:
                # connecting to the database
                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                mycur.execute("insert into emps values(%s,%s,%s,%s,%s,%s)",
                                (str(self.var_empid.get()),str(self.var_empname.get()), str(self.var_empdept.get()),
                                 str(self.var_empadd.get()),str(self.var_empgen.get()), str(self.var_empmail.get())))

                db.commit()
                self.fetch_data()
                db.close()
                messagebox.showinfo("success", "booking succesfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"something went wrong:{str(es)}", parent=self.root)
        # fetch data
        # fetch data

    def fetch_data(self):
        # connecting to the database
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select * from emps")
        rows = mycur.fetchall()
        if len(rows) != 0:
            self.emptbl.delete(*self.emptbl.get_children())
            for i in rows:
                self.emptbl.insert("", END, values=i)
            db.commit()
            db.close()
        # get cursor

    def get_cursor(self, event=""):
        cur_row = self.emptbl.focus()
        content = self.emptbl.item(cur_row)
        row = content["values"]
        self.var_empname.set(row[1])
        self.var_empdept.set(row[2])
        self.var_empgen.set(row[4])
        self.var_empadd.set(row[3])
        self.var_empmail.set(row[5])

        self.var_empid.set(row[0])



        # update

    def update(self):
        if self.var_empdept.get() == "":
            messagebox.showerror("error", "please enter department ", parent=self.root)
        else:

            # connecting to the database
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            # mycur.execute("update roombook set checkin=%s,checkout=%s,roomtype=%s,availableroom=%s,meal=%s,noofday=%s where contact=%s",
            # (str(self.var_checkin.get()), str(self.var_checkout.get()), str(self.var_roomtype.get()),
            # str(self.var_roomavailable.get()), str(self.var_meal.get()), str(self.var_noofday.get()),
            # str(self.var_contact.get())))
            mycur.execute("update emps set emp_name=%s,emp_dept=%s,emp_add=%s,emp_gen=%s,emp_mail=%s where emp_id=%s",
                          (self.var_empname.get(), self.var_empdept.get(), self.var_empadd.get(),
                           self.var_empgen.get(), self.var_empmail.get(), self.var_empid.get()

                           ))

        db.commit()
        self.fetch_data()
        db.close()
        messagebox.showinfo("success", "update successfully", parent=self.root)

    def deletebook(self):
        deletebook = messagebox.askyesno("hotel managment", "r u really want to delete employe detail", parent=self.root)
        if deletebook > 0:
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            query = "delete from emps where emp_id=%s"
            value = (self.var_empid.get(),)
            mycur.execute(query, value)
        else:
            if not deletebook:
                return
        db.commit()
        self.fetch_data()
        db.close()

        # resset

    def reset(self):
        self.var_empname.set('')
        self.var_empdept.set('')
        self.var_empadd.set('')
        self.var_empgen.set('')
        self.var_empmail.set('')
        self.var_empid.set('')

    def orcode(self):
        root=self.root

        self.root.geometry("1100x600+200+50")
        self.root.title("OrCodeGenerate|developed by nisha & Mansi")
        self.root.resizable(False, False)
        title = Label(self.root, text="Or Code Generator", font=("times new roman", 40), bg="#053246",
                      fg="white").place(x=0, y=0, relwidth=1)
        # employedeatil
        # variables
        self.var_empcode = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_des = StringVar()
        empframe = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        empframe.place(x=50, y=100, width=500, height=380)
        title1 = Label(empframe, text="Employe Details", font=("times new roman", 30, "bold"), bg="#043256",
                       fg="white").place(x=0, y=0, relwidth=1)
        empid = Label(empframe, text="Emloye Id", font=("times new roman", 15), bg="white").place(x=20, y=60)

        empnm = Label(empframe, text="Emloye Name", font=("times new roman", 15, "bold"), bg="white").place(x=20, y=100)
        empdept = Label(empframe, text="Department", font=("times new roman", 15, "bold"), bg="white").place(x=20,
                                                                                                             y=140)
        empdes = Label(empframe, text="Designation", font=("times new roman", 15, "bold"), bg="white").place(x=20,
                                                                                                             y=180)

        txtempid = Entry(empframe, font=("times new roman", 15), textvariable=self.var_empcode, bg="lightyellow").place(
            x=200, y=60)

        txtnm = Entry(empframe, font=("times new roman", 15), textvariable=self.var_name, bg="lightyellow").place(x=200,
                                                                                                                  y=100)
        txtdept = Entry(empframe, font=("times new roman", 15), textvariable=self.var_dept, bg="lightyellow").place(
            x=200, y=140)

        txtdes = Entry(empframe, font=("times new roman", 15), textvariable=self.var_des, bg="lightyellow").place(x=200,
                                                                                                                  y=180)
        btn = Button(empframe, text="Or-Generator", command=self.generate, font=("times new roman", 18, "bold"),
                     bg="#2196f3", fg="white").place(x=90, y=250, width=200, height=30)
        btnclr = Button(empframe, text="Clear", command=self.clear, font=("times new roman", 18, "bold"), bg="#607d8b",
                        fg="white").place(x=282, y=250, width=120, height=30)
        self.msg = "Or code generated successfully"
        self.lbl_msg = Label(empframe, text=self.msg, font=("times new roman", 15, "bold"), fg="green", bg="white")
        self.lbl_msg.place(x=0, y=320, relwidth=1)
        # employeOrcode
        qrframe = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qrframe.place(x=600, y=100, width=250, height=380)
        qrtitle = Label(qrframe, text="Employe Or Code", font=("times new roman", 20, "bold"), bg="#043256",
                        fg="white").place(x=0, y=0, relwidth=1)
        self.qr_code = Label(qrframe, text="no Or code \n availabe", font=("times new roman", 15, "bold"), bg="#3f51b5",
                             fg="white", bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_empcode.set('')
        self.var_name.set('')
        self.var_dept.set('')
        self.var_des.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_des.get() == '' or self.var_empcode.get() == '' or self.var_dept.get() == '' or self.var_name.get() == '':
            self.msg = "All fileds are required"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            qr_data = (
                f"Employe Id:{self.var_empcode.get()}\nEmploye name:{self.var_name.get()}\nEmploye Department:{self.var_dept.get()}\nEmploye Designtion:{self.var_des.get()})")
            qr_code = qrcode.make(qr_data)
            # print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save("images/Emp_" + str(self.var_empcode.get()) + ".png")

            # image updating
            self.img = ImageTk.PhotoImage(file="images/Emp_" + str(self.var_empcode.get()) + ".png")
            self.qr_code.config(image=self.img)
            # updating notification

            self.msg = "or code generate successfully"
            self.lbl_msg.config(text=self.msg, fg="green")

    pass





if __name__ == '__main__':
    root = Tk()
    obj = Employe(root)
    root.mainloop()