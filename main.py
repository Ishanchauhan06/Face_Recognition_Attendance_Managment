#  tkinter library is used for GUI making application and Python when combined with Tkinter provides a fast and easy way to create GUI applications
from cgitb import text
from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from Face_recognise import Face_Recoginition
from Attendance import AttendanceStu
from developer import Developer
from help import HelpDesk

class Face_Recoginition_System:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
 # For inserting the images
        img1 = Image.open(
            r"My_images\BestFacialRecognition.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
 # antilias converts high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(img1)

        firstlabel = Label(self.root, image=self.photoimg1)
        firstlabel.place(x=0, y=0, width=500, height=130)
  # 2nd image
        img2 = Image.open(
            r"My_images\facialrecognition.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        firstlabel = Label(self.root, image=self.photoimg2)
        firstlabel.place(x=500, y=0, width=500, height=130)
  # 3 image
        img = Image.open(
            r"My_images\images.jpg")
        img = img.resize((550, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        firstlabel = Label(self.root, image=self.photoimg)
        firstlabel.place(x=1000, y=0, width=550, height=130)


# bg image
        img3 = Image.open(
            r"My_images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bgimage = Label(self.root, image=self.photoimg3)
        bgimage.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bgimage, text="          FACE RECOGNITION SYSTEM FOR ATTENDANCE TRACKING", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        #  Timming
        def time():
            strtime = strftime('%H:%M:%S %p')
            lbl.config(text=strtime)
            lbl.after(1000, time)
        lbl =  Label(title_lbl, font=(
            "times new roman", 15, "bold"), bg="Darkblue", fg="white")
        lbl.place(x=0, y=0, width=110, height=45)
        time()
        

    # button for student details
        img4 = Image.open(
            r"My_images\students.jpeg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bgimage, command=self.Student_details, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bgimage, command=self.Student_details, text="Student Details", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

    # Button to detect a face

        img5 = Image.open(
            r"My_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bgimage, image=self.photoimg5, command=self.Face_data,cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bgimage, text="Face detector", command=self.Face_data,cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

    # button to attendace record

        img6 = Image.open(
            r"My_images\smart-attendance.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bgimage, image=self.photoimg6,command=self.attendancet ,cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bgimage, text="Attendance",command=self.attendancet ,cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

    #  Help button

        img7 = Image.open(
            r"My_images\help.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bgimage, image=self.photoimg7, cursor="hand2",command=self.Helpinfo)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bgimage, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white",command=self.Helpinfo)
        b1_1.place(x=1100, y=300, width=220, height=40)

    # For second row button we have 4 more buttons

    #   Button to train data set

        img8 = Image.open(
            r"My_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bgimage, image=self.photoimg8, cursor="hand2",command=self.Train_data)
        b1.place(x=200, y=390, width=220, height=220)

        b1_1 = Button(bgimage, text="Train Data",command=self.Train_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=590, width=220, height=40)

    #   Photos button

        img9 = Image.open(
            r"My_images\photogrp.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bgimage, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=390, width=220, height=220)

        b1_1 = Button(bgimage, text="Photos", cursor="hand2",command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=590, width=220, height=40)

    # #   Developer's button

        img12 = Image.open(
            r"My_images\developers.jpg")
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bgimage, image=self.photoimg12, cursor="hand2", command=self.DeveloperRec)
        b1.place(x=800, y=390, width=220, height=220)

        b1_1 = Button(bgimage, text="Developer", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=590, width=220, height=40)

    #   Chat bot

        # img10 = Image.open(
        #     r"My_images\chat.jpg")
        # img10 = img10.resize((220, 220), Image.ANTIALIAS)
        # self.photoimg10 = ImageTk.PhotoImage(img10)

        # b1 = Button(bgimage, image=self.photoimg10, cursor="hand2")
        # b1.place(x=800, y=390, width=220, height=220)

        # b1_1 = Button(bgimage, text="Chat bot", cursor="hand2", font=(
        #     "times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b1_1.place(x=800, y=590, width=220, height=40)

     # Exit button

        img11 = Image.open(
            r"My_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bgimage, image=self.photoimg11, cursor="hand2",command=self.isExit)
        b1.place(x=1100, y=390, width=220, height=220)

        b1_1 = Button(bgimage, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white",command=self.isExit)
        b1_1.place(x=1100, y=590, width=220, height=40)

    def open_img(self):
        os.startfile("data")
        
    def isExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You sure to Exit!",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


# *************function button*************

    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    
    def Train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
         
    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recoginition(self.new_window)
         
    def attendancet(self):
        self.new_window=Toplevel(self.root)
        self.app=AttendanceStu(self.new_window)
    
    def DeveloperRec(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
         
    def Helpinfo(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window)
         
        


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition_System(root)
    root.mainloop()
