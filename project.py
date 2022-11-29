from tkinter import *
from PIL import Image,ImageTk
import time
import mysql.connector
import tkinter.messagebox as tmsg

db1 = mysql.connector.connect(host="localhost",user="root",password="your password",database = "vaccine")
p=1
z=0
w=0
def start():
    global root
    root=Tk()
    root.title('ANSH GUI')
    root.geometry('1800x1200')
    x=Image.open(r"C:\Users\ansha\OneDrive\Desktop\oip.png")
    y=ImageTk.PhotoImage(x)
    label=Label(image=y)
    label.pack()
    Label(root,text='Covid Management System',font='segoe 30 italic',fg='black',bg='pink',padx=90).place(x=280,y=20)
    Label(root,text='Copyright(Ansh Agarwal) ',font='segoe 15 bold',fg='black',bg='cyan').place(x=490,y=600)
    b1=Button(root,fg='black',text='Add  Member',bd=3,padx=50,bg='coral',font='comicsansms 15 bold',command=addmember)
    b1.place(x=490,y=200)
    b2=Button(root,fg='black',text='Add Vaccination Record',bd=1,padx=50,bg='coral',font='comicsansms 15 bold',command=addvaccine)
    b2.place(x=450,y=270)
    b3=Button(root,fg='black',text='Member Info.',bd=1,padx=50,bg='coral',font='comicsansms 15 bold',command=showmember)
    b3.place(x=490,y=340)
    b4=Button(root,fg='black',text='Vaccinated Member Info.',bd=1,padx=40,bg='coral',font='comicsansms 15 bold',command=vaccineinfo)
    b4.place(x=450,y=410)
    b5=Button(root,fg='black',text='Quit',bd=1,padx=40,bg='coral',font='comicsansms 15 bold',command=Quit1)
    b5.place(x=540,y=480)
    root.mainloop()
    
    
    
def check():
    global db1
    a=e1.get()
    b=e2.get()
    #print(a,b)
    
    c2 = db1.cursor()
    q = "select * from users where username = %s and passw = %s"
    val = (a,b)
    c2.execute(q,val)
    res = c2.fetchall()
    if len(res)>=1:
        Label(root1,text='Acess Granted',font='segoe 12 bold',fg='black',bg='pink').place(x=570,y=350)
        root1.destroy()
        time.sleep(2)
        start()
    else:
        tmsg.showerror('Error','Incorrect Username or Password')
       
        
        
        
    #print(res)



def login():
    global e1,e2,root1
    root1=Tk()
    root1.title('ANSH GUI')
    root1.geometry('1800x1200')
    x=Image.open(r"C:\Users\ansha\OneDrive\Desktop\cov2.jpg")
    y=ImageTk.PhotoImage(x)
    label=Label(image=y)
    label.pack()
    Label(root1,text='LOGIN',font='segoe 35 bold',fg='black',bg='green2',padx=90).place(x=480,y=50)
    Label(root1,text='Username-',font='segoe 15 bold',fg='black',bg='yellow').place(x=480,y=250)
    e1=Entry(root1,font='segoe 13 bold',bd=3,fg='red')
    e1.place(x=600,y=250)
    Label(root1,text='Password-',font='segoe 15 bold',fg='black',bg='yellow').place(x=480,y=300)
 
    e2=Entry(root1,font='segoe 13 bold',show="*",bd=3,fg='red')
    e2.place(x=600,y=300)
    b1=Button(root1,fg='black',text='Submit',bd=3,padx=10,bg='coral',font='comicsansms 15 bold',command=check)
    b1.place(x=570,y=380)
    Label(root1,text='Copyright(Ansh Agarwal) ',font='segoe 15 bold',fg='black',bg='cyan').place(x=490,y=600)
    
   
    root1.mainloop()

