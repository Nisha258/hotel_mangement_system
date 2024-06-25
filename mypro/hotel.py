from tkinter import*
from PIL import Image,ImageTk
from customer import cust_win
from customer import*
from rooms import*
from details import*
from employe import*
#from login import*
from empdetail import*
from bill1 import*
class hotelman:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel managment system")
        self.root.geometry("1550x800+0+0")
        self.bg = ImageTk.PhotoImage(file="images/7.jpg")
        self.bg_image = Label(self.root, image=self.bg,bd=4,relief=RIDGE).place(x=0,y=0,width=1550,height=140)
        self.bg1 = ImageTk.PhotoImage(file="images/logo2.jpg")

        self.bg1_image = Label(self.root, image=self.bg1, bd=4, relief=RIDGE).place(x=0, y=0, width=230,  height=140)
        # title
#title
        title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), fg="gold", bg="black",bd=1,relief=RIDGE).place( x=0, y=140,width=1550,height=50)
#main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

#menu
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), fg="gold", bg="black",bd=4,relief=RIDGE).place( x=0, y=0,width=230)

#button frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=290)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cus_detail,width=22,font=("times new roman", 14, "bold"), fg="gold", bg="black",bd=0,relief=RIDGE,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOMS", command=self.roombook,width=22, font=("times new roman", 14, "bold"), fg="gold",bg="black", bd=0,relief=RIDGE, cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        detail_btn = Button(btn_frame, text="DETAILS", width=22,command=self.details_room, font=("times new roman", 14, "bold"), fg="gold",bg="black", bd=0,relief=RIDGE, cursor="hand1")
        detail_btn.grid(row=2, column=0, pady=1)
        empdetail = Button(btn_frame, text="EMPLOYEES Detail", command=self.emp1, width=22,
                         font=("times new roman", 14, "bold"), fg="gold", bg="black", bd=0, relief=RIDGE,
                         cursor="hand1")
        empdetail.grid(row=3,column=0,pady=1)

        Employes = Button(btn_frame, text="EMPLOYEES", command=self.emp,width=22, font=("times new roman", 14, "bold"), fg="gold",bg="black", bd=0, relief=RIDGE,cursor="hand1")
        Employes.grid(row=4,column=0,pady=1)
        Billing = Button(btn_frame, text="BILLING", command=self.bill1, width=22,
                          font=("times new roman", 14, "bold"), fg="gold", bg="black", bd=0, relief=RIDGE,
                          cursor="hand1")
        Billing.grid(row=5,column=0,pady=1)
        logout1 = Button(btn_frame, text="LogOut", command=self.logout, width=22,
                         font=("times new roman", 14, "bold"), fg="gold", bg="black", bd=0, relief=RIDGE,
                         cursor="hand1")
        logout1.grid(row=6,column=0,pady=1)



        #right side image
        self.rg = ImageTk.PhotoImage(file="images/7.jpg")
        self.rg_image = Label(main_frame, image=self.rg, bd=4, relief=RIDGE).place(x=225, y=0, width=1310, height=590)
        self.sg = ImageTk.PhotoImage(file="images/food.jpg")
        self.sg_image = Label(main_frame, image=self.sg, bd=4, relief=RIDGE).place(x=0, y=300, width=230, height=290)



    def cus_detail(self):
         self.new_window=Toplevel(self.root)
         self.app=cust_win(self.new_window)

    def roombook(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = details(self.new_window)

    def emp1(self):
        self.new_window = Toplevel(self.root)
        self.app = empdetails(self.new_window)
    def emp(self):
        self.new_window=Toplevel(self.root)
        self.app=Employe(self.new_window)

    def bill1(self):
        self.new_window = Toplevel(self.root)
        self.app = bill(self.new_window)
    def logout(self):
        self.root.destroy()
        






if __name__ == '__main__':
     root=Tk()
     obj=hotelman(root)
     root.mainloop()