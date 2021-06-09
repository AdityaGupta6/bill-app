from tkinter import*
import math
from random import randint
from tkinter import messagebox
import os
class Bill_App:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing counter")
        bg_color="#074463"
        title1=Label(self.root,text="Biling sofware",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30, "bold"),pady=2).pack(fill=X)

        # variables 
        self.soap=IntVar()
        self.faceCream=IntVar()
        self.faceWash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()

        self.rice=IntVar()
        self.foodOil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        self.maza=IntVar()
        self.cocaCola=IntVar()
        self.frooti=IntVar()
        self.thumbsUp=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        self.cosmeticPrice=StringVar()
        self.groceryPrice=StringVar()
        self.drinkPrice=StringVar()

        self.cosmeticTax=StringVar()
        self.groceryTax=StringVar()
        self.drinkTax=StringVar()

        self.cName=StringVar()
        self.cphone=StringVar()
        self.billNo=StringVar()
        x=randint(1000,9999)
        self.billNo.set(str(x))
        self.searchBill=StringVar()




        f1=LabelFrame(self.root,text ="Cusomer details",bg=bg_color,fg="gold",font=("times new roman",15, "bold"))
        f1.place(x=0,y=80,relwidth=1)

        custLabel=Label(f1,text="Customer Name" ,bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        custName=Entry(f1,width=15,textvariable=self.cName,font=("arial 15"),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=5)

        phoneLabel=Label(f1,text="Phone no" ,bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        phoneName=Entry(f1,width=15,textvariable=self.cphone,font=("arial 15"),bd=7,relief=SUNKEN).grid(row=0,column=3,pady=10,padx=5)

        billLabel=Label(f1,text="Bill number" ,bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        billName=Entry(f1,width=15,textvariable=self.searchBill,font=("arial 15"),bd=7,relief=SUNKEN).grid(row=0,column=5,pady=10,padx=5)

        billBtn=Button(f1,text="Search",command=self.findBill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=30)

        # cosmetoics
        f2=LabelFrame(self.root,text ="Costemetics",bg=bg_color,fg="gold",font=("times new roman",15, "bold"))
        f2.place(x=0,y=180,width=325,height=380)

        bathLabel=Label(f2,text="Bath Soap",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bathtext=Entry(f2,width=10,textvariable=self.soap,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        faceLabel=Label(f2,text="Face Cream",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        facetext=Entry(f2,width=10,textvariable=self.faceCream,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        faceWashLabel=Label(f2,text="Face Wash",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        faceWashtext=Entry(f2,width=10,textvariable=self.faceWash,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hairLabel=Label(f2,text="hair Spray",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hairtext=Entry(f2,width=10,textvariable=self.spray,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hairGelLabel=Label(f2,text="Hair Gel",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hairGeltext=Entry(f2,width=10,textvariable=self.gell,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        bodyLabel=Label(f2,text="Baody Lotion ",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        bodytext=Entry(f2,width=10,textvariable=self.lotion,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # grocery 
        f3=LabelFrame(self.root,text ="Grocery",bg=bg_color,fg="gold",relief=GROOVE,font=("times new roman",15, "bold"))
        f3.place(x=340,y=180,width=325,height=380)

        c1Label=Label(f3,text="Rice",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1text=Entry(f3,width=10,textvariable=self.rice,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2Label=Label(f3,text="Food Oil",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2text=Entry(f3,width=10,textvariable=self.foodOil,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3Label=Label(f3,text="Daal",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3text=Entry(f3,width=10,textvariable=self.daal,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4Label=Label(f3,text="Wheat",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4text=Entry(f3,width=10,textvariable=self.wheat,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5GelLabel=Label(f3,text="Sugar",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5Geltext=Entry(f3,width=10,textvariable=self.sugar,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6Label=Label(f3,text="Tea",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6text=Entry(f3,width=10,textvariable=self.tea,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Drinks
        f4=LabelFrame(self.root,text ="Drinks",bg=bg_color,fg="gold",font=("times new roman",15, "bold"))
        f4.place(x=680,y=180,width=325,height=380)

        d1Label=Label(f4,text="Maza",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        d1text=Entry(f4,width=10,textvariable=self.maza,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        d2Label=Label(f4,text="Coco-Cola",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        d2text=Entry(f4,width=10,textvariable=self.cocaCola,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        d3Label=Label(f4,text="Frooti",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        d3text=Entry(f4,width=10,textvariable=self.frooti,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        d4Label=Label(f4,text="Thumbs-up",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        d4text=Entry(f4,width=10,textvariable=self.thumbsUp,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        d5Label=Label(f4,text="Limca",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        d5text=Entry(f4,width=10,textvariable=self.limca,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        d6Label=Label(f4,text="Sprite",font=("imes new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        d6text=Entry(f4,width=10,textvariable=self.sprite,font=("imes new roman",15,"bold"),bd=5,bg=bg_color,fg="white",relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # bill area
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1000,y=180,width=350,height=380)
        billTitle=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrolly=Scrollbar(f5,orien=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        f6=LabelFrame(self.root,text ="Bill Menu",bg=bg_color,fg="gold",font=("times new roman",15, "bold"))
        f6.place(x=0,y=560,relwidth=1,height=140)
        m1=Label(f6,text="Toal cosmetic Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1Text=Entry(f6,width=18,textvariable=self.cosmeticPrice,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(f6,text="Toal Grocery Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2Text=Entry(f6,width=18,textvariable=self.groceryPrice,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(f6,text="Toal Drink Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3Text=Entry(f6,width=18,textvariable=self.drinkPrice,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1=Label(f6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1Text=Entry(f6,width=18,textvariable=self.cosmeticTax,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(f6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2Text=Entry(f6,width=18,textvariable=self.groceryTax,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(f6,text="Drink Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3Text=Entry(f6,width=18,textvariable=self.drinkTax,font="arial 10 bold ",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btnFrame=Frame(f6,bd=7,relief=GROOVE)
        btnFrame.place(x=750,width=580,height=105)

        totalBtn=Button(btnFrame,text ="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gBillBtn=Button(btnFrame,text ="Generate Bill",command=self.billArea,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        ClearBtn=Button(btnFrame,text ="Clear",command=self.clearData,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        ExitBtn=Button(btnFrame,text ="Exit",command=self.exitApp,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcomeBill()
    def total(self):
        self.csp=self.soap.get()*40
        self.cfcp=self.faceCream.get()*120
        self.cfwp=self.faceWash.get()*60
        self.cspp=self.spray.get()*180
        self.cgp=self.gell.get()*140
        self.clp=self.lotion.get()*180
        self.totalCosmeticPrice=float(
                                    self.csp+
                                    self.cfcp+
                                    self.cfwp+
                                    self.cspp+
                                    self.cgp+
                                    self.clp

        )

        self.cosmeticPrice.set("Rs "+str(self.totalCosmeticPrice))
        self.cTax=round(self.totalCosmeticPrice*0.05,2)
        self.cosmeticTax.set("Rs "+str(self.cTax))

        self.grp=self.rice.get()*80
        self.gfop=self.foodOil.get()*180
        self.gdp=self.daal.get()*60
        self.gwp=self.wheat.get()*240
        self.gsp=self.sugar.get()*45
        self.gtp=self.tea.get()*150

        self.totalGroceryPrice=float(
                                    self.grp+
                                    self.gfop+
                                    self.gdp+
                                    self.gwp+
                                    self.gsp+
                                    self.gtp
        )

        self.groceryPrice.set("Rs "+str(self.totalGroceryPrice))
        self.gTax=round(self.totalGroceryPrice*0.05,2)
        self.groceryTax.set("Rs "+str(self.gTax))

        self.dmp=self.maza.get()*60
        self.dccp=self.cocaCola.get()*60
        self.dfp=self.frooti.get()*50
        self.dtup=self.thumbsUp.get()*45
        self.dlp=self.limca.get()*40
        self.dsp=self.sprite.get()*60

        self.totalDrinkPrice=float(
                                self.dmp+
                                self.dccp+
                                self.dfp+
                                self.dtup+
                                self.dlp+
                                self.dsp
                                    
        )

        self.drinkPrice.set("Rs "+str(self.totalDrinkPrice))
        self.dTax=round(self.totalDrinkPrice*0.05,2)
        self.drinkTax.set("Rs "+str(self.dTax))

        self.totalBill=float(
                        self.totalCosmeticPrice+
                        self.totalGroceryPrice+
                        self.totalDrinkPrice+
                        self.cTax+
                        self.gTax+
                        self.dTax
                        
                        )


    def welcomeBill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome Webcpode Retail")
        self.textarea.insert(END,f"\n Bill Number : {self.billNo.get()}")
        self.textarea.insert(END,f"\nCustomer Name : {self.cName.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.cphone.get()}")
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================")
    def billArea(self):

        if self.cName.get()=="" or self.cphone=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmeticPrice.get()=="Rs 0.0" and self.groceryPrice.get()=="Rs 0.0" and self.drinkPrice.get()=="Rs 0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:
            self.welcomeBill()

            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap \t\t{self.soap.get()}\t\t{self.csp}")
            if self.faceCream.get()!=0:
                self.textarea.insert(END,f"\n Face cream \t\t{self.faceCream.get()}\t\t{self.cfcp}")
            if self.faceWash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash \t\t{self.faceWash.get()}\t\t{self.cfwp}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair spray \t\t{self.spray.get()}\t\t{self.cspp}")
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair gell \t\t{self.gell.get()}\t\t{self.cgp}")
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n Body Loion \t\t{self.loion.get()}\t\t{self.clp}")

        
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice \t\t{self.rice.get()}\t\t{self.grp}")
            if self.foodOil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil \t\t{self.foodOil.get()}\t\t{self.gfop}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal \t\t{self.daal.get()}\t\t{self.gdp}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat \t\t{self.wheat.get()}\t\t{self.gwp}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar \t\t{self.sugar.get()}\t\t{self.gwp}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea \t\t{self.tea.get()}\t\t{self.gtp}")


            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Mazza \t\t{self.maza.get()}\t\t{self.dmp}")
            if self.cocaCola.get()!=0:
                self.textarea.insert(END,f"\n Coco-Cola \t\t{self.cocaCola.get()}\t\t{self.dccp}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti \t\t{self.frooti.get()}\t\t{self.dfp}")
            if self.thumbsUp.get()!=0:
                self.textarea.insert(END,f"\n Thumbs - Up \t\t{self.thumbsUp.get()}\t\t{self.dtup}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca \t\t{self.limca.get()}\t\t{self.dlp}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite \t\t{self.sprite.get()}\t\t{self.dsp}")

            self.textarea.insert(END,f"\n--------------------------------------")
            if self.cosmeticTax.get()!="Rs 0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax \t\t\t\t{self.cosmeticTax.get()}")
                self.textarea.insert(END,f"\n--------------------------------------")
            if self.groceryTax.get()!="Rs 0.0":
                self.textarea.insert(END,f"\n Grocery  Tax \t\t\t\t{self.groceryTax.get()}")
                self.textarea.insert(END,f"\n--------------------------------------")
            if self.drinkTax.get()!="Rs 0.0":
                self.textarea.insert(END,f"\n Drink Tax \t\t\t\t{self.drinkTax.get()}")
                self.textarea.insert(END,f"\n--------------------------------------")
            self.textarea.insert(END,f"\n Total price \t\t\t\t{self.totalBill}")
            self.textarea.insert(END,f"\n--------------------------------------")
            self.saveBill()
            


    def saveBill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.billData=self.textarea.get("1.0",END)
            f1=open("bills/"+str(self.billNo.get())+ ".txt","w")
            f1.write(self.billData)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no : {self.billNo.get()} is saved successfully")

        else:
            return
    def findBill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.searchBill.get():
                f1=open(f"bills/{i} ","r")
                self.textarea.delete("1.0",END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error ","Invalid bill no")


    def clearData(self):
        op=messagebox.askyesno("Clear","Do you want to clear the data")
        if op>0:
            
            self.soap.set(0)
            self.faceCream.set(0)
            self.faceWash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)

            self.rice.set(0)
            self.foodOil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            self.maza.set(0)
            self.cocaCola.set(0)
            self.frooti.set(0)
            self.thumbsUp.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            self.cosmeticPrice.set("")
            self.groceryPrice.set("")
            self.drinkPrice.set("")

            self.cosmeticTax.set("")
            self.groceryTax.set("")
            self.drinkTax.set("")

            self.cName.set("")
            self.cphone.set("")
            self.billNo.set("")
            x=randint(1000,9999)
            self.billNo.set(str(x))
            self.searchBill.set("")

            self.welcomeBill()

    def exitApp(self):
        op=messagebox.askyesno("Exit","Do you want to really exit")
        if op>0:
            self.root.destroy()






root=Tk()
obj=Bill_App(root)
root.mainloop()

