from ast import Delete
from email import message
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np

class Train:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        title_lbl = Label(self.root, text="Train Data Set", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
          # inserting image for top 
        img_top = Image.open(
            r"My_images\facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        firstlabel = Label(self.root, image=self.photoimg_left)
        firstlabel.place(x=0, y=48, width=1530, height=325)
        # button for train data
         
        b1_1 = Button(self.root, text="Train Data", command=self.train_clasifier, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=360, width=1530, height=80)

          # inserting image for bottom
        img_bottom= Image.open(
            r"My_images\smart-attendance.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        firstlabel = Label(self.root, image=self.photoimg_bottom)
        firstlabel.place(x=0, y=440, width=1530, height=325)
       
        
        # 
    def train_clasifier(self):
        data_dir=("data")
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]  #list comprehensing
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') # Grey scale image conversion
            imagenp = np.array(img,'uint8')  #uint datatype
            id=int(os.path.split(image)[1].split('.')[1])
         # C:\Users\hp\OneDrive\Desktop\AttendanceSystemFaceRecognition\Face_Recognition_Attendance_Managment\data\user
            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #  ********* Training Classifier and save***********
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data set Completed!")
            
         
        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