def addmember():
    global root2,e3,e4,e5,e6,e7,e8,z
    root.destroy()
    root2=Tk()
    root2.title('ANSH GUI')
    root2.geometry('1800x1200')
    x=Image.open(r"C:\Users\ansha\OneDrive\Desktop\cov5.jpg")
    y=ImageTk.PhotoImage(x)
    label=Label(image=y)
    label.pack()
    Label(root2,text='ADD MEMBER',font='segoe 30 bold',fg='black',bg='yellow',padx=90).place(x=410,y=50)
    Label(root2,text='Name-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=220)
    Label(root2,text='Address-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=270)
    Label(root2,text='Phone No.-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=320)
    Label(root2,text='Email-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=370)
    Label(root2,text='Age-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=420)
    Label(root2,text='Aadhar No.-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=470)
    e3=Entry(root2,font=35)
    e3.place(x=580,y=220)
    e4=Entry(root2,font=35)
    e4.place(x=580,y=270)
    e5=Entry(root2,font=35)
    e5.place(x=580,y=320)
    e6=Entry(root2,font=35)
    e6.place(x=580,y=370)
    e7=Entry(root2,font=35)
    e7.place(x=580,y=420)
    e8=Entry(root2,font=35,show="*")
    e8.place(x=580,y=470)
    
    b1=Button(root2,fg='black',text='Back',bd=3,padx=10,bg='coral',font='comicsansms 15 bold',command=back)
    b1.place(x=500,y=530)
    b2=Button(root2,fg='black',text='Submit',bd=3,padx=10,bg='coral',font='comicsansms 15 bold',command=check1)
    b2.place(x=620,y=530)
    z=1    
   
    root2.mainloop()

def back():
    global p,w
    if z==1:
        root2.destroy()
    if z==2:
        p=1
        root3.destroy()
    if z==3:
        root4.destroy()
    if z==4:
        w=0
        root5.destroy()
    time.sleep(0.5)
    start()

def check1():
    
    x=0
    print(e8.get(),e3.get(),e4.get(),e6.get(),e5.get(),e7.get())
    a=(e5.get())
    b=(e6.get())
    c=(e7.get())
    d=(e8.get())
    if len(e3.get())>=3 and len(e4.get())>=4 and len(str(a))==10 and '@gmail.com' in b and len(str(c))<4 and len(str(d))==12:
        if int(e5.get()) and int(e7.get()) and int(e8.get()):
               x=1
    else:
        tmsg.showerror('Error','Enter Valid format')
        
        
    
    
    
    
    if x==1:
        c1 = db1.cursor()
        q = "insert into member values (%s,%s,%s,%s,%s,%s)"
        val =(e8.get(),e3.get(),e4.get(),e6.get(),e5.get(),e7.get())
        c1.execute(q,val)
        #Label(root2,text='Sucessful...',font='segoe 15 bold',fg='black',bg='seagreen1',padx=0).place(x=550,y=580)
        db1.commit()
        tmsg.showinfo('Help','Member Added Sucessfully')
        time.sleep(2)
        root2.destroy()
    
        
        start()
    
def showmember():
    global root3,z,e12
    root.destroy()
    root3=Tk()
    root3.title('ANSH GUI')
    root3.geometry('1800x1200')
    x=Image.open(r"C:\Users\ansha\OneDrive\Desktop\cov3.jpg")
    y=ImageTk.PhotoImage(x)
    label=Label(image=y)
    label.pack()
    Label(root3,text='Member Info..',font='papyrue 25 bold',bg='black',fg='red',padx=10,pady=0).place(x=520,y=30)
    Label(root3,text='Name-',font='papyrue 15 bold',bg='black',fg='red',padx=0,pady=0).place(x=480,y=100)
    e12=Entry(root3,font='segoe 13 bold',bd=3,fg='red')
    e12.place(x=560,y=99)
    Label(root3,text='',font='papyrue 25 bold',bg='black',fg='red',padx=350,pady=200).place(x=300,y=150)

    b1=Button(root3,fg='black',text='Back',bd=3,padx=10,bg='coral',font='comicsansms 15 bold',command=back)
    b1.place(x=600,y=600)
    b2=Button(root3,fg='yellow',text='Submit',bd=3,padx=0,bg='black',font='comicsansms 10 bold',command=check3)
    b2.place(x=780,y=97)
    
    #for val in res:
     #   print("Name = "+val[1] + " Aadhar Card= " + val[0])
    z=2
    root3.mainloop()
    
    
def addvaccine():
    global c1,c2,e9,e10,e11,root4,z
    root.destroy()
    root4=Tk()
    root4.title('ANSH GUI')
    root4.geometry('1800x1200')
    x=Image.open(r"C:\Users\ansha\OneDrive\Desktop\cov5.jpg")
    y=ImageTk.PhotoImage(x)
    label=Label(image=y)
    label.pack()
    Label(root4,text='Vaccination Record-',font='segoe 25 bold',fg='black',bg='wheat1',padx=0).place(x=450,y=50)
    #Label(root4,text='Aadhar No.-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=470)
    Label(root4,text='Aadhar No.-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=220)
    Label(root4,text='Vaccine Name-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=450,y=280)
    Label(root4,text='Date of Vaccination-',font='segoe 15 bold',fg='black',bg='pink',padx=0).place(x=430,y=340)
    Label(root4,text='(yyyy-mm-dd)',font='segoe 10 bold',fg='black',bg='pink',padx=0).place(x=480,y=375)
    e9=Entry(root4,font='segoe 13 bold',bd=3,fg='red')
    e9.place(x=630,y=220)
    e10=Entry(root4,font='segoe 13 bold',bd=3,fg='red')
    e10.place(x=630,y=280)
    e11=Entry(root4,font='segoe 13 bold',bd=3,fg='red')
    e11.place(x=630,y=340)
    c1=IntVar()
    c2=IntVar()
    
    b1=Checkbutton(root4,text='Dose1',font='segoe 13 bold',variable=c1,bg='orchid1',pady=5,bd=3).place(x=550,y=400)
    b2=Checkbutton(root4,text='Dose2',font='segoe 13 bold',variable=c2,bg='orchid1',pady=5,bd=3).place(x=650,y=400)
    b3=Button(root4,fg='black',text='Back',bd=3,padx=10,bg='coral',font='comicsansms 15 bold',command=back)
    b3.place(x=500,y=450)
    b4=Button(root4,fg='black',text='Submit',bd=3,padx=10,bg='coral',font='comicsansms 15 bold',command=check2)
    b4.place(x=620,y=450)
    z=3
    root4.mainloop()
    
    
def check2():
    d1=None
    d2=None
    access=None
    v2=0
    v3=0
    d,e,a,b,c= c1.get(),c2.get(),e9.get(),e10.get(),e11.get()
    #print(a,b,c,d,e)
    if d==1 and e==0:
        d1=1
    elif e==1 and d==0:
        d2=1
    else:
        tmsg.showerror('Error','Select One Dose Only')
    if d1==1 or d2==1:
        if len(a)==12 and b.lower() in ['sputnik','covidshield','covaxin'] and len(c)==10:
            #print('true')
            access=1
        else:
            tmsg.showerror('Error','Enter Correct Fomat')
    if v2==0:
         q = "select * from vaccination where aadharno = %s "
         val = (a,)
         c3 = db1.cursor()
         c3.execute(q,val)
         res = c3.fetchall()
         #print(len(res))
         if d1==1:
             if len(res)>=1:
                 v2+=2
                 tmsg.showerror('help','already registerd')
             else:
                 pass
         if d2==1:
             print(res)
             if len(res)==0:
                 tmsg.showwarning('Warning','Not Registerd for Dose1')
                 v3+=1
             
                
            
        
    
    if access==1 and v2==0 and v3==0:
        q = "select * from member where aadharno = %s "
        val = (a,)
        c3 = db1.cursor()
        c3.execute(q,val)
        res = c3.fetchall()
        #print(len(res))
        if len(res)>=1:
            if d1==1:
                q = "insert into vaccination values(%s,%s,%s,NULL)"
                val = (a,b,c)
                c3.execute(q,val)
                db1.commit()
                tmsg.showinfo('Help','Vaccination Record Added Sucessfully')
                root4.destroy()
                time.sleep(2)
                start()
            else:
                q1="select aadharno from vaccination where dose2 is null and  aadharno=%s"
                val=(a,)
                c3.execute(q1,val)
                res=c3.fetchall()
                if len(res)==1:
                    q = "update vaccination set dose2=%s where aadharno=%s"
                    val =(c,a)
                    c3.execute(q,val)
                    db1.commit()
                    tmsg.showinfo('Help','Vaccination Record Updated Sucessfully')
                    root4.destroy()
                    time.sleep(2)
                    start()
                else:
                    tmsg.showinfo('help','Already Regestired for Dose2')
        else:
            tmsg.showwarning('Warning','First Add Member Info')
        
    
    
    
def check3():
    global l4,p
    a=e12.get()
    #print(a)
    
    st='       Aadhar No. \t            Name           Address               Mob No.'
    c1 = db1.cursor()
    q="select * from member where name like '"+a+"%'"
    #print(q)
    c1.execute(q)
    result = c1.fetchall()
    #print(result)
    if len(result)>=1 and len(a)>=1 and p==1 :
        Label(root3,text=st,font='papyrue 15 bold',bg='black',fg='red',padx=0,pady=0).place(x=300,y=180)
        a=0
        for res in result:
            a+=30
            res1=(res[0],res[1],res[2],res[4])
            for i in range(4):
                lst=[0,1,2,4]
                v=lst[i]
                if i==0:
                    l4=Label(root3,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l4.place(x=330,y=200+a)
                elif i==1:
                    l4=Label(root3,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l4.place(x=540,y=200+a)
                elif i==2:
                    l4=Label(root3,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l4.place(x=670,y=200+a)
                else:
                    l4=Label(root3,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l4.place(x=820,y=200+a)
        
        p=0
        

    else:
        if p==0:
            tmsg.showwarning('Warning','Back, Try Again')
        else:
            tmsg.showerror('Error','Enter the Name')
    
    
    
    
def vaccineinfo():
    global e13,root5,z
    root.destroy()
    root5=Tk()
    root5.title('ANSH GUI')
    root5.geometry('1800x1200')
    x=Image.open(r"C:\Users\ansha\OneDrive\Desktop\cov3.jpg")
    y=ImageTk.PhotoImage(x)
    label=Label(image=y)
    label.pack()
    Label(root5,text=' Vaccinated Member Info..',font='papyrue 25 bold',bg='black',fg='yellow',padx=10,pady=0).place(x=430,y=30)
    Label(root5,text='Name-',font='papyrue 15 bold',bg='black',fg='yellow',padx=0,pady=0).place(x=480,y=100)
    e13=Entry(root5,font='segoe 13 bold',bd=3,fg='red')
    e13.place(x=560,y=99)
    Label(root5,text='',font='papyrue 25 bold',bg='black',fg='green2',padx=350,pady=200).place(x=300,y=150)

    b1=Button(root5,fg='black',text='Back',bd=3,padx=10,bg='coral',font='comicsansms 15 bold',command=back)
    b1.place(x=600,y=600)
    b2=Button(root5,fg='red',text='Submit',bd=3,padx=0,bg='black',font='comicsansms 10 bold',command=check4)
    b2.place(x=780,y=97)
    z=4
    root5.mainloop()
    
    
def check4():
    global w
    a=e13.get()
    st='   Aadhar No. \t      Name                     Vname           Dose1               Dose2'
    c1 = db1.cursor()
    q="select m.name,v.aadharno,v.vname,v.dose1,v.dose2 from vaccination v,member m where name like '"+a+"%'" +"and m.aadharno=v.aadharno"
    #print(q)
    c1.execute(q)
    result = c1.fetchall()
    print(result)
    if len(result)>=1 and len(a)>=1 and w==0:
        Label(root5,text=st,font='papyrue 14 bold',bg='black',fg='red',padx=0,pady=0).place(x=300,y=180)
        a=0
        for res in result:
            a+=30
            res1=(res[0],res[1],res[2],res[3],res[4])
            for i in range(5):
                lst=[0,1,2,3,4]
                v=lst[i]
                if i==0:
                    l5=Label(root5,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l5.place(x=500,y=200+a)
                    
                elif i==1:
                    l5=Label(root5,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l5.place(x=310,y=200+a)
                elif i==2:
                    l5=Label(root5,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l5.place(x=640,y=200+a)
                elif i==3:
                    l5=Label(root5,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l5.place(x=770,y=200+a)
                    
                else:
                    l5=Label(root5,text=res[v],font='papyrue 12 bold',bg='black',fg='red',padx=10,pady=0)
                    l5.place(x=880,y=200+a)
        w=1
    else:
         if w==1:
            tmsg.showwarning('Warning','Back, Try Again')
         elif len(result)==0:
             tmsg.showerror('Error','Not Found')
         else:
            tmsg.showerror('Error','Enter the Name')
    
        
    
def Quit1():
    root.destroy()

login()
    
    
