from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1295x570+230+220")



    #===========VARIABLES=========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()  



    #==============TITLE==========================
        lbl_title=Label(self.root,text='ADD CUSTOMER DETAILS',font=('Arial',18,'bold'),bg='black',fg='Purple',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

    #==============LOGO===========================
        img2=Image.open(r'C:\users\bablu\OneDrive\Desktop\FSP\Python\hotel images\logohotel.png')
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=4,width=100,height=40)

    #============LABEL FRAME=======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer details",padx=2,font=('Arial',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=490)

    #============LABEL ENTRYS======================
        #cust ref
        lbl_cust_ref=Label(labelframeleft,text="Customer ref",font=('Arial',12,'bold'),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=('Arial',13,'bold'),state='readonly')
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,text="Customer name",font=('Arial',12,'bold'),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        entry_cname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=('Arial',13,'bold'))
        entry_cname.grid(row=1,column=1)

        #mother name
        mname=Label(labelframeleft,text="Mother name",font=('Arial',12,'bold'),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        entry_mname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=('Arial',13,'bold'))
        entry_mname.grid(row=2,column=1)

        #gender combobox
        gender=Label(labelframeleft,text="Gender",font=('Arial',12,'bold'),padx=2,pady=6)
        gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=('Arial',12,'bold'),width=27,state='readonly')
        combo_gender['value']=('Male','Female','Others')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #post code
        pcode=Label(labelframeleft,text="Postal Code",font=('Arial',12,'bold'),padx=2,pady=6)
        pcode.grid(row=4,column=0,sticky=W)
        entry_pcode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=('Arial',13,'bold'))
        entry_pcode.grid(row=4,column=1)

        #email
        mail=Label(labelframeleft,text="Email",font=('Arial',12,'bold'),padx=2,pady=6)
        mail.grid(row=5,column=0,sticky=W)
        entry_mail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=('Arial',13,'bold'))
        entry_mail.grid(row=5,column=1)
        
        #mobile
        mob=Label(labelframeleft,text="Mobile",font=('Arial',12,'bold'),padx=2,pady=6)
        mob.grid(row=6,column=0,sticky=W)
        entry_mob=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=('Arial',13,'bold'))
        entry_mob.grid(row=6,column=1)

        #nationality
        nat=Label(labelframeleft,text="Nationality",font=('Arial',12,'bold'),padx=2,pady=6)
        nat.grid(row=7,column=0,sticky=W)

        combo_nat=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=('Arial',12,'bold'),width=27,state='readonly')
        combo_nat['value']=('Indian','American','British','Other')
        combo_nat.current(0)
        combo_nat.grid(row=7,column=1)

        #id proof
        idtype=Label(labelframeleft,text="ID proof",font=('Arial',12,'bold'),padx=2,pady=6)
        idtype.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=('Arial',12,'bold'),width=27,state='readonly')
        combo_id['value']=('Aadhar','Driving license','Passport','Other')
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #id number
        idnum=Label(labelframeleft,text="ID number",font=('Arial',12,'bold'),padx=2,pady=6)
        idnum.grid(row=9,column=0,sticky=W)
        entry_idnum=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=('Arial',13,'bold'))
        entry_idnum.grid(row=9,column=1)

        #address
        addr=Label(labelframeleft,text="Address",font=('Arial',12,'bold'),padx=2,pady=6)
        addr.grid(row=10,column=0,sticky=W)
        entry_addr=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=('Arial',13,'bold'))
        entry_addr.grid(row=10,column=1)
        
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

        #============TABLE FRAME=======================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search system",font=('Arial',12,'bold'))
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblsearchby=Label(Table_frame,text="Search by:",font=('Arial',12,'bold'),bg='red',fg='White')
        lblsearchby.grid(row=0,column=0,sticky=W)

        self.serch_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,textvariable=self.serch_var,font=('Arial',12,'bold'),width=24,state='readonly')
        combo_search['value']=('Mobile','ref')
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()
        entry_search=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=('Arial',13,'bold'))
        entry_search.grid(row=0,column=2)

        search_btn=Button(Table_frame,command=self.search,text='Search',width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        search_btn.grid(row=0,column=3,padx=1)

        Sall_btn=Button(Table_frame,text='Search all',command=self.fetch_data,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        Sall_btn.grid(row=0,column=4,padx=1)
        

        #===============Show data table================

        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=('ref','name','mother','gender','post',
                                        'mobile','email','nationality','idproof','idnumber','address'))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)


        self.Cust_Details_Table.heading('ref',text='Refer no')
        self.Cust_Details_Table.heading('name',text='Name')
        self.Cust_Details_Table.heading('mother',text='Mother name')
        self.Cust_Details_Table.heading('gender',text='Gender')
        self.Cust_Details_Table.heading('post',text='Postcode')
        self.Cust_Details_Table.heading('mobile',text='Mobile')
        self.Cust_Details_Table.heading('email',text='Email')
        self.Cust_Details_Table.heading('nationality',text='Nationality')
        self.Cust_Details_Table.heading('idproof',text='Id Proof')
        self.Cust_Details_Table.heading('idnumber',text='Id Number')
        self.Cust_Details_Table.heading('address',text='Address')


        self.Cust_Details_Table['show']='headings'

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
         
        self.fetch_data()
        

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                      self.var_ref.get(),
                                                                      self.var_cust_name.get(),
                                                                      self.var_mother.get(),
                                                                      self.var_gender.get(),
                                                                      self.var_post.get(),
                                                                      self.var_mobile.get(),
                                                                      self.var_email.get(),
                                                                      self.var_nationality.get(),
                                                                      self.var_id_proof.get(),
                                                                      self.var_id_number.get(),
                                                                      self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer data has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]),

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                              self.var_cust_name.get(),
                                                                                                                                                              self.var_mother.get(),
                                                                                                                                                              self.var_gender.get(),
                                                                                                                                                              self.var_post.get(),
                                                                                                                                                              self.var_mobile.get(),
                                                                                                                                                              self.var_email.get(),
                                                                                                                                                              self.var_nationality.get(),
                                                                                                                                                              self.var_id_proof.get(),
                                                                                                                                                              self.var_id_number.get(),
                                                                                                                                                              self.var_address.get(),
                                                                                                                                                              self.var_ref.get()
                                                                                                                                                              ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
            my_cursor=conn.cursor()
            query="Delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='Liyakath@045',
            database='management'
        )
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
if __name__=='__main__':
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
