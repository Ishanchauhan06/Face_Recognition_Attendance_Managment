from ast import Delete
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox

class HelpDesk:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        title_lbl = Label(self.root, text="Help Desk", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
          # inserting image for top 
        img_top = Image.open(
            r"My_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1530, 735), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        firstlabel = Label(self.root, image=self.photoimg_left)
        firstlabel.place(x=0, y=48, width=1530, height=735)
        
        Dev_label = Label(firstlabel, text="Email: chauhanishan82@gmail.com \n Contact Number: 9119041246    ",
                           bg="white", font=("time new roman", 20, "bold"),fg="blue")
        Dev_label.place(x=550,y=205)
       
        

     

if __name__ == "__main__":
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()

     