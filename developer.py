from ast import Delete
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        # inserting image for top
        img_top = Image.open(
            r"My_images\dev.jpg")
        img_top = img_top.resize((1530, 735), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        firstlabel = Label(self.root, image=self.photoimg_left)
        firstlabel.place(x=0, y=48, width=1530, height=735)

     # creating a frame
        main_frame = Frame(firstlabel, bd=2, bg="white")
        main_frame.place(x=550, y=0, width=500, height=600)

        img_top_pht = Image.open(
            r"My_images\developers.jpg")
        img_top_pht = img_top_pht.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_left_pht = ImageTk.PhotoImage(img_top_pht)

        firstlabel = Label(main_frame, image=self.photoimg_left_pht)
        firstlabel.place(x=300, y=0, width=200, height=200)

        # Developers
        Dev_label = Label(main_frame, text="Hello Everyone!",
                          bg="white", font=("time new roman", 20, "bold"), fg="blue")
        Dev_label.place(x=0, y=15)

        Dev_label = Label(main_frame, text="This is my \n Engage Program \n Project",
                          bg="white", font=("time new roman", 20, "bold"), fg="blue")
        Dev_label.place(x=0, y=60)

        Dev_label = Label(main_frame, 
    text="This Project will track students attendance and \n  will also save, update and delete student \n details, In the take photo section student can \n take its photo to train data after training of \n data the machine will autonmatically detect \n a person that will come in front of \n camera and take attendace automatically ",
                          bg="white", font=("time new roman", 15, "bold"), fg="black")
        Dev_label.place(x=0, y=230)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
