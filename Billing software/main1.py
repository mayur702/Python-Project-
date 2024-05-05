from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
import random,os
from tkinter import messagebox 
import tempfile
from datetime import datetime



class Bill_App:
    def __init__(self,root):
    
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        #==================variable==========================#
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.categories=StringVar()
        
       


        

        

        


        #product categories list
        self.Category=["Select Option","Oil","Salt","Sweet","Rice"]
        self.SubCatOil=["Hair oil","Refined Oil"]
        self.Hairoil=["parashot oil","Coconat oil"]
        self.price_parashotoil=120
        self.price_coconatoil=100
       
        self.Refinedoil=["Keshar gold","Palmolen oil"]
        self.price_Keshargold=1650
        self.price_palmolenoil=1450

        self.SubCatSalt=["Big Salt","Small Salt"]
        self.Bigsalt=["Tata salt","Iodin salt"]
        self.price_tata=10
        self.price_iodin=10

        self.smallsalt=["Tata salt","Iodin salt"]
        self.price_tatas=10
        self.price_iodins=10

        self.SubCatSweet=["Sugar","Gul"]
        self.sugar=["Herms organic","Uttam sugar","vedaka"]
        self.price_herms=46
        self.price_uttam=60
        self.price_vedaka=50

        self.Gul=["Ratan","keshari"]
        self.price_ratan=60
        self.price_keshari=58

        
        self.SubCatRice=["sample rice","higher rice"]
        self.samplerice=["Tukada"]
        self.price_Tukada=50
        
        
        
        self.higherrice=["Chand Tara","Basamati","Fourchunar"]
        self.price_ChandTara=80
        self.price_Basamati=70
        self.price_Fourchunar=100



        
#Image1
        img_1=Image.open("image/first.jpg")
        img_1=img_1.resize((500,130),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=0,y=0,width=500,height=130)
#Image2
        img_2=Image.open("image/girls.jpg")
        img_2=img_2.resize((500,130),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=500,y=0,width=500,height=130)
