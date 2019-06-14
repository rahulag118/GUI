from tkinter import*
import tkinter.messagebox
from PIL import ImageTk,Image
import sqlite3
from scrolling_area import*

root=Tk()
root.geometry("1366x768+0+0")
root.title("student account")
root.resizable(0,0)
root.config(bg="powder blue")
def home():
    f1=Frame(root,width=1366,height=768,bg="powder blue")
    img = ImageTk.PhotoImage(Image.open('2_730.jpg'))
    Label(f1, image=img, width=1366, height=768).place(x=0, y=0)
    f1.pack()
    b1= Button(f1,text="ADD",bd=5,width=12,height=2,command=lambda :add(f1,root))
    b1.place(x=400,y=60)
    b2= Button(f1,text="SHOW",bd=5,width=12,height=2,command=lambda :show(f1,root))
    b2.place(x=800,y=60)
    f1.mainloop()
def add(f1,root):
    f1.destroy()
    f2=Frame(root,width=1366,height=768,bg="pink")
    img=ImageTk.PhotoImage(Image.open('3_.jpg'))
    Label(f2, image=img, width=1366, height=768).place(x=0, y=0)
    f2.pack()
    l1=Label(f2,text="Name",bd=5,font=('arial',15,'bold'),width=8)
    l1.place(x=30,y=20)
    l2=Label(f2,text="Course",font=('arial',15,'bold'),width=8)
    l2.place(x=30,y=80)
    l3 = Label(f2, text="Email", font=('arial', 15, 'bold'), width=8)
    l3.place(x=30,y=140)
    l4= Label(f2, text="College", bd=5,font=('arial', 15, 'bold'), width=8)
    l4.place(x=30,y=200)
    l5 = Label(f2, text="Contact No", bd=5, font=('arial', 15, 'bold'), width=8)
    l5.place(x=30,y=260)
    e1=Entry(f2,bd=10,width=29,bg="white",textvariable=StringVar())
    e1.place(x=200,y=20)
    #e2=Entry(f2, bd=10,width=29,bg="white")
    #e2.place(x=200,y=80)
    variable = StringVar(f2)
    variable.set('Python')
    e2 = OptionMenu(f2, variable, 'Python', 'Java', 'Machine Learning', 'Android', 'Cloud Computing')
    e2.config(width='24')
    e2.place(x=200, y=80)
    e3=Entry(f2, bd=10, width=29, bg="white",textvariable=StringVar())
    e3.place(x=200,y=140)

    e4=Entry(f2, bd=10, width=29, bg="white",textvariable=StringVar())
    e4.place(x=200,y=200)
    e5=Entry(f2, bd=10, width=29, bg="white",textvariable=IntVar())
    e5.place(x=200,y=260)
    b1=Button(f2,text='SUBMIT',bd=5,width=12,height=2,command=lambda :submit(f2,root,e1,variable,e3,e4,e5))
    b1.place(x=50,y=350)
    b2 = Button(f2, text='RESET', bd=5, width=12, height=2,command=lambda :add(f2,root))
    b2.place(x=250, y=350)
    b3 = Button(f2, text='BACK', bd=5, width=12, height=2,command=lambda :back(f2,root))
    b3.place(x=450, y=350)
    f2.mainloop()

