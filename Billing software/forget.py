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
from subprocess import call
root1=Tk()


root1.title("Forget password")
root1.geometry("1520x800")
root1.state('zoomed')

bg=ImageTk.PhotoImage(file=r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\prop2.jpg")

lbl_bg=Label(root1,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

frame=Frame(root1,bg="black",width=340,height=490)
frame.place(x=450,y=100)

img1=Image.open(r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\image312.webp")
img1=img1.resize((100,100),Image.LANCZOS)
Photoimage1=ImageTk.PhotoImage(img1)
lblimg1=Label(frame,image=Photoimage1,bg="black",borderwidth=0,width=100,height=100)
lblimg1.place(x=118,y=3)

get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
get_str.place(x=95,y=105)

curpass=lbl=Label(frame,text="Current Password :",font=("times new roman",15,"bold"),fg="white",bg="black")
curpass.place(x=70,y=155)

txt=ttk.Entry(frame,font=("times new roman",15,"bold"))
txt.place(x=40,y=180,width=270)

newpass=lbl=Label(frame,text="New Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
newpass.place(x=70,y=225)

txt1=ttk.Entry(frame,font=("times new roman",15,"bold"))
txt1.place(x=40,y=250,width=270)



password=lbl=Label(frame,text="Confrom Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
password.place(x=70,y=295)

txt2=ttk.Entry(frame,font=("times new roman",15,"bold"))
txt2.place(x=40,y=320,width=270)




img2=Image.open(r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\lock.jpg")
img2=img2.resize((20,20),Image.LANCZOS)
Photoimage2=ImageTk.PhotoImage(img2)
lblimg2=Label(frame,image=Photoimage2,borderwidth=0,bg="black",width=20,height=20)
lblimg2.place(x=50,y=158)

img3=Image.open(r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\lock.jpg")
img3=img3.resize((20,20),Image.LANCZOS)
Photoimage3=ImageTk.PhotoImage(img3)
lblimg3=Label(frame,image=Photoimage3,borderwidth=0,width=20,height=20)
lblimg3.place(x=50,y=228)

img4=Image.open(r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\lock.jpg")
img4=img4.resize((20,20),Image.LANCZOS)
Photoimage4=ImageTk.PhotoImage(img4)
lblimg4=Label(frame,image=Photoimage4,borderwidth=0,width=20,height=20)
lblimg4.place(x=50,y=298)




        
def login():
  f=txt.get()
  g=txt1.get()
  a=txt2.get()
  if f=="" or g=="" or a=="":
      messagebox.showerror("Error","All filed required")
      
  elif a!=g:
      messagebox.showerror("Error","Password not match")
     
 
    
  elif a and g:
      messagebox.showinfo("Success","Your Login form successfully Submit")
      call(['python','login.py'])
      root1.destroy()
      
  else:
     messagebox.showerror("Invalid","Invalid username&Password")
        
        



def log(e):
   login()

root1.bind("<Return>",log)

def back():
    call(['python','login.py'])
    root1.destroy()

loginbtn=Button(frame,text="Submit",command=login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
loginbtn.place(x=190,y=430,width=120,height=35)


backbtn=Button(frame,text="Back",command=back,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
backbtn.place(x=40,y=430,width=120,height=35)




root1.mainloop()