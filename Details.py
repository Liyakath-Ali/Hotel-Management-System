from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roomdetails:
    def __init__(self,root):
        self.root=root
        self.root.title("New Room Details")
        self.root.geometry("1310x550+230+220")

        #==============TITLE==========================
        lbl_title=Label(self.root,text='NEW ROOM DETAILS',font=('Arial',18,'bold'),bg='black',fg='Purple',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #==============LOGO===========================
        img2=Image.open(r'C:\Users\bablu\OneDrive\Desktop\FSP\Python\hotel images\logohotel.png')
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=4,width=100,height=40)

        #============LABEL FRAME=======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=('Arial',12,'bold'))
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #============LABEL ENTRYS======================
        #floor
        lbl_floor=Label(labelframeleft,text="Floor no:",font=('Arial',12,'bold'),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=('Arial',13,'bold'))
        entry_floor.grid(row=0,column=1,sticky=W)

        #room no
        lbl_RoomNo=Label(labelframeleft,text="Room No:",font=('Arial',12,'bold'),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)

        self.var_roomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=20,font=('Arial',13,'bold'))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #room type
        lbl_RoomType=Label(labelframeleft,text="Room Type:",font=('Arial',12,'bold'),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=('Arial',13,'bold'))
        entry_RoomType.grid(row=2,column=1,sticky=W)

        #====================buttons====================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        add_btn=Button(btn_frame,text='ADD',command=self.add_data,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        add_btn.grid(row=0,column=0,padx=1)

        upd_btn=Button(btn_frame,text='UPDATE',command=self.update,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        upd_btn.grid(row=0,column=1,padx=1)

        del_btn=Button(btn_frame,text='DELETE',command=self.mDelete,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        del_btn.grid(row=0,column=2,padx=1)
        
        res_btn=Button(btn_frame,text='RESET',command=self.reset,width=10,font=('Arial',11,'bold'),bg='black',fg='Blue',cursor='hand2',relief=RIDGE)
        res_btn.grid(row=0,column=3,padx=1)

        #============TABLE FRAME SEARCH SYSTEM=======================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show room details",font=('Arial',12,'bold'))
        Table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_frame,column=('floor','roomno','roomType'))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('floor',text='Floor')
        self.room_table.heading('roomno',text='Room No')
        self.room_table.heading('roomType',text='Room Type')


        self.room_table['show']='headings'


        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                      self.var_floor.get(),
                                                                      self.var_roomNo.get(),
                                                                      self.var_RoomType.get()
                                                                      ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])

    #update
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_RoomType.get(),
                                                                                    self.var_roomNo.get()
                                                                                                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)

    #delete
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Liyakath@045',database='management')
            my_cursor=conn.cursor()
            query="Delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")

if __name__=="__main__":
    root=Tk()
    obj=Roomdetails(root)
    root.mainloop()
