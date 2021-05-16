import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

import PIL
from PIL import Image, ImageTk


# from src.login1 import  log
import MySQLdb

# from src.loginn import log

con=MySQLdb.connect(host='localhost',user='root',passwd="root",port=3308,db="rating")
cmd=con.cursor()

a1=None
global iddd
def login11(uid):
    print(uid)
    global iddd
    iddd= uid
    vhome = Tk()
    vhome.geometry('900x900+350+90')
    global  a1
    z = StringVar()
    q=StringVar()
    v = IntVar()



    def search():

        postt = combo4.get()

        print("post-----", postt)

        with open('post.txt', 'w') as f:
            f.write(postt)

        # cmd.execute("SELECT `pnlist` FROM `panel` ")
        # plist= cmd.fetchall()
        #
        #
        # print("plist-----------",plist)
        phase1st = []

        # for pp in plist:


        cmd.execute("SELECT `L_ID` FROM `college`")
        clg = cmd.fetchall()


        for cc in clg:
            print("cc------------", cc)

            cmd.execute(" select * from movie")
            res = cmd.fetchone()

            print("res----------",res)



            if res[0] is not None:

                print("eeeee",str(res[0]))
                row=[]

                row.append(str(res[0]))
                row.append(str(res[2]))
                row.append(str(res[3]))
                phase1st.append(row)


        print("phaselist---------",phase1st)




        i=0.0
        img=[]

        k=0
        for d in phase1st:
            print("d----",d)
            global id
            # global vhome
            id=d[0]
            a3=Label(vhome,text=d[1])
            a3.place(relx=0.155,rely=(0.15*i)+0.2)

            ########################################
            # print("C:\\Users\\rahee\PycharmProjects\\vote\\src\\static\\symbol\\"+d[1])
            # img.append(PhotoImage(file=r"C:\Users\rahee\PycharmProjects\vote\src\static\symbol\\"+d[1]))
            # canvas = tkinter.Label(vhome,image=img[k], width=100, height=100)
            # k+=1
            # print('haaaaai', type(canvas))
            # # cn = canvas.create_image(20, 20, anchor=NW, )
            # canvas.place(relx=0.455,rely=(0.15*i)+0.5)
            #

            a4 = Label(vhome, text=d[2])
            a4.place(relx=0.455, rely=(0.15 * i) + 0.2)


            qw = Radiobutton(vhome,variable=v, value=int(d[0]))
            qw.place(relx=0.675, rely=(0.15*i)+0.2)
            i=i+1.0

        vhome.mainloop()

    # b1=Button(vhome,text="Search",command=search())
    # b1.place(relx=0.675,rely=0.1)




    l1=Label(vhome,text="TIMER", fg="black" ,font=(None, 13) )
    l1.place(relx=0.155,rely=0.1)





    q1=Label(vhome,text="POST",fg="black" ,font=(None, 13))
    q1.place(relx=0.455,rely=0.1)


    # search()




    def countdown():
        remaining = 0
        countdown(10)
        if remaining is not None:
            remaining = remaining

        if remaining <= 0:
            l5.configure(text="time's up!")
        else:
            l5.configure(text="%d" % remaining)
            remaining = remaining - 1
            after(1000, countdown)

    l5 = Label(vhome, text="",width=10, )
    l5.place(relx=0.20, rely=0.05)

    cmd.execute("SELECT moviename  FROM `movie`")
    s = cmd.fetchall()

    combo4 = Combobox(vhome, values=s)
    # combo4.bind("<<ComboboxSelected>>", justamethod())
    combo4.place(relx=0.30, rely=0.05)
    combo4.current(0)

    b1 = Button(vhome, text="START", command=search)
    b1.place(relx=0.50, rely=0.05)

    vhome.mainloop()
login11(14)
