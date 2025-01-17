from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room booking")
        self.root.geometry("1310x550+230+220")


        #============VARIABLES========================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()



        #==============TITLE==========================
        lbl_title=Label(self.root,text='ROOM BOOKING DETAILS',font=('Arial',18,'bold'),bg='black',fg='Purple',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #==============LOGO===========================
        img2=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\logohotel.png')
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=4,width=100,height=40)

        #============LABEL FRAME=======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room booking details",padx=2,font=('Arial',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #============LABEL ENTRYS======================
        #customer number
        lbl_cust_contact=Label(labelframeleft,text="Customer contact",font=('Arial',12,'bold'),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=('Arial',13,'bold'))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch-data button
        fetch_data_btn=Button(labelframeleft,text='Fetch data',command=self.Fetch_contact,width=8,font=('Arial',8,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        fetch_data_btn.place(x=347,y=4)

        #check-in Date
        check_in_Date=Label(labelframeleft,text="Check-in Date:",font=('Arial',12,'bold'),padx=2,pady=6)
        check_in_Date.grid(row=1,column=0,sticky=W)
        txtcheck_in_Date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=('Arial',13,'bold'))
        txtcheck_in_Date.grid(row=1,column=1)

        #check-out Date
        check_out_Date=Label(labelframeleft,text="Check-out Date:",font=('Arial',12,'bold'),padx=2,pady=6)
        check_out_Date.grid(row=2,column=0,sticky=W)
        txtcheck_out_Date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=('Arial',13,'bold'))
        txtcheck_out_Date.grid(row=2,column=1)

        #rrom type
        label_roomtype=Label(labelframeleft,text="Room type",font=('Arial',12,'bold'),padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=('Arial',12,'bold'),width=27,state='readonly')
        combo_roomtype['value']=('Single','Double','Luxury')
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        #Available room
        lblRoomAvail=Label(labelframeleft,text="Available room",font=('Arial',12,'bold'),padx=2,pady=6)
        lblRoomAvail.grid(row=4,column=0,sticky=W)
        entry_RoomAvail=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=('Arial',13,'bold'))
        entry_RoomAvail.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,text="Meal",font=('Arial',12,'bold'),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        combo_meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=('Arial',12,'bold'),width=27,state='readonly')
        combo_meal['value']=('BreakFast','Lunch','Dinner','All')
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)

        #No of days
        lbldays=Label(labelframeleft,text="No of days:",font=('Arial',12,'bold'),padx=2,pady=6)
        lbldays.grid(row=6,column=0,sticky=W)
        entry_days=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=('Arial',13,'bold'))
        entry_days.grid(row=6,column=1)

        #paid tax
        lblptax=Label(labelframeleft,text="Paid Tax:",font=('Arial',12,'bold'),padx=2,pady=6)
        lblptax.grid(row=7,column=0,sticky=W)
        entry_ptax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=('Arial',13,'bold'))
        entry_ptax.grid(row=7,column=1)

        #Sub total
        lblstotal=Label(labelframeleft,text="Sub Total",font=('Arial',12,'bold'),padx=2,pady=6)
        lblstotal.grid(row=8,column=0,sticky=W)
        entry_stotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=('Arial',13,'bold'))
        entry_stotal.grid(row=8,column=1)

        #Total cost
        lblcost=Label(labelframeleft,text="Total Cost:",font=('Arial',12,'bold'),padx=2,pady=6)
        lblcost.grid(row=9,column=0,sticky=W)
        entry_cost=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=('Arial',13,'bold'))
        entry_cost.grid(row=9,column=1)

        #==============Bill button=============
        bill_btn=Button(labelframeleft,text='Bill',command=self.total,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        bill_btn.grid(row=10,column=0,padx=1,sticky=W)

        #====================buttons====================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        add_btn=Button(btn_frame,text='ADD',command=self.add_data,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        add_btn.grid(row=0,column=0,padx=1)

        upd_btn=Button(btn_frame,text='UPDATE',command=self.update,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        upd_btn.grid(row=0,column=1,padx=1)

        del_btn=Button(btn_frame,text='DELETE',command=self.mDelete,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        del_btn.grid(row=0,column=2,padx=1)
        
        res_btn=Button(btn_frame,text='RESET',command=self.reset,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        res_btn.grid(row=0,column=3,padx=1)

        #===============RIGHT SIDE IMAGE=============================
        img3=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\bed.jpg')
        img3=img3.resize((520,300))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)
        
        #============TABLE FRAME SEARCH SYSTEM=======================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search system",font=('Arial',12,'bold'))
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblsearchby=Label(Table_frame,text="Search by:",font=('Arial',12,'bold'),bg='red',fg='White')
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=('Arial',12,'bold'),width=24,state='readonly')
        combo_search['value']=('Contact','Room')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=('Arial',13,'bold'))
        txtsearch.grid(row=0,column=2,padx=2)

        search_btn=Button(Table_frame,text='Search',command=self.search,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        search_btn.grid(row=0,column=3,padx=1)

        Sall_btn=Button(Table_frame,text='Search all',command=self.fetch_data,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        Sall_btn.grid(row=0,column=4,padx=1)
        

        #===============Show data table================

        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=('contact','check-in','check-out','roomtype','roomavailable',
                                        'meal','noofdays'))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading('contact',text='Mobile')
        self.room_table.heading('check-in',text='Check-in-date')
        self.room_table.heading('check-out',text='Check-out-date')
        self.room_table.heading('roomtype',text='Room Type')
        self.room_table.heading('roomavailable',text='Room no')
        self.room_table.heading('meal',text='Meal')
        self.room_table.heading('noofdays',text='No of Days')


        self.room_table['show']='headings'


        self.room_table.column("contact",width=100)
        self.room_table.column("check-in",width=100)
        self.room_table.column("check-out",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()   

    # add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                      self.var_contact.get(),
                                                                      self.var_checkin.get(),
                                                                      self.var_checkout.get(),
                                                                      self.var_roomtype.get(),
                                                                      self.var_roomavailable.get(),
                                                                      self.var_meal.get(),
                                                                      self.var_noofdays.get()
                                                                      ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()             

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content['values']

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    #update
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,room=%s,meal=%s,noofdays=%s where Contact=%s",(
                                                                                                                          self.var_checkin.get(),
                                                                                                                          self.var_checkout.get(),
                                                                                                                          self.var_roomtype.get(),
                                                                                                                          self.var_roomavailable.get(),
                                                                                                                          self.var_meal.get(),
                                                                                                                          self.var_noofdays.get(),
                                                                                                                          self.var_contact.get()
                                                                                                                         ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
    
    #delete
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
            my_cursor=conn.cursor()
            query="Delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 
    #reset
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax=(""),
        self.var_actualtotal=(""),
        self.var_total=("")
        
    #========================ALL DATA FETCH==============================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
            my_cursor=conn.cursor() 
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)

            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                #=====================Name=================================
                lblName=Label(showDataframe,text="Name:",font=('Arial',12,'bold'))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=('Arial',12,'bold'))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor() 
                query=("select Name from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()    
                 
                #===================Gender=================================
                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor() 
                query=("select gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()  

                lblGender=Label(showDataframe,text="Gender:",font=('Arial',12,'bold'))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=('Arial',12,'bold'))
                lbl2.place(x=90,y=30)

                #===================EMAIL=================================
                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor() 
                query=("select email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()  

                lblGender=Label(showDataframe,text="Email:",font=('Arial',12,'bold'))
                lblGender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=('Arial',12,'bold'))
                lbl2.place(x=90,y=60)

                #===================NATIONALITY=================================
                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor() 
                query=("select nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()  

                lblGender=Label(showDataframe,text="Email:",font=('Arial',12,'bold'))
                lblGender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=('Arial',12,'bold'))
                lbl2.place(x=90,y=90)


                #===================ADDRESS=================================
                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor() 
                query=("select address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()  

                lblGender=Label(showDataframe,text="Address:",font=('Arial',12,'bold'))
                lblGender.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=('Arial',12,'bold'))
                lbl2.place(x=90,y=120)

    #calculate no of days
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_roomtype.get()=='Single'):
            if(self.var_meal.get()=='BreakFast'):
                q11=float(200) #brakfast price
                q12=float(300) #single price
                q13=float(self.var_noofdays.get())
                q14=float(q11+q12)
                q15=float(q13*q14)
                Tax="Rs."+str("%.2f"%((q15)*0.1))
                ST="Rs."+str('%.2f'%((q15)))
                TT="Rs."+str("%.2f"%(q15+((q15)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

            elif(self.var_meal.get()=='Lunch'):
                q11=float(300) #lunch price
                q12=float(300) #single price
                q13=float(self.var_noofdays.get())
                q14=float(q11+q12)
                q15=float(q13*q14)
                Tax="Rs."+str("%.2f"%((q15)*0.1))
                ST="Rs."+str('%.2f'%((q15)))
                TT="Rs."+str("%.2f"%(q15+((q15)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

            elif(self.var_meal.get()=='Dinner'):
                q11=float(400) #dinner price
                q12=float(300) #single price
                q13=float(self.var_noofdays.get())
                q14=float(q11+q12)
                q15=float(q13*q14)
                Tax="Rs."+str("%.2f"%((q15)*0.1))
                ST="Rs."+str('%.2f'%((q15)))
                TT="Rs."+str("%.2f"%(q15+((q15)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)
            else:
                q11=float(900) #all meal price
                q12=float(300) #single price
                q13=float(self.var_noofdays.get())
                q14=float(q11+q12)
                q15=float(q13*q14)
                Tax="Rs."+str("%.2f"%((q15)*0.1))
                ST="Rs."+str('%.2f'%((q15)))
                TT="Rs."+str("%.2f"%(q15+((q15)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

        elif(self.var_roomtype.get()=='Double'):
            if(self.var_meal.get()=='BreakFast'):
                q21=float(200) #BreakFast price
                q22=float(500) #Double price
                q23=float(self.var_noofdays.get())
                q24=float(q21+q22)
                q25=float(q23*q24)
                Tax="Rs."+str("%.2f"%((q25)*0.1))
                ST="Rs."+str('%.2f'%((q25)))
                TT="Rs."+str("%.2f"%(q25+((q25)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

            elif(self.var_meal.get()=='Lunch'):
                q21=float(300) #lunch price
                q22=float(500) #Double price
                q23=float(self.var_noofdays.get())
                q24=float(q21+q22)
                q25=float(q23*q24)
                Tax="Rs."+str("%.2f"%((q25)*0.1))
                ST="Rs."+str('%.2f'%((q25)))
                TT="Rs."+str("%.2f"%(q25+((q25)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

            elif(self.var_meal.get()=='Dinner'):
                q21=float(400) #dinner price
                q22=float(500) #Double price
                q23=float(self.var_noofdays.get())
                q24=float(q21+q22)
                q25=float(q23*q24)
                Tax="Rs."+str("%.2f"%((q25)*0.1))
                ST="Rs."+str('%.2f'%((q25)))
                TT="Rs."+str("%.2f"%(q25+((q25)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

            else:
                q11=float(900) #all meal price
                q12=float(500) #double price
                q13=float(self.var_noofdays.get())
                q14=float(q11+q12)
                q15=float(q13*q14)
                Tax="Rs."+str("%.2f"%((q15)*0.1))
                ST="Rs."+str('%.2f'%((q15)))
                TT="Rs."+str("%.2f"%(q15+((q15)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

        else:
            if(self.var_meal.get()=='BreakFast'):
                q21=float(200) #BreakFast price
                q22=float(700) #Luxury price
                q23=float(self.var_noofdays.get())
                q24=float(q21+q22)
                q25=float(q23*q24)
                Tax="Rs."+str("%.2f"%((q25)*0.1))
                ST="Rs."+str('%.2f'%((q25)))
                TT="Rs."+str("%.2f"%(q25+((q25)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

            elif(self.var_meal.get()=='Lunch'):
                q21=float(300) #lunch price
                q22=float(700) #Luxury price
                q23=float(self.var_noofdays.get())
                q24=float(q21+q22)
                q25=float(q23*q24)
                Tax="Rs."+str("%.2f"%((q25)*0.1))
                ST="Rs."+str('%.2f'%((q25)))
                TT="Rs."+str("%.2f"%(q25+((q25)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)

            elif(self.var_meal.get()=='Dinner'):
                q21=float(400) #dinner price
                q22=float(700) #Luxury price
                q23=float(self.var_noofdays.get())
                q24=float(q21+q22)
                q25=float(q23*q24)
                Tax="Rs."+str("%.2f"%((q25)*0.1))
                ST="Rs."+str('%.2f'%((q25)))
                TT="Rs."+str("%.2f"%(q25+((q25)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)
            else:
                q11=float(900) #all meal price
                q12=float(700) #Luxury price
                q13=float(self.var_noofdays.get())
                q14=float(q11+q12)
                q15=float(q13*q14)
                Tax="Rs."+str("%.2f"%((q15)*0.1))
                ST="Rs."+str('%.2f'%((q15)))
                TT="Rs."+str("%.2f"%(q15+((q15)*0.1)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(ST)
                self.var_total.set(TT)
            
                
                

        #elif(self.var_meal.get=='BreakFast' and self.var_roomtype.get()=='Luxury'):
            #q1=float(200) #brakfast price
            #q2=float(700) #luxury price
            #q3=float(self.var_noofdays.get())
            #q4=float(q1+q2)
            #q5=float(q3*q4)
            #Tax="Rs."+str("%.2f"%((q5)*0.1))
            #ST="Rs."+str('%.2f'%((q5)))
            #TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            #self.var_paidtax.set(Tax)
            #self.var_actualtotal.set(TT)
            #self.var_total.set(TT)

            

        #elif(self.var_meal.get()=='Lunch' and self.var_roomtype.get()=='Single'):
            #q1=float(300) #Lunch price
            #q2=float(300) #Single price
            #q3=float(self.var_noofdays.get())
            #q4=float(q1+q2)
            #q5=float(q3+q4)
            #Tax="Rs."+str("%.2f"%((q5)*0.1))
            #ST="Rs."+str('%.2f'%((q5)))
            #TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            #self.var_paidtax.set(Tax)
            #self.var_actualtotal.set(ST)
            #self.var_total.set(TT)
    #search system
    def search(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='Liyakath@045',
            database='management'
        )
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
