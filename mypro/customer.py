import random
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import LabelFrame
import mysql.connector
#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="hoteldb")
mycur = db.cursor()

class cust_win:
    def __init__(self,root):
        self.root=root

        self.root.title("hotel managment system")
        self.root.geometry("1295x550+230+220")
        #variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_postcode=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
#title
        title = Label(self.root, text="Add Customer Detail", font=("times new roman", 20, "bold"), fg="gold", bg="black").place(x=0, y=0,width=1295,height=50)
        self.bg11 = ImageTk.PhotoImage(file="images/logo2.jpg")
        self.bg11_image = Label(self.root, image=self.bg11, bd=4, relief=RIDGE).place(x=0, y=0, width=100, height=40)
#label
        lblframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer details",padx=2,font=("times new roman", 20, "bold")).place(x=5,y=50,width=425,height=490)
        #labels and entry
       # lbl_cust_ref=Label(root,bd=2,relief=RIDGE,text="customer ref",padx=5,pady=7,font=("times new roman", 15, "bold")).place(x=5,y=50,width=425,height=490)
        Label(root, text="").pack()
        lbl_menu = Label(root, text="customer ref", font=("times new roman", 15), pady=-200, fg="black", bg="white",bd=1,relief=RIDGE).place( x=20,y=90,width=170,height=25)
        ref_varify = StringVar()
        Entry(root, textvariable=self.var_ref,state="readonly").place(x=200,y=90,width=170,height=25)

        #cust_name
        lbl_menu1 = Label(root, text="customer name", font=("times new roman", 15), pady=-200, fg="black", bg="white",bd=1, relief=RIDGE).place(x=20, y=130, width=170, height=25)
        Label(root, text="").pack()
        username_varify = StringVar()
        Entry(root, textvariable=self.var_name).place(x=200, y=130, width=170, height=25)

        # cust_gen
        lbl_menu2 = Label(root, text="Gender", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=170, width=170, height=25)
        Label(root, text="").pack()
        combo=ttk.Combobox(root,font=("times new roman", 15,),textvariable=self.var_gender,width=27)
        combo["value"]=("male","female","others")
        combo.current(0)
        combo.place(x=200, y=170, width=170, height=25)
        # cust_postcode
        lbl_menu3 = Label(root, text="PostCode ", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=210, width=170, height=25)
        Label(root, text="").pack()

        Entry(root, textvariable=self.var_postcode).place(x=200, y=210, width=170, height=25)
        # cust_Address
        lbl_menu4 = Label(root, text="Address ", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=250, width=170, height=25)
        Label(root, text="").pack()

        Entry(root, textvariable=self.var_address).place(x=200, y=250, width=170, height=25)
        #nationality
        lbl_menu5 = Label(root, text="Nationality", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=290, width=170, height=25)
        Label(root, text="").pack()
        combo1 = ttk.Combobox(root,font=("times new roman", 15),textvariable=self.var_nationality, width=27)
        combo1["value"] = ("India","Uk","USA","Dubai")
        combo1.current(0)
        combo1.place(x=200, y=290, width=170, height=25)
        #mobile
        lbl_menu6 = Label(root, text="Mobile ", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=330, width=170, height=25)
        Label(root, text="").pack()

        Entry(root, textvariable=self.var_mobile).place(x=200, y=330, width=170, height=25)
        # email
        lbl_menu7 = Label(root, text="Email ", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=370, width=170, height=25)
        Label(root, text="").pack()

        Entry(root, textvariable=self.var_email).place(x=200, y=370, width=170, height=25)
        # idprrof
        lbl_menu8 = Label(root, text="Id Proof Type", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=410, width=170, height=25)
        Label(root, text="").pack()
        combo4 = ttk.Combobox(root,font=("times new roman", 15),textvariable=self.var_idproof, width=27)
        combo4["value"] = ("Aadhar Card","Driving licence","passpirt")
        combo4.current(0)
        combo4.place(x=200, y=410, width=170, height=25)
        lbl_menu9 = Label(root, text="Id Number ", font=("times new roman", 15), pady=-200, fg="black", bg="white",
                          bd=1, relief=RIDGE).place(x=20, y=450, width=170, height=25)
        Label(root, text="").pack()

        Entry(root, textvariable=self.var_idnumber).place(x=200, y=450, width=170, height=25)

        btn_frame=Frame(root,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=490,width=370,height=40)
        btnadd=Button(btn_frame,text="ADD",command=self.add_data, font=("times new roman", 12,"bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=0,padx=1)
        btnupdate = Button(btn_frame, command=self.update,text="UPDATE", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=8)
        btnupdate.grid(row=0, column=1,padx=1)
        btndel = Button(btn_frame, command=self.deletem,text="DELETE", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=8)
        btndel.grid(row=0, column=2,padx=1)
        btnre = Button(btn_frame, command=self.reset,text="RESET", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=8)
        btnre.grid(row=0, column=3,padx=1)
        #TABLE FRAME search
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System ",padx=2,font=("times new roman", 15, "bold"))
        table_frame.place(x=435,y=50,width=860,height=490)
        lblsaerch = Label(table_frame, text="Search By", font=("times new roman", 15, "bold"), bg="red", fg="white", width=8)
        lblsaerch.grid(row=0, column=0, padx=1,sticky=W)
        self.search_var=StringVar()
        combosearch = ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman", 12), width=20,state="readonly")
        combosearch["value"] = ("mobile","ref")
        combosearch.current(0)
        combosearch.grid(row=0,column=1)
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",12,"bold"),width=20)
        txtsearch.grid(row=0,column=2)

        btnsearch = Button(table_frame,command=self.search, text="Search", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=8)
        btnsearch.grid(row=0, column=3, padx=1)
        btnshow = Button(table_frame, text="Show all",command=self.fetch_data, font=("times new roman", 12, "bold"), bg="black", fg="gold",
                           width=8)
        btnshow.grid(row=0, column=4, padx=1)
        #shoe data table
        deatilframe = Frame(table_frame,bd=2, relief=RIDGE)
        deatilframe.place(x=0, y=50, width=860, height=350)
        scroll_x=ttk.Scrollbar(deatilframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(deatilframe,orient=VERTICAL)
        self.cust_details_tbl=ttk.Treeview(deatilframe,column=("ref","name","gender","postcode","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_details_tbl.xview)
        scroll_y.config(command=self.cust_details_tbl.yview)

        self.cust_details_tbl.heading("ref",text="refer no")
        self.cust_details_tbl.heading("name",text="name")
        self.cust_details_tbl.heading("gender",text=" gender")
        self.cust_details_tbl.heading("postcode",text="postcode")
        self.cust_details_tbl.heading("mobile",text="mobile")
        self.cust_details_tbl.heading("email",text="email")
        self.cust_details_tbl.heading("nationality",text="nationality")
        self.cust_details_tbl.heading("idproof",text="idproof")
        self.cust_details_tbl.heading("idnumber",text="idnumber")
        self.cust_details_tbl.heading("address",text="address")
        self.cust_details_tbl["show"]="headings"
        self.cust_details_tbl.column("ref",width=100)
        self.cust_details_tbl.column("name", width=100)
        self.cust_details_tbl.column("gender", width=100)
        self.cust_details_tbl.column("postcode", width=100)
        self.cust_details_tbl.column("mobile", width=100)
        self.cust_details_tbl.column("email", width=100)
        self.cust_details_tbl.column("nationality", width=100)
        self.cust_details_tbl.column("idproof", width=100)
        self.cust_details_tbl.column("idnumber", width=100)
        self.cust_details_tbl.column("address", width=100)
        self.cust_details_tbl.pack(fill=BOTH,expand=1)
        self.cust_details_tbl.bind("<ButtonRelease-1>",self.fetch_data1)
        self.fetch_data()
    def add_data(self):
        # connecting to the database
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()

        if self.var_mobile.get == "" or self.var_name.get() == "" or self.var_address.get() == "" or self.var_gender.get == "":
            messagebox.showerror("Please complete the required field!", "Please complete the required field!")
        else:

            m=mycur.execute("INSERT INTO `customer`(`ref`, `name`, `gender`, `postcode`, `mobile`, `email`, `nationality`, `idproof`, `idnumber`,`address`)"
                           " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (str(self.var_ref.get()),str(self.var_name.get()), str(self.var_gender.get()),
                            str(self.var_postcode.get()),str(self.var_mobile.get()), str(self.var_email.get()),str(self.var_nationality.get()),
                            str(self.var_idproof.get()),str(self.var_idnumber.get()),str(self.var_address.get())))
            db.commit()
            self.fetch_data()
            self.var_ref.set("")
            self.var_name.set("")
            self.var_gender.set("")
            self.var_postcode.set("")
            self.var_mobile.set("")
            self.var_email.set("")
            self.var_nationality.set("")
            self.var_idproof.set("")
            self.var_idnumber.set("")
            self.var_address.set("")
            messagebox.showinfo("Successfully Created!", "customer has been added")
            mycur.close()
            mycur.close()
    def fetch_data(self):
    # connecting to the database
     db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
     mycur = db.cursor()
     mycur.execute("select * from customer")
     rows=mycur.fetchall()
     if len(rows)!=0:
         self.cust_details_tbl.delete(*self.cust_details_tbl.get_children())
         for i in rows:
             self.cust_details_tbl.insert("",END,values=i)
         db.commit()
         db.close()

    def fetch_data1(self,event=""):
         cur_row=self.cust_details_tbl.focus()
         content=self.cust_details_tbl.item(cur_row)
         row=content["values"]
         self.var_ref.set(row[0])
         self.var_name.set(row[1])
         self.var_gender.set(row[2])
         self.var_postcode.set(row[3])
         self.var_mobile.set(row[4])
         self.var_email.set(row[5])
         self.var_nationality.set(row[6])
         self.var_idproof.set(row[7])
         self.var_idnumber.set(row[8])
         self.var_address.set(row[9])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("error","please enter mobile no",parent=self.root)
        else:


        # connecting to the database
         db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
         mycur = db.cursor()
         mycur.execute("update customer set name=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",
                            (str(self.var_name.get()), str(self.var_gender.get()),str(self.var_postcode.get()),str(self.var_mobile.get()), str(self.var_email.get()),str(self.var_nationality.get()),str(self.var_idproof.get()),str(self.var_idnumber.get()),str(self.var_address.get()),str(self.var_ref.get())))

        db.commit()
        self.fetch_data()
        db.close()
        messagebox.showinfo("success","update successfully",parent=self.root)
    
    def deletem(self):
        deletem=messagebox.askyesno("hotel managment system","do you want to delete this customer",parent=self.root)
        if deletem>0:
            # connecting to the database
            db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
            mycur = db.cursor()
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            mycur.execute(query,value)
        else:
            if not deletem:
                return 
        db.commit()
        self.fetch_data()
        db.close()
    def reset(self):
        self.var_ref.set('')
        self.var_name.set('')
        self.var_gender.set('')
        self.var_postcode.set('')
        self.var_mobile.set('')
        self.var_email.set('')
        self.var_nationality.set('')
        self.var_idproof.set('')
        self.var_idnumber.set('')
        self.var_address.set('')
    def search(self):
        # connecting to the database
        db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hoteldb")
        mycur = db.cursor()
        mycur.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=mycur.fetchall()
        if len(rows)!=0:
            self.cust_details_tbl.delete(*self.cust_details_tbl.get_children())
            for i in rows:
                self.cust_details_tbl.insert("",END,values=i)
            db.commit()
            db.close()



        







if __name__ == '__main__':
    root = Tk()
    obj=cust_win(root)
    root.mainloop()
