import sys
from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import mysql.connector as mysql
from tkinter import messagebox

class bill:
    def __init__(self, win):
        self.win=win
        self.win.title("hotel managment system")
        self.win.geometry("1310x750+0+0")
        self.title_label = Label(self.win,text="billing",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        #=========variables============#

        bill_no = random.randint(100,9999)
        self.bill_no_tk = StringVar()
        self.bill_no_tk.set(bill_no)
        self.calc_var = StringVar()

        self.customer_nm = StringVar()
        self.customer_contact = StringVar()
        self.date_pr = StringVar()
        self.room_type = StringVar()
        self.room_qunty = StringVar()
        self.cost_c = StringVar()
        self.date_pr.set(datetime.now())

        total_list = []
        self.grd_total = 0



        #==============================#
        self.entry_frame = LabelFrame(self.win,text="Enter Details",background="lightgrey",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number ",font=('Arial',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.entry_frame,bd=5,textvariable=self.bill_no_tk,font=('Arial',15))
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name ",font=('Arial',15),bg="lightgrey")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=self.customer_nm,font=('Arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_con_lbl = Label(self.entry_frame,text="Customer Contact",font=('Arial',15),bg="lightgrey")
        self.cust_con_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.cust_con_ent = Entry(self.entry_frame,bd=5,textvariable=self.customer_contact,font=('Arial',15))
        self.cust_con_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl = Label(self.entry_frame,text="Date ",font=('Arial',15),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=self.date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.room_lbl = Label(self.entry_frame,text="Room Type ",font=('Arial',15),bg="lightgrey")
        self.room_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.room_ent = Entry(self.entry_frame,bd=5,textvariable=self.room_type,font=('Arial',15))
        self.room_ent.grid(row=4,column=1,padx=2,pady=2)

        self.roomqty_lbl = Label(self.entry_frame,text="Room Quantity ",font=('Arial',15),bg="lightgrey")
        self.roomqty_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.roomqty_ent = Entry(self.entry_frame,bd=5,textvariable=self.room_qunty,font=('Arial',15))
        self.roomqty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_lbl = Label(self.entry_frame,text="Cost Of One ",font=('Arial',15),bg="lightgrey")
        self.cost_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.cost_ent = Entry(self.entry_frame,bd=5,textvariable=self.cost_c,font=('Arial',15))
        self.cost_ent.grid(row=6,column=1,padx=2,pady=2)


    def default_bill(self):
            self.bill_txt.insert(END,"\t\t\t\tUrban Hotel")
            self.bill_txt.insert(END,"\n\t\t\t7 Street, Near RAilway Lines, Amreli")
            self.bill_txt.insert(END,"\n\t\t\t    Contact - +01122343255")
            self.bill_txt.insert(END,"\n==================================================================================")
            self.bill_txt.insert(END,f"\nBill Number {self.bill_no_tk.get()}")

    def getbill(self):

            self.bill_txt.insert(END,f"\nCustomer Name : {self.customer_nm.get()}")
            self.bill_txt.insert(END, f"\nCustomer Contact : {self.customer_contact.get()}")
            self.bill_txt.insert(END, f"\nDate : {self.date_pr.get()}")
            self.bill_txt.insert(END,"\n==================================================================================")
            self.bill_txt.insert(END,"\nRoom Type\t\tRoom Quantity\t\tPer Cost\t\tTotal")
            self.bill_txt.insert(END,"\n==================================================================================")

            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")


    def clear_fun(self):
            self.customer_nm.set("")
            self.customer_contact.set("")
            self.room_type.set("")
            self.room_qunty.set("")
            self.cost_c.set("")

    def reset_fun(self):
            self.total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            self.default_bill()

    def add_fun(self):
            if self.room_type.get() == "" or self.room_qunty.get() == "":
                messagebox.showerror("Error!","please enter  all the fields correctly.")
            else:
                try:
                    # connecting to the database
                    db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
                    mycur = db.cursor()
                    mycur.execute("insert into bill values(%s,%s,%s,%s,%s,%s,%s)",
                                  (str(self.bill_no_tk.get()), str(self.calc_var.get()), str(self.customer_nm.get()), str(self.customer_contact.get()), str(self.date_pr.get()), str(self.room_type.get()), str(self.room_qunty.get()), str(self.cost_c.get())))

                    db.commit()
                    self.fetch_data()
                    db.close()
                    messagebox.showinfo("success", "room added succesfully", parent=self.root)
                except Exception as es:
                    messagebox.showwarning("warning", f"something went wrong:{str(es)}", parent=self.root)

        # fetch data
    def total_fun(self):
            for item in self.total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n==================================================================================")
            self.bill_txt.insert(END,f"\n\t\t\t\t\tGrand Total :{self.grd_total}")
            self.bill_txt.insert(END,"\n==================================================================================")
            self.save_btn.config(state="normal")

    def save_func(self):
            admin = messagebox.askyesno("Confirm?",f"Do you want to save the bill {self.bill_no_tk.get()}")
            if admin > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                con = open(f"{sys.path[0]}/bills/"+str(self.bill_no_tk.get())+".txt","w")
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("successfully",f"Bill {self.bill_no_tk.get()} has been saved successfully",parent=self.win)
            else:
                return

        #================ BUtton ================

            self.button_frame = LabelFrame(self.entry_frame,bd=5,text="OPtions ",bg="lightgrey",font=("Arial",15))
            self.button_frame.place(x=20,y=270,width=390,height=300)

            self.add_btn = Button(self.button_frame,bd=3,text="Add",font=('Arial',12),width=12,height=3,command=add_fun)
            self.add_btn.grid(row=0,column=0,padx=4,pady=2)

            self.generate_btn = Button(self.button_frame,bd=3,text="Generate",font=('Arial',12),width=12,height=3,command=getbill)
            self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

            self.clear_btn = Button(self.button_frame,bd=3,text="Clear",font=('Arial',12),width=12,height=3,command=clear_fun)
            self.clear_btn.grid(row=0,column=2,padx=4,pady=2)

            self.total_btn = Button(self.button_frame,bd=3,text="Total",font=('Arial',12),width=12,height=3,command=total_fun)
            self.total_btn.grid(row=1,column=0,padx=4,pady=2)

            self.reset_btn = Button(self.button_frame,bd=3,text="Reset",font=('Arial',12),width=12,height=3,command=reset_fun)
            self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

            self.save_btn = Button(self.button_frame,bd=3,text="Save",font=('Arial',12),width=12,height=3,command=save_func)
            self.save_btn.grid(row=1,column=2,padx=4,pady=2)

            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")

    #===============================#

    def press_btn(self):
        text = self.widget.cget("text")

        #==============================#

        self.cal_frame = Frame(self.win,bd=5,background="black",relief=GROOVE)
        self.cal_frame.place(x=570,y=110,width=700,height=295)

        self.num_ent = Entry(self.cal_frame,bd=15,background="white",textvariable=None,font=('Arial',15),width=61,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=11)

    def press_btn(self):
            text = self.widget.cget("text")
            if text == "=":
                if self.calc_var.get().isdigit():
                    value = int(self.calc_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("error")
                self.calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                pass
            else:
                self.calc_var.set(self.calc_var.get() + text)
                self.num_ent.update()




            self.btn7 = Button(self.cal_frame,bg="orange",text="7",bd=7,width=13,height=1,font=('Arial',15))
            self.btn7.grid(row=1,column=0,padx=2,pady=2)
            self.btn7.bind("<Button-1>",self.press_btn)

            self.btn8 = Button(self.cal_frame, bg="orange", text="8", bd=8, width=13, height=1,font=('Arial',15))
            self.btn8.grid(row=1, column=1, padx=2, pady=2)
            self.btn8.bind("<Button-1>", self.press_btn)

            self.btn9 = Button(self.cal_frame, bg="orange", text="9", bd=8, width=13, height=1,font=('Arial',15))
            self.btn9.grid(row=1, column=2, padx=2, pady=2)
            self.btn9.bind("<Button-1>", self.press_btn)

            self.btnadd = Button(self.cal_frame, bg="orange", text="+", bd=8, width=13, height=1,font=('Arial',15))
            self.btnadd.grid(row=1, column=3, padx=2, pady=2)
            self.btnadd.bind("<Button-1>", self.press_btn)

            self.btn4 = Button(self.cal_frame,bg="orange",text="4",bd=4,width=13,height=1,font=('Arial',15))
            self.btn4.grid(row=2,column=0,padx=2,pady=2)
            self.btn4.bind("<Button-1>", self.press_btn)

            self.btn5 = Button(self.cal_frame, bg="orange", text="5", bd=8, width=13, height=1,font=('Arial',15))
            self.btn5.grid(row=2, column=1, padx=2, pady=2)
            self.btn5.bind("<Button-1>", self.press_btn)

            self.btn6 = Button(self.cal_frame, bg="orange", text="6", bd=8, width=13, height=1,font=('Arial',15))
            self.btn6.grid(row=2, column=2, padx=2, pady=2)
            self.btn6.bind("<Button-1>", self.press_btn)

            self.btnsub = Button(self.cal_frame, bg="orange", text="-", bd=8, width=13, height=1,font=('Arial',15))
            self.btnsub.grid(row=2, column=3, padx=2, pady=2)
            self.btnsub.bind("<Button-1>", self.press_btn)

            self.btn1 = Button(self.cal_frame,bg="orange",text="1",bd=7,width=13,height=1,font=('Arial',15))
            self.btn1.grid(row=3,column=0,padx=2,pady=2)
            self.btn1.bind("<Button-1>", self.press_btn)

            self.btn2 = Button(self.cal_frame, bg="orange", text="2", bd=8, width=13, height=1,font=('Arial',15))
            self.btn2.grid(row=3, column=1, padx=2, pady=2)
            self.btn2.bind("<Button-1>", self.press_btn)

            self.btn3 = Button(self.cal_frame, bg="orange", text="3", bd=8, width=13, height=1,font=('Arial',15))
            self.btn3.grid(row=3, column=2, padx=2, pady=2)
            self.btn3.bind("<Button-1>", self.press_btn)

            self.btnmul = Button(self.cal_frame, bg="orange", text="*", bd=8, width=13, height=1,font=('Arial',15))
            self.btnmul.grid(row=3, column=3, padx=2, pady=2)
            self.btnmul.bind("<Button-1>", self.press_btn)

            self.btn0 = Button(self.cal_frame,bg="orange",text="0",bd=7,width=13,height=1,font=('Arial',15))
            self.btn0.grid(row=4,column=0,padx=2,pady=2)
            self.btn0.bind("<Button-1>", self.press_btn)

            self.btnpoint = Button(self.cal_frame, bg="orange", text=".", bd=8, width=13, height=1,font=('Arial',15))
            self.btnpoint.grid(row=4, column=1, padx=2, pady=2)
            self.btnpoint.bind("<Button-1>", self.press_btn)

            self.btnclr = Button(self.cal_frame, bg="orange", text="=", bd=8, width=13, height=1,font=('Arial',15))
            self.btnclr.grid(row=4, column=2, padx=2, pady=2)
            self.btnclr.bind("<Button-1>", self.press_btn)

            self.btndiv = Button(self.cal_frame, bg="orange", text="/", bd=8, width=13, height=1,font=('Arial',15))
            self.btndiv.grid(row=4, column=3, padx=2, pady=2)
            self.btndiv.bind("<Button-1>", self.press_btn)


       #================biling========

            self.bill_frame =LabelFrame(self.win,text="Bill Area ",font=("Arial",18),background="lightgrey",bd=8,relief=GROOVE)
            self.bill_frame.place(x=570,y=420,width=700,height=295)


            self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
            self.bill_txt = Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
            self.y_scroll.config(command=self.bill_txt.yview)
            self.y_scroll.pack(side=RIGHT,fill=Y)
            self.bill_txt.pack(fill=BOTH,expand=TRUE)

            self.default_bill()

if __name__ == '__main__':
     win=Tk()
     obj=bill(win)
     win.mainloop()

