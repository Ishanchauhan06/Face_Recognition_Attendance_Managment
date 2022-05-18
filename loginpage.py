from datetime import datetime
# from fcntl import F_GET_SEALS
from tkinter import*
from tkinter import ttk
# from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np
import json

class LoginWindow:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")
        
        img = Image.open(
            r"My_images\loginbg.jpg")
        img = img.resize((1530, 790), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg = ImageTk.PhotoImage(img)

        bgimage = Label(self.root, image=self.photoimg)
        bgimage.place(x=0, y=13, relwidth=1, relheight=1)

        title_lbl = Label(self.root, text=" LOGIN ", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1540, height=45)
        
        frame = Frame(self.root, bg="black")
        frame.place(x=610,y=170, width=340, height=450)
        
        
        img2 = Image.open(
            r"My_images\character.png")
        img2 = img2.resize((200, 200), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)
        firstlabel = Label(image=self.photoimg2,bg="black",borderwidth=0)
        firstlabel.place(x=675, y=90, width=200, height=200)
        
        get_started=Label(frame,text="Face Recognition Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_started.place(x=35,y=130)
        
        # Label
        Username_label = Label(frame, text="Username: ",
                           font=("time new roman", 15, "bold"),fg="white", bg="black")
        Username_label.place(x=55,y=170)
        # Entry fill
        self.User_entry = ttk.Entry(
            frame, width=20, font=("time new roman", 15, "bold"))
        self.User_entry.place(x=35,y=200,width=280)
        # icon
        img3 = Image.open(
            r"My_images\LoginIconAppl.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg3 = ImageTk.PhotoImage(img3)
        firstlabel = Label(image=self.photoimg3,bg="black",borderwidth=0)
        firstlabel.place(x=640, y=340, width=25, height=25)
        
        
        
        # Password
        Username_label = Label(frame, text="Password: ",
                           font=("time new roman", 15, "bold"),fg="white", bg="black")
        Username_label.place(x=55,y=240)
        # Password fill
        self.User_entry = ttk.Entry(
            frame, width=20, font=("time new roman", 15, "bold"))
        self.User_entry.place(x=35,y=270,width=280)
        
        
        
        


        
        






if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root)
    root.mainloop()

