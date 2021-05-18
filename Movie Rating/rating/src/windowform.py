from tkinter import *
import MySQLdb
from time import time
import numpy as np
import cv2
from keras.preprocessing import image

root=Tk()
con = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='password', db='rating')
cmd = con.cursor()

root.geometry("600x600+350+40")
root.configure(bg="white")
root.title("SHOWS")
cmd.execute("select moviename from movie")
mov=cmd.fetchall()
OP=["choose your film"]
for d in mov:
    OP.append(d[0])
var=IntVar()
def rating(value):
    con=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='password',db='rating')
    cmd=con.cursor()
    cmd.execute("select id from movie where moviename='"+value+"'")
    x=cmd.fetchone()
    if x is not None:
        entry1.delete(0, last=END)
        entry1.insert(END, str(x[0]))
    #     check_emotion(x[0])

def insert():
    con=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='password',db='rating')
    cmd = con.cursor()
    # cmd.execute("select * from movie_review where id="+str(ide)+"")
def clear():

    entry1.delete(0,last=END)
    entry0.delete(0,last=END)
    var.set(OP[0])
def am1():
    s="11:00"
    entry0.insert(END,s)
def pm2():
    s="16:00"
    entry0.insert(END,s)
def pm3():
    s="21:00"
    entry0.insert(END,s)


paused = True


def startemo():
    fid=entry1.get()
    check_emotion(str(fid))

########################################################################################
def check_emotion(filmid):



    face_cascade = cv2.CascadeClassifier('static/model/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    # -----------------------------
    # face expression recognizer initialization
    from keras.models import model_from_json
    model = model_from_json(open("C:/Users/Murali/PycharmProjects/movie_flask/data.json", "r").read())
    model.load_weights('static/model/facial_expression_model_weights.h5')  # load weights

    # -----------------------------

    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'




    cmd.execute("select emotion,TIME(start_time),TIME(end_time) from storyboard where movieid='" + str(filmid) + "'")
    s = cmd.fetchall()
    # cur_time = display.cget("text")
    import datetime
    a = datetime.datetime.now().replace(microsecond=0)
    # a= entry0.get()
    print("a----",a)

    i = 0
    while (True):
        # time.sleep(1)
        i = i + 1



        ret, img = cap.read()
        # img = cv2.imread('C:/Users/IS96273/Desktop/hababam.jpg')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # print(faces) #locations of detected faces
        totalface = len(faces)
        noofcemo = 0

        flag = 0

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # draw rectangle to main image

            detected_face = img[int(y):int(y + h), int(x):int(x + w)]  # crop detected face
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)  # transform to gray scale
            detected_face = cv2.resize(detected_face, (48, 48))  # resize to 48x48

            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis=0)

            img_pixels /= 255  # pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

            predictions = model.predict(img_pixels)  # store probabilities of 7 expressions

            # find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
            max_index = np.argmax(predictions[0])

            emotion = emotions[max_index]

            b = datetime.datetime.now().replace(microsecond=0)
            # print("b----------",type(b))
            cur_diff = b - (a)
            # print("tpp===",type(cur_diff))

            print("curdiff---", cur_diff)

            for d in s:

                 if (d[1]) <= cur_diff <= (d[2]):
                    print("true=====")
                    flag = 1
                    if d[0] == emotion:
                        noofcemo = noofcemo + 1

            # write emotion text above rectangle
            cv2.putText(img, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # process on detected face end
        # -------------------------

        cv2.imshow('img', img)
        if flag == 1:
            rating=0
            if totalface>0:
                rating = (noofcemo / totalface) * 5
                cmd.execute("insert into rating_tbl values(null,'" + str(filmid) + "',curdate(),'" + str(rating) + "')")
                con.commit()
        if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
            break

    # kill open cv things
    cap.release()
    cv2.destroyAllWindows()


#########################################################################################



label1=Label(root,text="Movie :",font=("bold",10)).place(x=100,y=150)
op1=OptionMenu(root,var,*OP,command=rating)
op1.place(x=200,y=150)
var.set(OP[0])
label2=Label(root,text="Show :",font=("bold",10)).place(x=100,y=200)
button1=Button(root,text="11:00",bg="red",fg="white",command=am1)
button1.place(x=200,y=200)
button2=Button(root,text="16:00",bg="red",fg="white",command=pm2)
button2.place(x=280,y=200)
button3=Button(root,text="21:00",bg="red",fg="white",command=pm3)
button3.place(x=360,y=200)
entry1=Entry(root,width="12")
entry1.place(x=200,y=250)
entry0=Entry(root,width="8")
entry0.place(x=300,y=250)
button0=Button(root,text="CLEAR",bg="grey",fg="white",command=clear)
button0.place(x=370,y=150)
button4=Button(root,text="START",bg="orange",fg="white",command=startemo)
button4.place(x=230,y=300)




root.mainloop()