def show(f1,root):
    f1.destroy()
    f3=Frame(root,width=1366,height=768,bg='black')
    img=ImageTk.PhotoImage(Image.open('9.jpg'))
    Label(f3, image=img, width=1366, height=768).place(x=0, y=0)
    f3.pack()
    a=IntVar()
    b=IntVar()
    c=IntVar()
    d=IntVar()
    e=IntVar()
    c1=Checkbutton(f3,text='python',variable=a,onvalue=1,offvalue=0,height=2,width=8,font=('arial', 15, 'bold'),bg='black',fg='red')
    c1.place(x=100,y=60)
    c2 = Checkbutton(f3, text='Java', variable=b, onvalue=1, offvalue=0, height=2, width=5,font=('arial', 15, 'bold'), bg='black', padx=0,fg='red')
    c2.place(x=100, y=140)
    c3 = Checkbutton(f3, text='Machine Learning', variable=c, onvalue=1, offvalue=0, height=2,font=('arial', 15, 'bold'), width=14, bg='black', fg='red')
    c3.place(x=100, y=220)
    c4 = Checkbutton(f3, text='Android', variable=d, onvalue=1, offvalue=0, height=2, width=8, font=('arial', 15, 'bold'),bg='black', fg='red')
    c4.place(x=100, y=300)
    c5 = Checkbutton(f3, text='Cloud Computing', variable=e, onvalue=1, offvalue=0, height=2, width=14,font=('arial', 15, 'bold'), bg='black',padx=0, fg='red')
    c5.place(x=100, y=380)
    b1 = Button(f3, text="OK", bd=5, width=12, height=2,command=lambda :ok(f3,root,a,b,c,d,e))
    b1.place(x=150, y=550)
    b2 = Button(f3, text="RESET", bd=5, width=12, height=2, command=lambda: show(f3, root))
    b2.place(x=300, y=550)
    b3 = Button(f3, text="BACK", bd=5, width=12, height=2, command=lambda: back(f3,root))
    b3.place(x=450, y=550)
    f3.mainloop()
def back(f2,root):
    f2.destroy()
    home()
def submit(f2,root,e1,e2,e3,e4,e5):
    a=e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()
    print(a,b,c,d,e)
    con=sqlite3.connect("ZEETRON")
    con.execute("create table if not exists Zeetron1(Name char[20],Course char[20],Email char[50],College char[50],Contact  int[10])")
    query="insert into Zeetron1(Name,Course,Email,College,Contact )values('{}','{}','{}','{}',{})".format(a,b,c,d,e)
    i=con.execute(query)
    con.commit()
    m=con.execute("select * from Zeetron1")
    print("successfully inserted ")
    print(list(m))
    tkinter.messagebox.showinfo("successfully","successfully inserted data into database")
    con.close()
def ok(f3,root,a,b,c,d,e):
    f3.destroy()
    frame4=Frame(root,width=1366,height=768,bg="powder blue")
    f1=a.get()
    f2=b.get()
    f3a = c.get()
    f4 = d.get()
    f5 = e.get()
    print(f1,f2,f3a,f4,f5)
    con=sqlite3.connect("ZEETRON")
    frame4.pack()
    scrolling_area=Scrolling_Area(frame4,height=220,width=1366)
    scrolling_area.place(x=0,y=0)
    table=Table(scrolling_area.innerframe,
                ["Name","Course","Email","College","Contact"],
                column_minwidths=[270,270,270,270,260])
    table.pack(expand=True, fill=X)
    table.on_change_data(scrolling_area.update_viewport)
    text_area=Text(frame4,width=200,height=20,bd=10,bg="white")
    text_area.insert(INSERT,"")
    text_area.place(x=0,y=250)
    if f1==1:
        o1=con.execute("select* from Zeetron1 ")
        con.commit()
        data=[]
        for row in o1:
            column=[]
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)
    if f2 == 1:
        o2 = con.execute("select* from Zeetron1 where Course='Java'")
        con.commit()
        data = []
        for row in o2:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)
    if f3a == 1:
        o3 = con.execute("select* from Zeetron1 where Course='Machine learning'")
        con.commit()
        data = []
        for row in o3:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f4 == 1:
        o4 = con.execute("select* from Zeetron1 where Course='Android'")
        con.commit()
        data = []
        for row in o4:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)
    if f5 == 1:
        o5 = con.execute("select* from Zeetron1 where Course='Cloud Computing'")
        con.commit()
        data = []
        for row in o5:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    b3 = Button(frame4, text="BACK", bd=5, width=12, height=2, command=lambda: back(frame4,root))
    b3.place(x=160, y=600)
    b4 = Button(frame4, text="SEND MAIL", bd=5, width=12, height=2)
    b4.place(x=20, y=600)
    #frame4.mainloop()




home()