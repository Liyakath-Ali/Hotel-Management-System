from tkinter import *
from PIL import Image,ImageTk
from Customer import cust_win
from Room_123 import Roombooking


class hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #============1st image==================
        img1=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\hotel1.png') #opening image from local storage
        img1=img1.resize((1550,140)) #resizes the length,breadth of image
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE) #image1 initialization
        lblimg.place(x=0,y=0,width=1550,height=140) #image1 geometry

        #=================LOGO====================
        img2=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\logohotel.png')
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #=================TITLE===================
        lbl_title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=('Arial',36,'bold'),bg='black',fg='Purple',bd=4)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        #===============MAIN FRAME================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #==============MENU=======================
        lbl_menu=Label(main_frame,text='MENU',font=('Arial',20,'bold'),bg='black',fg='Blue',bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #==============BUTTON FRAME===============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=230)

        cust_btn=Button(btn_frame,text='CUSTOMER',command=self.cust_details,width=19,font=('Arial',14,'bold'),bg='black',fg='Blue',bd=4,cursor='hand2',relief=RIDGE)
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text='ROOM',width=19,command=self.roombooking,font=('Arial',14,'bold'),bg='black',fg='Blue',bd=4,cursor='hand2',relief=RIDGE)
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text='DETAILS',width=19,font=('Arial',14,'bold'),bg='black',fg='Blue',bd=4,cursor='hand2',relief=RIDGE)
        details_btn.grid(row=3,column=0,pady=1)

        report_btn=Button(btn_frame,text='REPORT',width=19,font=('Arial',14,'bold'),bg='black',fg='Blue',bd=4,cursor='hand2',relief=RIDGE)
        report_btn.grid(row=4,column=0,pady=1)

        logout_btn=Button(btn_frame,text='LOGOUT',width=19,font=('Arial',14,'bold'),bg='black',fg='Blue',bd=4,cursor='hand2',relief=RIDGE)
        logout_btn.grid(row=5,column=0,pady=1)


        #==========RIGHT SIDE IMAGE================

        img3=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\slide3.jpg')
        img3=img3.resize((1310,590))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=230,y=0,width=1310,height=590)

        #==========DOWN IMAGES===================
        img4=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\myh.jpg')
        img4=img4.resize((230,170))
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=260,width=230,height=170)

        img5=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\khana.jpg')
        img5=img5.resize((230,190))
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
    

        
if __name__=="__main__":
    root=Tk()
    obj=hotelmanagementsystem(root)
    root.mainloop()
