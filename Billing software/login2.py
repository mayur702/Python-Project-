from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from subprocess import call
import re
import mysql.connector
import pyttsx3


class Register():
    def __init__(self,root):
        self.root=root
        self.root.title('Reigeister page')
        self.root.geometry('1600x790+0+0')
        
        #text to speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
        
        #variable
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        self.id_var=StringVar()
        self.id_no_var=StringVar()
        self.password_var=StringVar()
        self.confirm_pass_var=StringVar()
        self.check_var=IntVar()
        
        
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Mayur Magar\Desktop\Mayur Billing software\image\prop4.jpg")

        lbl_bg=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        logo_img=Image.open('image/th.jpg')
        logo_img=logo_img.resize((60,60),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)
        
        #title frame

        title_frame=Frame(self.root,bd=1,relief=RAISED,width=550,height=82)
        title_frame.place(x=450,y=28)
        
        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='USER REGISTER FORM',font=("times new roman",25,'bold'),fg='darkblue')
        title_lbl.place(x=10,y=10)
        
        #main frame
        
        main_frame=Frame(self.root,bd=1,relief=RAISED)
        main_frame.place(x=450,y=110,width=550,height=620)
        
        #username
        
        user_name=Label(main_frame,text='Username:',font=("times new roman",16,'bold'))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=("times new roman",16,'bold'),width=25)
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        validate_name=self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))
        
        
        email=Label(main_frame,text='Email:',font=("times new roman",16,'bold'))
        email.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        email_entry=ttk.Entry(main_frame,textvariable=self.email_var,font=("times new roman",16,'bold'),width=25)
        email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        contact=Label(main_frame,text='Contact:',font=("times new roman",16,'bold'))
        contact.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        contact_entry=ttk.Entry(main_frame,textvariable=self.contact_var,font=("times new roman",16,'bold'),width=25)
        contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        validate_contact=self.root.register(self.checkcontact)
        contact_entry.config(validate='key',validatecommand=(validate_contact,'%P'))
        
          
        gender_lbl=Label(main_frame,text='Select Gender:',font=("times new roman",16,'bold'))
        gender_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        gender_frame=Frame(main_frame)
        gender_frame.place(x=200,y=160,width=280,height=35)
        
        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='Male',text='Male',font=("times new roman",15))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set('Male')
        
        radio_female=Radiobutton(gender_frame,variable=self.gender_var,value='Female',text='Female',font=("times new roman",15))
        radio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)
        
        select_country=Label(main_frame,text='Select Country:',font=("times new roman",16,'bold'))
        select_country.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        self.gender_var.set('Female')
        
        list=['India','UK','Nepal','China']
        droplist=OptionMenu(main_frame,self.country_var,*list)
        droplist.config(width=21,font=("times new roman",15),bg='white')
        self.country_var.set('Select your Country')
        droplist.grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        
        id_type=Label(main_frame,text='Select ID Type:',font=("times new roman",16,'bold'))
        id_type.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        
        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=("times new roman",15),justify='center',state="readonly",width=23)
        self.combo_id_type['values']=("Select Your Id","Adhar Card","Passport","Driving Licence")
        self.combo_id_type.grid(row=5,column=1,padx=10,pady=10)
        self.combo_id_type.current(0) 
        
        
        
        
        id_no=Label(main_frame,text='ID Number:',font=("times new roman",16,'bold'))
        id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        
        entry_idno=ttk.Entry(main_frame,textvariable=self.id_no_var,font=("times new roman",15),width=25)
        entry_idno.grid(row=6,column=1,padx=10,pady=10,sticky=W)
        
        
        
        password=Label(main_frame,text='Password:',font=("times new roman",16,'bold'))
        password.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        
        entry_password=ttk.Entry(main_frame,textvariable=self.password_var,font=("times new roman",15),width=25)
        entry_password.grid(row=7,column=1,padx=10,pady=10,sticky=W)
        
        
        
        confirm=Label(main_frame,text='Confirm Password:',font=("times new roman",16,'bold'))
        confirm.grid(row=8,column=0,padx=10,pady=10,sticky=W)
        
        entry_confirm=ttk.Entry(main_frame,textvariable=self.confirm_pass_var,font=("times new roman",15),width=25)
        entry_confirm.grid(row=8,column=1,padx=10,pady=10,sticky=W)
        
        check_frame=Frame(main_frame)
        check_frame.place(x=130,y=460,width=400,height=70)
        
        check_btn=Checkbutton(check_frame,variable=self.check_var,text="Agree our terms & Conditions",font=("times new roman",15),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)
        
        self.check_lbl=Label(check_frame,font=("times new roman",15),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        btn_frame=Frame(main_frame)
        btn_frame.place(x=30,y=530,width=480,height=70)
        
        
        savedata=Button(btn_frame,text="Save",command=self.validation,font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',foreground='white')
        savedata.grid(row=0,column=0,padx=1,sticky=W)
        
        
        
        verifydata=Button(btn_frame,text="Verify Data",command=self.verify_data,font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',foreground='white')
        verifydata.grid(row=0,column=1,padx=1,sticky=W)
        
        
        
        cleardata=Button(btn_frame,text="Clear Data",command=self.clear_data,font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',foreground='white')
        cleardata.grid(row=0,column=2,padx=1,sticky=W)
        
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed'+name[-1])
            
            
            
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror('Invalid','Invalid Mobile Number')
            return False
        
        
        
        
          
            
    def checkpassword(self,Password):
        if len(Password)<=8:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",Password):
                return True
            else:
                self.engine.say('Enter valid password(Example:Hacker@001)')
                self.engine.runAndWait()
                messagebox.showinfo("Invalid","Enter valid password(Example:Hacker@001)")
                return False
            
        else:
            messagebox.showerror("Invalid","Please Try Again")
            return False
        
        
        
    def checkemail(self,Email):
        if len(Email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",Email):
                return True
            else:
                self.engine.say('Invalid Email Please Enter Valid Email(roadtopper01@gmail.com)')
                self.engine.runAndWait()
                messagebox.showwarning("Alert","Invalid Email Please Enter Valid Email(roadtopper01@gmail.com)")
                return False
            
        else:
            messagebox.showerror("Invalid","Please Try Again")
            return 
        
    #validtion
    
    def validation(self):
        if self.name_var.get()=='':
            self.engine.say('Please Enter Your Name')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Enter Your Name",parent=self.root)
            
        elif self.email_var.get()=='':
            self.engine.say('Please Enter Your Email')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Enter Your Email",parent=self.root)
            
        elif self.contact_var.get()=='' or len(self.contact_var.get())!=10:
            self.engine.say('Please Enter Your Vaild Contact')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Enter Your Vaild Contact",parent=self.root)
            
        elif self.gender_var.get()=='':
            self.engine.say('Please Select Your Gender')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Select Your Gender",parent=self.root)
            
            
        elif self.country_var.get()=='' or self.country_var.get()=='Select Your Country':
            self.engine.say('Please Select Your Country Name')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Select Your Country Name",parent=self.root)
            
            
        elif self.id_var.get()=="Select Your ID":
            self.engine.say('Please Select Your ID Type')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Select Your ID Type",parent=self.root)
            
        elif self.id_no_var.get()=='':
            self.engine.say('Please Enter your id no')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Enter your id no",parent=self.root)
            
        elif len(self.id_no_var.get())!=12:
            self.engine.say('Please Enter your 12 digit')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Enter your 12 digit",parent=self.root)
            
        elif self.password_var.get()=='':
            self.engine.say('Please Enter your Password')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Enter your Password",parent=self.root)
            
        elif self.confirm_pass_var.get()=='':
            self.engine.say('Please Enter your Confirm Password')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Please Enter your Confirm Password",parent=self.root)
            
        elif self.confirm_pass_var.get()!=self.password_var.get():
            self.engine.say('Password&Confirm Password Must be Same')
            self.engine.runAndWait()
            messagebox.showerror('Error',"Password&Confirm Password Must be Same",parent=self.root)
            
        elif self.email_var.get()!=None and self.password_var.get()!=None:
            x=self.checkemail(self.email_var.get())
            y=self.checkpassword(self.password_var.get())
            
        if (x==True) and (y==True):
            if self.check_var.get()==0:
                self.engine.say('Please Agree our terms & Conditions')
                self.engine.runAndWait()
                self.check_lbl.config(text="Please Agree our terms & Conditions",fg='red')
            else:
                self.check_lbl.config(text="Checked",fg='green')
                
                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='siit@123',database='mayur')
                    my_curser=conn.cursor()
                    my_curser.execute('insert into magarm values(%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                             self.name_var.get(),
                                                                                             self.email_var.get(),
                                                                                             self.contact_var.get(),
                                                                                             self.gender_var.get(),
                                                                                             self.country_var.get(),
                                                                                             self.id_var.get(),
                                                                                             self.id_no_var.get(),
                                                                                             self.password_var.get(),
                        
                            
                                                                                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Successfully",f"Your registration successfully completed your username:{self.name_var.get()} and Password:{self.password_var.get()}")
                    call(['python','login.py'])
                    self.root.destroy()
                except Exception as es:
                    messagebox.showerror('Error'f"Due to:{str(es)}",parent=self.root)
         
         
    def verify_data(self):
        data=f'Name:{self.name_var.get()}\nEmail:{self.email_var.get()}\nContact{self.contact_var.get()}\nGender{self.gender_var.get()}\nCountry_Name{self.country_var.get()}\nId:{self.id_var.get()}\nId Number{self.id_no_var.get()}\nPassword{self.password_var.get()}'      
        messagebox.showinfo('Detalis',data)
        
        
    def clear_data(self):
        self.name_var.set('')
        self.email_var.set('')
        self.contact_var.set('')
        self.gender_var.set('Male')
        self.country_var.set('Select Your Country')
        self.id_var.set('Select Your Id')
        self.id_no_var.set('')
        self.password_var.set('')
        self.confirm_pass_var.set('')
        self.check_var.set(0)
         
         
    
    
         
         
            
            
            
        
        
        
        
        
        
        
        


        
        
        
        
if __name__=='__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()
        