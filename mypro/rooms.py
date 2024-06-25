import random
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import LabelFrame
import mysql.connector
from time import strftime
from datetime import datetime
import tkinter as tk
from tkcalendar import dateentry, Calendar









class Roombooking:
    def __init__(self,root):
        self.root=root

        self.root.title("hotel managment system")
        self.root.geometry("1295x550+230+220")
        self.var_contact=StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofday= StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()


        # title
        title = Label(self.root, text="Room Booking Detail", font=("times new roman", 20, "bold"), fg="gold",
                      bg="black").place(x=0, y=0, width=1295, height=50)
        self.bg11 = ImageTk.PhotoImage(file="images/logo2.jpg")
        self.bg11_image = Label(self.root, image=self.bg11, bd=4, relief=RIDGE).place(x=0, y=0, width=100, height=40)
        lblframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking details",padx=2,font=("times new roman", 20, "bold"))
        lblframeleft.place(x=5,y=50,width=425,height=490)


        # labels and entry
        # lbl_cust_ref=Label(root,bd=2,relief=RIDGE,text="customer ref",padx=5,pady=7,font=("times new roman", 15, "bold")).place(x=5,y=50,width=425,height=490)
       # Label(root, text="").pack()
        lbl_con = Label(root, text="Customer Contact", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                         bd=1, relief=RIDGE).place(x=20, y=90, width=170, height=25)

        Entry(root,textvariable=self.var_contact,font=("times new roman", 15)).place(x=200, y=90 ,width=130, height=25)
        #fetch data button
        btnfetch = Button(lblframeleft,command=self.fetch_contact, text="Fetch Data",  font=("times new roman", 12, "bold"), bg="black",
                        fg="gold", width=8).place(x=340,y=4)






        #check in date
        lblcheckin = Label(root, text="Check_in Date", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                         bd=1, relief=RIDGE).place(x=20, y=130, width=170, height=25)

        checkin=Entry(root,relief=FLAT, textvariable=self.var_checkin,font=("times new roman", 15))
        checkin.place(x=200, y=130, width=170, height=25)
        




        # check out date
        lblcheckout = Label(root, text="Check_out Date", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                         bd=1, relief=RIDGE).place(x=20, y=170, width=170, height=25)

        Entry(root, textvariable=self.var_checkout,font=("times new roman", 15)).place(x=200, y=170, width=170, height=25)
        # room type
        lblroom = Label(root, text="Room Type", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                         bd=1, relief=RIDGE).place(x=20, y=210, width=170, height=25)
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select roomtype from roomdetail")
        rows = mycur.fetchall()
        combo = ttk.Combobox(root, textvariable=self.var_roomtype, font=("times new roman", 16), width=27)
        combo["value"] = rows
        combo.current(0)
        combo.place(x=200, y=210, width=170, height=25)
        # available room
        lblavailble = Label(root, text="Available Room", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                         bd=1, relief=RIDGE).place(x=20, y=250, width=170, height=25)
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select roomno from roomdetail")
        rows=mycur.fetchall()
        combo2 = ttk.Combobox(root, textvariable=self.var_roomavailable, font=("times new roman", 16), width=27)
        combo2["value"] =rows
        combo2.current(0)
        combo2.place(x=200, y=250, width=170, height=25)

        #Entry(root, textvariable=self.var_roomavailable,font=("times new roman", 15)).place(x=200, y=250, width=170, height=25)
        # Meal
        lblmeal = Label(root, text="Meal", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                         bd=1, relief=RIDGE).place(x=20, y=290, width=170, height=25)
        combo4 = ttk.Combobox(root, font=("times new roman", 15), textvariable=self.var_meal, width=27)
        combo4["value"] = ("breakfast", "dinner", "lunch")
        combo4.current(0)
        combo4.place(x=200, y=290, width=170, height=25)

        #no of days
        lblnodays = Label(root, text="No Of Days", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=330, width=170, height=25)

        Entry(root, textvariable=self.var_noofday,font=("times new roman", 15)).place(x=200, y=330, width=170, height=25)
        #paid tax
        lbltax = Label(root, text="Paid Tax", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=370, width=170, height=25)

        Entry(root,textvariable=self.var_paidtax, font=("times new roman", 15)).place(x=200, y=370, width=170, height=25)
        #sub total
        lbltotal = Label(root, text="Sub Total", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=410, width=170, height=25)

        Entry(root,textvariable=self.var_actualtotal ,font=("times new roman", 15)).place(x=200, y=410, width=170, height=25)
        #total cost
        lblcost = Label(root, text="Total Cost", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                        bd=1, relief=RIDGE).place(x=20, y=450, width=170, height=25)

        Entry(root, textvariable=self.var_total,font=("times new roman", 15)).place(x=200, y=450, width=170, height=25)


        #buttons
        btn_frame = Frame(root, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=490, width=430, height=40)
        # bill button
        btnbill = Button(btn_frame, command=self.total,text="BILL", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=8)
        btnbill.grid(row=0, column=0, padx=1)
        btnadd = Button(btn_frame,command=self.add_data, text="ADD",  font=("times new roman", 12, "bold"), bg="black",fg="gold", width=8)
        btnadd.grid(row=0, column=1, padx=1)
        btnupdate = Button(btn_frame, command=self.update, text="UPDATE", font=("times new roman", 12, "bold"),bg="black", fg="gold", width=8)
        btnupdate.grid(row=0, column=2, padx=1)
        btndel = Button(btn_frame, command=self.deletebook,  text="DELETE", font=("times new roman", 12, "bold"),bg="black", fg="gold", width=8)
        btndel.grid(row=0, column=3, padx=1)
        btnre = Button(btn_frame,  command=self.reset,text="RESET", font=("times new roman", 12, "bold"), bg="black",fg="gold", width=8)
        btnre.grid(row=0, column=4, padx=1)
        #image
        self.bg11 = ImageTk.PhotoImage(file="images/img4.jpg")

        self.bg11_image = Label(self.root, image=self.bg11, bd=4, relief=RIDGE).place(x=760, y=55, width=350, height=190)
        # TABLE FRAME search system
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System ", padx=2,font=("times new roman", 15, "bold"))
        table_frame.place(x=435, y=280, width=860, height=260)
        lblsaerch = Label(table_frame, text="Search By", font=("times new roman", 15, "bold"), bg="red", fg="white", width=8)
        lblsaerch.grid(row=0, column=0, padx=1, sticky=W)
        self.search_var = StringVar()
        combosearch = ttk.Combobox(table_frame, textvariable=self.search_var, font=("times new roman", 12), width=20,state="readonly")
        combosearch["value"] = ("Contact", "Room")
        combosearch.current(0)
        combosearch.grid(row=0, column=1)
        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame, textvariable=self.txt_search, font=("arial", 12, "bold"), width=20)
        txtsearch.grid(row=0, column=2)

        btnsearch = Button(table_frame, command=self.searchrec, text="Search", font=("times new roman", 12, "bold"),bg="black", fg="gold", width=8)
        btnsearch.grid(row=0, column=3, padx=1)
        btnshow = Button(table_frame, command=self.fetch_data,text="Show all",  font=("times new roman", 12, "bold"), bg="black", fg="gold",width=8)
        btnshow.grid(row=0, column=4, padx=1)


        # shoe data table
        deatilframe = Frame(table_frame, bd=2, relief=RIDGE)
        deatilframe.place(x=0, y=50, width=860, height=180)
        scroll_x = ttk.Scrollbar(deatilframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(deatilframe, orient=VERTICAL)
        self.room_table = ttk.Treeview(deatilframe, column=(
        "contact", "checkin", "checkout", "roomavailable", "roomtype", "meal", "noofdays",),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomavailable", text="Room no")
        self.room_table.heading("roomtype", text="Room type")
        self.room_table.heading("meal", text="meal")
        self.room_table.heading("noofdays", text="No of days")

        self.room_table["show"] = "headings"
        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    #add data
    def add_data(self):

        if self.var_contact.get()=="" or self.var_checkin.get()=="":
                messagebox.showerror("error","all field are required",parent=self.root)
        else:
            try:
                # connecting to the database
                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                mycur.execute("insert into roombook values(%s,%s,%s,%s,%s,%s,%s)",
                     (str(self.var_contact.get()), str(self.var_checkin.get()), str(self.var_checkout.get()),
                      str(self.var_roomavailable.get()),str(self.var_roomtype.get()),  str(self.var_meal.get()),
                      str(self.var_noofday.get())))

                db.commit()
                self.fetch_data()
                db.close()
                messagebox.showinfo("success","booking succesfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
            # connecting to the database
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select * from roombook")
        rows = mycur.fetchall()
        if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("", END, values=i)
                db.commit()
                db.close()
    #get cursor
    def get_cursor(self, event=""):
        cur_row = self.room_table.focus()
        content = self.room_table.item(cur_row)
        row = content["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])

        self.var_roomavailable.set(row[3])
        self.var_roomtype.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofday.set(row[6])
    #update

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("error", "please enter Contact no", parent=self.root)
        else:

            # connecting to the database
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            #mycur.execute("update roombook set checkin=%s,checkout=%s,roomtype=%s,availableroom=%s,meal=%s,noofday=%s where contact=%s",
                 #(str(self.var_checkin.get()), str(self.var_checkout.get()), str(self.var_roomtype.get()),
                 #str(self.var_roomavailable.get()), str(self.var_meal.get()), str(self.var_noofday.get()),
                 #str(self.var_contact.get())))
            mycur.execute("update roombook set checkin=%s,checkout=%s,roomtype=%s,meal=%s,noofday=%s where contact=%s",
                          (self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),
                           self.var_meal.get(),self.var_noofday.get(),self.var_contact.get()

            ))

        db.commit()
        self.fetch_data()
        db.close()
        messagebox.showinfo("success", "update successfully", parent=self.root)
    def deletebook(self):
        deletebook=messagebox.askyesno("hotel managment","r u really want ro cancle booking",parent=self.root)
        if deletebook>0:
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            query="delete from roombook where contact=%s"
            value=(self.var_contact.get(),)
            mycur.execute(query,value)
        else:
            if not deletebook:
                return
        db.commit()
        self.fetch_data()
        db.close()

    #resset
    def reset(self):
        self.var_contact.set('')
        self.var_checkin.set('')
        self.var_checkout.set('')
        self.var_roomtype.set('')
        self.var_roomavailable.set('')
        self.var_meal.set('')
        self.var_noofday.set('')
        self.var_paidtax.set('')
        self.var_actualtotal.set('')
        self.var_total.set('')



















        #all data fetch


    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter valid contact",parent=self.root)
        else:
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            mycur.execute(query,value)
            row=mycur.fetchone()

            if row==None:
                messagebox.showerror("error","this number not found",parent=self.root)
            else:
                db.commit()
                db.close()
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)
                lblname=Label(showDataFrame,text="Name:",font=("arial",12))
                lblname.place(x=0,y=0)
                lbl=Label(showDataFrame,text=row,font=("arial",12))
                lbl.place(x=90,y=0)

                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                query = ("select gender from customer where mobile=%s")
                value = (self.var_contact.get(),)
                mycur.execute(query, value)
                row = mycur.fetchone()
                lblgender = Label(showDataFrame, text="Gender:", font=("arial", 12))
                lblgender.place(x=0, y=30)
                lbl2 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl2.place(x=90, y=30)

                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                query = ("select email from customer where mobile=%s")
                value = (self.var_contact.get(),)
                mycur.execute(query, value)
                row = mycur.fetchone()
                lblemail = Label(showDataFrame, text="Email:", font=("arial", 12))
                lblemail.place(x=0, y=60)
                lbl3 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl3.place(x=90, y=60)

                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                query = ("select nationality from customer where mobile=%s")
                value = (self.var_contact.get(),)
                mycur.execute(query, value)
                row = mycur.fetchone()
                lblnationality = Label(showDataFrame, text="Nationality:", font=("arial", 12))
                lblnationality.place(x=0, y=90)
                lbl4 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl4.place(x=90, y=90)

                db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                mycur = db.cursor()
                query = ("select address from customer where mobile=%s")
                value = (self.var_contact.get(),)
                mycur.execute(query, value)
                row = mycur.fetchone()
                lbladdress = Label(showDataFrame, text="Address:", font=("arial", 12))
                lbladdress.place(x=0, y=120)
                lbl5= Label(showDataFrame, text=row, font=("arial", 12))
                lbl5.place(x=90, y=120)
     #searchg system
    def searchrec(self):
        # connecting to the database
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select * from roombook where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=mycur.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            db.commit()
            db.close()
        # get the selected date when the user closes the caleder




    #datetim
    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_noofday.set(abs(outdate-indate).days)
        if (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="luxury"):
            q1=float(300)#breakfast
            q2=float(1000)#luxury
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)#300+1000
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        if (self.var_meal.get() == "lunch" and self.var_roomtype.get() == "single"):
            q1 = (300)
            q2 = (700)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "breakfast" and self.var_roomtype.get() == "duplex"):
            q1 = (500)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "breakfast" and self.var_roomtype.get() == "double"):
            q1 = (500)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "dinner" and self.var_roomtype.get() == "double"):
            q1 = (400)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "dinner" and self.var_roomtype.get() == "luxury"):
            q1 = (600)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "lunch" and self.var_roomtype.get() == "luxury"):
            q1 = (400)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "dinner" and self.var_roomtype.get() == "single"):
            q1 = (400)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "breakfast" and self.var_roomtype.get() == "single"):
            q1 = (400)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        elif (self.var_meal.get() == "lunch" and self.var_roomtype.get() == "double"):
            q1 = (400)
            q2 = (1000)
            q3 = float(self.var_noofday.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            st = "Rs." + str("%.2f" % ((q5)))
            tt = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)


if __name__ == '__main__':
    root = Tk()
    obj=Roombooking(root)
    root.mainloop()