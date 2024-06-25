import random
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import LabelFrame
import mysql.connector
from time import strftime
from datetime import datetime


class details:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel managment system")
        self.root.geometry("1295x550+230+220")
        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomtype=StringVar()
        # title
        title = Label(self.root, text=" Room Managment", font=("times new roman", 20, "bold"), fg="gold",
                      bg="black").place(x=0, y=0, width=1295, height=50)
        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text=" New Room ", padx=2,
                                  font=("times new roman", 20, "bold"))
        lblframeleft.place(x=5, y=50, width=540, height=350)
        self.bg11 = ImageTk.PhotoImage(file="images/logo2.jpg")
        self.bg11_image = Label(self.root, image=self.bg11, bd=4, relief=RIDGE).place(x=0, y=0, width=100, height=40)
        #floor
        lbl_floor = Label(root, text="Floor", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=90, width=170, height=25)

        Entry(root,textvariable=self.var_floor,  font=("times new roman", 15)).place(x=200, y=90, width=170,height=25)
        #roomno
        lbl_roomno = Label(root, text="Room No", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=120, width=170, height=25)

        Entry(root,textvariable=self.var_roomno, font=("times new roman", 15)).place(x=200, y=120, width=170, height=25)
        # Roomtype
        lbl_roomtype = Label(root, text="Room Type",font=("times new roman", 15), pady=-200, fg="black", bg="white",
                         bd=1, relief=RIDGE).place(x=20, y=160, width=170, height=25)

        Entry(root, textvariable=self.var_roomtype,font=("times new roman", 15)).place(x=200, y=160, width=170, height=25)
        #buttons
        btn_frame = Frame(root, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=350, height=40)
        btnadd = Button(btn_frame, command=self.add_data,text="ADD", font=("times new roman", 12, "bold"), bg="black",
                        fg="gold", width=8)
        btnadd.grid(row=0, column=0, padx=1)
        btnupdate = Button(btn_frame, command=self.update,text="UPDATE", font=("times new roman", 12, "bold"),
                           bg="black", fg="gold", width=8)
        btnupdate.grid(row=0, column=1, padx=1)
        btndel = Button(btn_frame,command=self.deleterrom,  text="DELETE", font=("times new roman", 12, "bold"),
                        bg="black", fg="gold", width=8)
        btndel.grid(row=0, column=2, padx=1)
        btnre = Button(btn_frame,command=self.reset, text="RESET", font=("times new roman", 12, "bold"), bg="black",
                       fg="gold", width=8)
        btnre.grid(row=0, column=3, padx=1)
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details ", padx=2,
                                 font=("times new roman", 15, "bold"))
        table_frame.place(x=600, y=55, width=600, height=280)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(table_frame, column=(
            "floor", "roomno", "roomtype",),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Roomno")
        self.room_table.heading("roomtype", text="Roomtype")


        self.room_table["show"] = "headings"
        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
     # add data

    def add_data(self):

        if self.var_floor.get() == "" or self.var_roomno.get() == "":
            messagebox.showerror("error", "all field are required", parent=self.root)
        else:
            try:
                # connecting to the database
                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                mycur.execute("insert into roomdetail values(%s,%s,%s)",
                              (str(self.var_floor.get()), str(self.var_roomno.get()), str(self.var_roomtype.get())))

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
        mycur.execute("select * from roomdetail")
        rows = mycur.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            db.commit()
            db.close()

        # get cursor
    def get_cursor(self, event=""):
        cur_row = self.room_table.focus()
        content = self.room_table.item(cur_row)
        row = content["values"]
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
    #update
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("error", "please enter floor no", parent=self.root)
        else:

            # connecting to the database
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            #mycur.execute("update roombook set checkin=%s,checkout=%s,roomtype=%s,availableroom=%s,meal=%s,noofday=%s where contact=%s",
                 #(str(self.var_checkin.get()), str(self.var_checkout.get()), str(self.var_roomtype.get()),
                 #str(self.var_roomavailable.get()), str(self.var_meal.get()), str(self.var_noofday.get()),
                 #str(self.var_contact.get())))
            mycur.execute("update roomdetail set floor=%s,roomtype=%s where roomno=%s",
                          (self.var_floor.get(),self.var_roomtype.get(),self.var_roomno.get()


            ))
            db.commit()
            self.fetch_data()
            db.close()
            messagebox.showinfo("success", "update successfully", parent=self.root)

    def deleterrom(self):
        deletebook = messagebox.askyesno("hotel managment", "r u really want ro cancle room", parent=self.root)
        if deletebook > 0:
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            query = "delete from roomdetail where roomno=%s"
            value = (self.var_roomno.get(),)
            mycur.execute(query, value)
        else:
            if not deletebook:
                return
        db.commit()
        self.fetch_data()
        db.close()

        # resset
    def reset(self):
        self.var_floor.set('')
        self.var_roomno.set('')
        self.var_roomtype.set('')



if __name__ == '__main__':
            root = Tk()
            obj = details(root)
            root.mainloop()