#Image3
        img_3=Image.open("image/girl1.jpg")
        img_3=img_3.resize((520,130),Image.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lbl_img_3=Label(self.root,image=self.photoimg_3)
        lbl_img_3.place(x=1000,y=0,width=520,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("times new roman",35,"bold"),fg="red")
        lbl_title.place(x=400,y=130,width=500,height=45)
        
          
        #lbl_title2=Label(self.root,text="Develped By-Roadtopper.com",font=("times new roman",20,"bold"),fg="red")
        #lbl_title2.place(x=910,y=130,width=400,height=45)


        def time():
                string=strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(self.root,font=("times new roman",16,"bold"),background="white",foreground="blue")
        lbl.place(x=30,y=130,width=120,height=45)
        time()

        '''date=dt.datetime.now()
        label=Label(self.root,text=f"{date:%A, %B %d, %Y}", font="Calibri, 15",bg="white")
        label.place(x=150,y=15,width=120,height=45)'''


        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=175,width=1530,height=620)

    #customer LabelFrame

        cust_frame=LabelFrame(Main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(cust_frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        
        self.cust_name=Label(cust_frame,text="Customer Name.",font=("times new roman",12,"bold"),bg="white")
        self.cust_name.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.entry_custname=ttk.Entry(cust_frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.entry_custname.grid(row=1,column=1)

        
        self.lbl_email=Label(cust_frame,text="Customer Email.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_email.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.entry_email=ttk.Entry(cust_frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.entry_email.grid(row=2,column=1)

         #product LabelFrame

        product_frame=LabelFrame(Main_frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        product_frame.place(x=370,y=5,width=620,height=140)

        #categories

        
        self.lblcategories=Label(product_frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white")
        self.lblcategories.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.combo_categories=ttk.Combobox(product_frame,textvariable=self.categories,value=self.Category,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_categories.current(0)
        self.combo_categories.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.combo_categories.bind("<<ComboboxSelected>>",self.Categories)

        #subcategories


        
        
        self.subcategories=Label(product_frame,text="Subcategory",font=("times new roman",12,"bold"),bg="white")
        self.subcategories.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.combo_subcategories=ttk.Combobox(product_frame,value=[""],font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_subcategories.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.combo_subcategories.bind("<<ComboboxSelected>>",self.Product_add)

        #productname

        
        
        self.lblproduct=Label(product_frame,text="Product name",font=("times new roman",12,"bold"),bg="white")
        self.lblproduct.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.combo_product=ttk.Combobox(product_frame,textvariable=self.product,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_product.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.combo_product.bind("<<ComboboxSelected>>",self.price)

        #price

        
        
        self.lblprice=Label(product_frame,text="Price",font=("times new roman",12,"bold"),bg="white")
        self.lblprice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.combo_price=ttk.Combobox(product_frame,textvariable=self.prices,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_price.grid(row=0,column=3,stick=W,padx=5,pady=2)

        #Qty
        
        
        self.lblQty=Label(product_frame,text="Qty",font=("times new roman",12,"bold"),bg="white")
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.combo_Qty=ttk.Combobox(product_frame,textvariable=self.qty,font=("times new roman",10,"bold"),width=24)
        self.combo_Qty.grid(row=1,column=3,stick=W,padx=5,pady=2)

        #Middle Frame

        MiddleFrame=Frame(Main_frame,bd=10)
        MiddleFrame.place(x=0,y=150,width=950,height=340)

        #Image
        img_4=Image.open("image/good.jpg")
        img_4=img_4.resize((490,340),Image.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        lbl_img_4=Label(MiddleFrame,image=self.photoimg_4)
        lbl_img_4.place(x=0,y=0,width=490,height=340)
        #Image5
        img_5=Image.open("image/mall.jpg")
        img_5=img_5.resize((490,340),Image.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        lbl_img_5=Label(MiddleFrame,image=self.photoimg_5)
        lbl_img_5.place(x=490,y=0,width=490,height=340)


        
        #Search
        Search_Frame=Frame(Main_frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("times new roman",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=15)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("times new roman",10,"bold"),bg="Orangered",fg="white",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #RightFrame Bill Aria

        RightLabelFrame=LabelFrame(Main_frame,text="Bill Aria",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,heigh=440)

        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        
#Bill Countar Labelframe
        Bottom_Frame=LabelFrame(Main_frame,text="Bill Countar",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal=Label(Bottom_Frame,text="SubTotal",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Entry_SubTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.Entry_SubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lblgovtax=Label(Bottom_Frame,text="Gov Tax",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblgovtax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.Entry_govtax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.Entry_govtax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbltotal=Label(Bottom_Frame,text="Total",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbltotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.Entry_total=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.Entry_total.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        
        #Button Frame       
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        lbl_title1=Label(Btn_Frame,text="ContactAs |MAYUR MAGAR|mayurmagar702@gmail.com| 8104051015",font=("times new roman",10,"bold"),fg="red")
        lbl_title1.grid(row=2,column=11,padx=10)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",height=2,font=("times new roman",10,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=2,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",height=2,font=("times new roman",10,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=2,column=2)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,text="Save Bill",height=2,font=("times new roman",10,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=2,column=4)

        self.Btnprint=Button(Btn_Frame,command=self.iprint,text="Print",height=2,font=("times new roman",10,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.Btnprint.grid(row=2,column=6)

        self.Btnclear=Button(Btn_Frame,command=self.clear,text="Clear",height=2,font=("times new roman",10,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.Btnclear.grid(row=2,column=8)

        self.Btnexit=Button(Btn_Frame,command=self.root.destroy,text="Exit",height=2,font=("times new roman",10,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.Btnexit.grid(row=2,column=10)
        self.welcome()

        self.l=[]

       # ========================function==================================#


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome Mayur Kirana Store")
        
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Mobile Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")
       

        


        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\t\t\tPrice")
        self.textarea.insert(END,"\n==================================================\n")

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
                messagebox.showerror("Error","Please Select the Product Name")
        else:
                self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
                self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
                self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
                self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
                messagebox.showerror("Error","Please Add To Cart Product")
        
        else:
                text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                self.welcome()
                self.textarea.insert(END,text)
                self.textarea.insert(END,"\n ==================================================")
                self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
                self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
                self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
                self.textarea.insert(END,"\n==================================================\n")


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to Save the Bill")
        if op>0:
                self.bill_data=self.textarea.get(1.0,END)
                f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
                f1.write(self.bill_data)
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully")
                f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"Print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                        f1=open(f'bills/{i}','r')
                        self.textarea.delete(1.0,END)
                        for d in f1:
                                self.textarea.insert(END,d)
                        f1.close()
                        found="yes"

        if found=='no':
                messagebox.showerror("Error","Invalid Bill No.")


    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        x=random.randint(1,9999)
        self.bill_no.set(str(x))
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.categories.set("")
        self.l=[0]
        self.welcome()
        



    def Categories(self,event=""):
        if self.combo_categories.get()=="Oil":
                self.combo_subcategories.config(value=self.SubCatOil)
                self.combo_subcategories.current(0)


        if self.combo_categories.get()=="Salt":
                self.combo_subcategories.config(value=self.SubCatSalt)
                self.combo_subcategories.current(0)


        if self.combo_categories.get()=="Sweet":
                self.combo_subcategories.config(value=self.SubCatSweet)
                self.combo_subcategories.current(0)

        if self.combo_categories.get()=="Rice":
                self.combo_subcategories.config(value=self.SubCatRice)
                self.combo_subcategories.current(0)



    def Product_add(self,event=""):
        if self.combo_subcategories.get()=="Hair oil":
                self.combo_product.config(value=self.Hairoil)
                self.combo_product.current(0)


        if self.combo_subcategories.get()=="Refined Oil":
                self.combo_product.config(value=self.Refinedoil)
                self.combo_product.current(0)


      #salt

        if self.combo_subcategories.get()=="Big Salt":
                self.combo_product.config(value=self.Bigsalt)
                self.combo_product.current(0)


        if self.combo_subcategories.get()=="Small Salt":
                self.combo_product.config(value=self.smallsalt)
                self.combo_product.current(0)



        #sweet

        
        if self.combo_subcategories.get()=="Sugar":
                self.combo_product.config(value=self.sugar)
                self.combo_product.current(0)


        
        if self.combo_subcategories.get()=="Gul":
                self.combo_product.config(value=self.Gul)
                self.combo_product.current(0)



          #rice

        
        if self.combo_subcategories.get()=="sample rice":
                self.combo_product.config(value=self.samplerice)
                self.combo_product.current(0)


        
        if self.combo_subcategories.get()=="higher rice":
                self.combo_product.config(value=self.higherrice)
                self.combo_product.current(0)


    def price(self,event=""):
        if  self.combo_product.get()=="parashot oil":
                self.combo_price.config(value=self.price_parashotoil)
                self.combo_price.current(0)
                self.qty.set(1)


        if  self.combo_product.get()=="Coconat oil":
                self.combo_price.config(value=self.price_coconatoil)
                self.combo_price.current(0)
                self.qty.set(1) 


        if  self.combo_product.get()=="Keshar gold":
                self.combo_price.config(value=self.price_Keshargold)
                self.combo_price.current(0)
                self.qty.set(1)


        
        if  self.combo_product.get()=="Palmolen oil":
                self.combo_price.config(value=self.price_palmolenoil)
                self.combo_price.current(0)
                self.qty.set(1)



        
        if  self.combo_product.get()=="Tata salt":
                self.combo_price.config(value=self. price_tata)
                self.combo_price.current(0)
                self.qty.set(1)



        
        if  self.combo_product.get()=="Iodin salt":
                self.combo_price.config(value=self. price_iodin)
                self.combo_price.current(0)
                self.qty.set(1)



        
        
        if  self.combo_product.get()=="Tata salt":
                self.combo_price.config(value=self. price_tatas)
                self.combo_price.current(0)
                self.qty.set(1)



        
        if  self.combo_product.get()=="Iodin salt":
                self.combo_price.config(value=self. price_iodins)
                self.combo_price.current(0)
                self.qty.set(1) 



        
        
        if  self.combo_product.get()=="Herms organic":
                self.combo_price.config(value=self. price_herms)
                self.combo_price.current(0)
                self.qty.set(1)



        
        if  self.combo_product.get()=="Uttam sugar":
                self.combo_price.config(value=self. price_uttam)
                self.combo_price.current(0)
                self.qty.set(1)


        if  self.combo_product.get()=="vedaka":
                self.combo_price.config(value=self. price_vedaka)
                self.combo_price.current(0)
                self.qty.set(1) 


        
        if  self.combo_product.get()=="Ratan":
                self.combo_price.config(value=self. price_ratan)
                self.combo_price.current(0)
                self.qty.set(1)


        if  self.combo_product.get()=="keshari":
                self.combo_price.config(value=self. price_keshari)
                self.combo_price.current(0)
                self.qty.set(1)



        if  self.combo_product.get()=="Tukada":
                self.combo_price.config(value=self. price_Tukada)
                self.combo_price.current(0)
                self.qty.set(1)




        if  self.combo_product.get()=="Chand Tara":
                self.combo_price.config(value=self. price_ChandTara)
                self.combo_price.current(0)
                self.qty.set(1)


        if  self.combo_product.get()=="Basamati":
                self.combo_price.config(value=self. price_Basamati)
                self.combo_price.current(0)
                self.qty.set(1)

        
        if  self.combo_product.get()=="Fourchunar":
                self.combo_price.config(value=self. price_Fourchunar)
                self.combo_price.current(0)
                self.qty.set(1)


        




         




        


        



 





















if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()