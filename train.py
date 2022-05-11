from ast import Delete
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Train:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="Train Data Set", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        
        
         
        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

