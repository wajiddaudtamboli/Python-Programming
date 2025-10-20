from tkinter import *
from tkinter import messagebox

import sqlite3


class proj:

    def __init__(self):

        

        self.top=Tk()

        self.top.geometry("500x500")

        f=Frame(self.top,width=400,height=400,bg="pink")

        l=Label(f,text="Login",font=("bold",20),bg="pink")
        l.place(x=160,y=30)

        ul=Label(f,text="username",font=("bold",15),bg="pink")
        ul.place(x=50,y=80)
        self.ue=Entry(f)
        self.ue.place(x=160,y=80)


        pl=Label(f,text="password",font=("bold",15),bg="pink")
        pl.place(x=50,y=120)
        self.pe=Entry(f)
        self.pe.place(x=160,y=120)

        b=Button(f,text="login",bg="light green",font=("bold",12),width=8,height=1,command=self.logincode)
        b.place(x=160,y=160)

        b1=Button(f,text="Sign in",bg="light blue",font=("bold",12),width=8,height=1,command=self.register)
        b1.place(x=160,y=200)

        b2=Button(f,text="update",bg="light blue",font=("bold",12),width=8,height=1,command=self.update)
        b2.place(x=160,y=240)

        b2=Button(f,text="delete",bg="light blue",font=("bold",12),width=8,height=1,command=self.delete)
        b2.place(x=160,y=280)

        f.place(x=50,y=50)

        self.top.mainloop()

    def delete(self):
         user=self.ue.get()
         
         try:
             con=sqlite3.connect("mydata.db")
             cur=con.cursor()
             sql="delete from details  where id=?"
             cur.execute(sql,(user))
             con.commit()
             
             messagebox.showinfo("info"," user delete sucessfully")
             
             
         except Exception as e:

             print(e)
         finally:
             con.close()
             self.ue.delete(first=0,last=100)
        


    def update(self):
         user=self.ue.get()
         pas=self.pe.get()
         try:
             con=sqlite3.connect("mydata.db")
            
             sql="update register set password=? where email=?"
             con.execute(sql,(pas,user))
             con.commit()
             
             messagebox.showinfo("info"," password change sucessfully")
             
             
         except Exception as e:

             print(e)
         finally:
             con.close()
             self.ue.delete(first=0,last=100)

        

    def home(self):

        f2=Frame(self.top,width=400,height=400,bg="green")
        l=Label(f2,text="Home",font=("bold",20),bg="green")
        l.place(x=160,y=30)
        f2.place(x=50,y=50)
        

    def logincode(self):

        user=self.ue.get()
        pas=self.pe.get()

        try:
             con=sqlite3.connect("mydata.db")
             cur=con.cursor()
             sql="select * from Register"
             cur.execute(sql)
             rows=cur.fetchall()
             print(rows)
             f=0

             for row in rows:

                 if user==row[2] and pas==row[3]:

                     f=1

             if f==1:
                 print("login sucessfull")
                 messagebox.showinfo("info","login sucessfully")
                 self.home()
             else:

                 messagebox.showinfo("info","invalid username and password")
             
        except Exception as e:

            print(e)
        finally:
            con.close()
            

    def regcode(self):

            name=self.fne.get()
            lname=self.lne.get()
            email=self.ee1.get()
            pas=self.pe1.get()
            mob=self.me1.get()
            print(name,lname,email,pas,mob)


            try:

                con=sqlite3.connect("mydata.db")

                sql="insert into register(fname,lname,email,password,mobile)values(?,?,?,?,?)"

                con.execute(sql,(name,lname,email,pas,mob))

                con.commit()

                messagebox.showinfo("info","data insert sucessfull")
            except Exception as e:

                print(e)
            finally:

                con.close()
                self.fne.delete(first=0,last=100)
                self.lne.delete(first=0,last=100)
                self.ee1.delete(first=0,last=100)
                self.pe1.delete(first=0,last=100)
                self.me1.delete(first=0,last=100)
        

    def register(self):

        f1=Frame(self.top,width=400,height=400,bg="light blue")

        l=Label(f1,text="Register",font=("bold",20),bg="light blue")
        l.place(x=160,y=10)

        
        fnl=Label(f1,text="First Name",font=("bold",15),bg="light blue")
        fnl.place(x=100,y=100)

        self.fne=Entry(f1)
        self.fne.place(x=210,y=100)

        lnl=Label(f1,text="Last Name",font=("bold",15),bg="light blue")
        lnl.place(x=100,y=140)

        self.lne=Entry(f1)
        self.lne.place(x=210,y=140)

        el=Label(f1,text="Email",font=("bold",15),bg="light blue")
        el.place(x=100,y=180)

        self.ee1=Entry(f1)
        self.ee1.place(x=210,y=180)
        
        pl=Label(f1,text="password",font=("bold",15),bg="light blue")
        pl.place(x=100,y=220)

        self.pe1=Entry(f1)
        self.pe1.place(x=210,y=220)

        
        ml=Label(f1,text="Mobile no",font=("bold",15),bg="light blue")
        ml.place(x=100,y=260)

        self.me1=Entry(f1)
        self.me1.place(x=210,y=260)

        b3=Button(f1,text="register",bg="light green",font=("bold",12),width=8,height=1,command=self.regcode)
        b3.place(x=190,y=300)

        b3=Button(f1,text="<-",command=self.__init__)
        b3.place(x=0,y=0)


        f1.place(x=50,y=50)


obj=proj()












