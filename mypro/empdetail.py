import random
from tkinter import*
from tkinter import messagebox, StringVar
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import LabelFrame
import mysql.connector
from time import strftime
from datetime import datetime


class empdetails:


    def __init__(self,root):
        self.root=root
        self.root.title("hotel managment system")
        self.root.geometry("1295x550+230+220")
        self.var_dept= StringVar()
        self.var_id= StringVar()
        self.var_con = StringVar()

        # title
        title = Label(self.root, text=" Employe Managment", font=("times new roman", 20, "bold"), fg="gold",
                      bg="black").place(x=0, y=0, width=1295, height=50)
        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text=" New Room ", padx=2,
                                  font=("times new roman", 20, "bold"))
        lblframeleft.place(x=5, y=50, width=540, height=350)
        self.bg11 = ImageTk.PhotoImage(file="images/logo2.jpg")
        self.bg11_image = Label(self.root, image=self.bg11, bd=4, relief=RIDGE).place(x=0, y=0, width=100, height=40)
        # id
        Id = Label(root, text="ID", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                   bd=1, relief=RIDGE).place(x=20, y=90, width=170, height=25)

        Entry(root, textvariable=self.var_id, font=("times new roman", 15)).place(x=200, y=90, width=170, height=25)

        #dept
        dept = Label(root, text="Department", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=130, width=170, height=25)

        Entry(root,textvariable=self.var_dept,  font=("times new roman", 15)).place(x=200, y=130, width=170,height=25)
        contact = Label(root, text="Contact", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                     bd=1, relief=RIDGE).place(x=20, y=170, width=170, height=25)

        Entry(root, textvariable=self.var_con, font=("times new roman", 15)).place(x=200, y=170, width=170, height=25)

        #buttons
        btn_frame = Frame(root, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=350, height=40)
        btnadd = Button(btn_frame, command=self.add_data,text="ADD", font=("times new roman", 12, "bold"), bg="black",
                        fg="gold", width=8)
        btnadd.grid(row=0, column=0, padx=1)
        btnupdate = Button(btn_frame, command=self.update,text="UPDATE", font=("times new roman", 12, "bold"),
                           bg="black", fg="gold", width=8)
        btnupdate.grid(row=0, column=1, padx=1)
        btndel = Button(btn_frame, command=self.deletebook, text="DELETE", font=("times new roman", 12, "bold"),
                        bg="black", fg="gold", width=8)
        btndel.grid(row=0, column=2, padx=1)
        btnre = Button(btn_frame, command=self.reset,text="RESET", font=("times new roman", 12, "bold"), bg="black",
                       fg="gold", width=8)
        btnre.grid(row=0, column=3, padx=1)
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details ", padx=2,
                                 font=("times new roman", 15, "bold"))
        table_frame.place(x=600, y=55, width=600, height=280)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.empdept = ttk.Treeview(table_frame, column=("empcon",
            "empid","empdept"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.empdept.xview)
        scroll_y.config(command=self.empdept.yview)



        self.empdept.heading("empcon", text="Contact")
        self.empdept.heading("empid", text="Id")
        self.empdept.heading("empdept", text="Department")





        self.empdept["show"] = "headings"



        self.empdept.column("empcon", width=100)
        self.empdept.column("empid", width=100)
        self.empdept.column("empdept", width=100)



        self.empdept.pack(fill=BOTH, expand=1)
        self.empdept.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
     # add data

    def add_data(self):

        if self.var_dept.get() == "" or self.var_id.get()=="":
            messagebox.showerror("error", "all field are required", parent=self.root)
        else:
            try:
                # connecting to the database
                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                mycur.execute("insert into empdetail1 values(%s,%s,%s)", (str(self.var_con.get()), str(self.var_id.get()),str(self.var_dept.get())))





                db.commit()
                self.fetch_data()
                db.close()
                messagebox.showinfo("success", "room added succesfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"something went wrong:{str(es)}", parent=self.root)
    #fetch data
    def fetch_data(self):
        # connecting to the database
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select * from empdetail1")
        rows = mycur.fetchall()
        if len(rows) != 0:
            self.empdept.delete(*self.empdept.get_children())
            for i in rows:
                self.empdept.insert("", END, values=i)
            db.commit()
            db.close()

        # get cursor
    def get_cursor(self, event=""):
        cur_row = self.empdept.focus()
        content = self.empdept.item(cur_row)
        row = content["values"]
        self.var_id.set(row[1])
        self.var_dept.set(row[2])
        self.var_con.set(row[0])

        # update

    def update(self):
        if self.var_dept.get() == "":
            messagebox.showerror("error", "please enter Contact no", parent=self.root)
        else:

            # connecting to the database
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            # mycur.execute("update roombook set checkin=%s,checkout=%s,roomtype=%s,availableroom=%s,meal=%s,noofday=%s where contact=%s",
            # (str(self.var_checkin.get()), str(self.var_checkout.get()), str(self.var_roomtype.get()),
            # str(self.var_roomavailable.get()), str(self.var_meal.get()), str(self.var_noofday.get()),
            # str(self.var_contact.get())))
            mycur.execute("update empdetail1 set empdept=%s,empcon=%s where empid=%s",
                          (self.var_dept.get(),self.var_con.get(),self.var_id.get()

                           ))

        db.commit()
        self.fetch_data()
        db.close()
        messagebox.showinfo("success", "update successfully", parent=self.root)

    def deletebook(self):
        deletebook = messagebox.askyesno("hotel managment", "r u really want ro cancle booking", parent=self.root)
        if deletebook > 0:
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            query = "delete from empdetail1 where empid=%s"
            value = (self.var_id.get(),)
            mycur.execute(query, value)
        else:
            if not deletebook:
                return
        db.commit()
        self.fetch_data()
        db.close()
        # resset

    def reset(self):
        self.var_id.set('')
        self.var_dept.set('')
        self.var_con.set('')





if __name__ == '__main__':
            root = Tk()
            obj = empdetails(root)
            root.mainloop()
