from tkinter import*
from tkinter import ttk
# from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import json


class Face_Recoginition:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=60)
        #  1st image
        img_top = Image.open(
            r"My_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        firstlabel = Label(self.root, image=self.photoimg_left)
        firstlabel.place(x=0, y=47, width=655, height=750)

        img_bottom = Image.open(
            r"My_images\Facey.jpg")
        img_bottom = img_bottom.resize((900, 700), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        firstlabel = Label(self.root, image=self.photoimg_bottom)
        firstlabel.place(x=655, y=47, width=900, height=750)

        # button for Face recognition

        b1_1 = Button(firstlabel, text="Recognise Face Here", command=self.Recognise_face, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=300, y=615, width=280, height=70)

        # *** Face Recognition***

    def Recognise_face(self):
        def draw_bound(img, classifier, ScaleFactor, minneighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, ScaleFactor, minneighbour)

            coord = []  # coordinates array

            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Ishan@2506", database="face_recognitiondb")
                my_cursor = conn.cursor()
                
                my_cursor.execute(
                    "select Name from student where StudentID="+str(id))
                i = my_cursor.fetchone()
                # To check which data is fetched through database
                with open('myfile.json','w',encoding='utf8') as json_file:
                    json.dump(id,json_file)
                
                i = "+".join(i)

                my_cursor.execute(
                    "select Dept from student where StudentID="+str(id))
                j = my_cursor.fetchone()
                j="+".join(j)

                my_cursor.execute(
                    "select Year from student where StudentID="+str(id))
                k = my_cursor.fetchone()
                k="+".join(k)

                my_cursor.execute(
                    "select MailId from student where StudentID="+str(id))
                l = my_cursor.fetchone()
                l = "+".join(l)

                if confidence > 77:
                    cv2.putText(
                        img, f"Name:{i}", (x, y-60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Dept:{j}", (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Year:{k}", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Mailid:{l}", (x, y+5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_bound(img, faceCascade, 1.1, 10,
                               (255, 255, 255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_captu = cv2.VideoCapture(0)

        while True:
            ret,img = video_captu.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_captu.release()
        cv2.destroyAllWindows()
        



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition(root)
    root.mainloop()
