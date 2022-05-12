from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np

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
        title_lbl.place(x=0, y=0, width=1530, height=45)
        #  1st image
        img_top = Image.open(
            r"My_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        firstlabel = Label(self.root, image=self.photoimg_left)
        firstlabel.place(x=0, y=47, width=655, height=750)

         
        img_bottom= Image.open(
            r"My_images\Facey.jpg")
        img_bottom = img_bottom.resize((900, 700), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        firstlabel = Label(self.root, image=self.photoimg_bottom)
        firstlabel.place(x=655, y=47, width=900, height=750)
        
        # button for Face recognition
         
        b1_1 = Button(firstlabel, text="Recognise Face Here" ,cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=300, y=615, width=280, height=70)
        
        # *** FAce REcognition***
    
    def Recognise_face(self):
        def draw_bound(img,classifier,ScaleFactor,minneighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,ScaleFactor,minneighbour)
            
            coord=[] # coordinates array
            
            for(x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence= int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Ishan@2506", database="face_recognitiondb")
                my_cursor = conn.cursor()
                
                
                if confidence>77:
                    
                
            
            
       





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition(root)
    root.mainloop()
