from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
import random
import mysql.connector
from subprocess import call
root1=Tk()


root1.title("login page")
root1.geometry("1520x800")
root1.state('zoomed')

bg=ImageTk.PhotoImage(file=r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\prop4.jpg")

lbl_bg=Label(root1,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

frame=Frame(root1,bg="black",width=340,height=450)
frame.place(x=450,y=100)

img1=Image.open(r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\image312.webp")
img1=img1.resize((100,100),Image.LANCZOS)
Photoimage1=ImageTk.PhotoImage(img1)
lblimg1=Label(frame,image=Photoimage1,bg="black",borderwidth=0,width=100,height=100)
lblimg1.place(x=118,y=3)

get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
get_str.place(x=95,y=105)

username=lbl=Label(frame,text="UserName :",font=("times new roman",15,"bold"),fg="white",bg="black")
username.place(x=70,y=155)

txt=ttk.Entry(frame,font=("times new roman",15,"bold"))
txt.place(x=40,y=180,width=270)

password=lbl=Label(frame,text="Password :",font=("times new roman",15,"bold"),fg="white",bg="black")
password.place(x=70,y=225)

txt1=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
txt1.place(x=40,y=250,width=270)

img2=Image.open(r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\th.jpg")
img2=img2.resize((20,20),Image.LANCZOS)
Photoimage2=ImageTk.PhotoImage(img2)
lblimg2=Label(frame,image=Photoimage2,borderwidth=0,bg="black",width=20,height=20)
lblimg2.place(x=50,y=158)

img3=Image.open(r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\lock.jpg")
img3=img3.resize((20,20),Image.LANCZOS)
Photoimage3=ImageTk.PhotoImage(img3)
lblimg3=Label(frame,image=Photoimage3,borderwidth=0,width=20,height=20)
lblimg3.place(x=50,y=228)

        
def login():
  conn=mysql.connector.connect(host='database-2.ct0qesoicb3w.us-east-2.rds.amazonaws.com',username='admin',password='admin123',database='mayur')
  my_curser=conn.cursor()
  my_curser.execute("select name from magarm where password='"+txt1.get()+"'")
  
  v=my_curser.fetchall()
  for i in v:
     for j in i:
        x=j
  my_curser.execute("select password from magarm where name='"+txt.get()+"'")
  v=my_curser.fetchall()
  for i in v:
     for j1 in i:
        
                                              
         f=txt.get()
         g=txt1.get()
         
         z=j1
         if f=="" and g=="":
            
            messagebox.showerror("Error","All filed required")
            
         elif f != x and g != z:
            messagebox.showerror("Error","Username&Password Invalid ")
               
        
                     
         elif f==x and g==z:
               messagebox.showinfo("Success","Your Login form successfully Submit")
               call(['python','main1.py'])
               root1.destroy()
               
         else:
            messagebox.showerror("Invalid","Invalid username&Password")
               
               



def log(e):
   login()

root1.bind("<Return>",log)

def newuser():
   call(['python','login2.py'])
   root1.destroy()
   
   
def forget():
   call(['python','forget.py'])
   root1.destroy()
   

loginbtn=Button(frame,text="Login",command=login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red",cursor="hand2")
loginbtn.place(x=110,y=300,width=120,height=35)

loginbtn=Button(frame,text="New User Register",command=newuser,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
loginbtn.place(x=15,y=350,width=160)

loginbtn=Button(frame,text="Forget Password",command=forget,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
loginbtn.place(x=10,y=370,width=160)





root1.mainloop()