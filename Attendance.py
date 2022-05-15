from ast import Delete
from cProfile import label
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Student:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")
        
        
        img1 = Image.open(
            r"My_images\studying.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
 # antilias converts high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(img1)
        firstlabel = Label(self.root, image=self.photoimg1)
        firstlabel.place(x=0, y=0, width=800, height=200)
     # 2nd image
        img2 = Image.open(
            r"My_images\face-recognition.png")
        img2 = img2.resize((800, 200), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        firstlabel = Label(self.root, image=self.photoimg2)
        firstlabel.place(x=800, y=0, width=800, height=200)
        
        title_lbl = Label(self.root, text="ATTENDANCE  MANAGEMENT  PORTAL", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=200, width=1540, height=45)
        
        # creating main frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=8, y=250, width=1530, height=625)
        
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=(
            "time new roman", 12, "bold"))  # ridge is border style
        Left_frame.place(x=10, y=10, width=750, height=510)
        img_left = Image.open(
            r"C:\Users\hp\OneDrive\Desktop\facerecoginition\My_images\students.jpeg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        firstlabel = Label(Left_frame, image=self.photoimg_left)
        firstlabel.place(x=7, y=0, width=720, height=130)
        # left inside frame
        Left_inside_frame = Frame(Left_frame, bd=2, bg="white",relief=RIDGE)
        Left_inside_frame.place(x=8, y=140, width=730, height=340)
        
        # label entry 
        Studentid_label = Label(Left_inside_frame, text="AttendanceID:", bg="white", font=(
            "time new roman", 12, "bold"))
        Studentid_label.grid(row=0, column=0, pady=8, sticky=W)

        Studentid_entry = ttk.Entry(
            Left_inside_frame, width=20, font=("time new roman", 12, "bold"))
        Studentid_entry.grid(row=0, column=1, pady=8, sticky=W)
        #  Name 
        Student_name_label = Label(Left_inside_frame, text="Student Name:", bg="white", font=(
            "time new roman", 12, "bold"))
        Student_name_label.grid(row=0, column=2,pady=8, sticky=W)

        Student_name_entry = ttk.Entry(
            Left_inside_frame, width=20, font=("time new roman", 12, "bold"))
        Student_name_entry.grid(row=0, column=3, pady=8, sticky=W)
         #  time
        time_label = Label(Left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        time_label.grid(row=1,column=0)
        
        atten_time=ttk.Entry(Left_inside_frame,width=20,font="comicsansns 11 bold")
        atten_time.grid(row=1,column=1,pady=8)
        
        
        #  date
        date_label = Label(Left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        date_label.grid(row=1,column=2)
        
        atten_date=ttk.Entry(Left_inside_frame,width=20,font="comicsansns 11 bold")
        atten_date.grid(row=1,column=3,pady=8)
        
        #  Attendance
        
        attendance_label = Label(Left_inside_frame, text="Attendance:",
                             bg="white", font=("time new roman", 12, "bold"))
        attendance_label.grid(row=2, column=0,)
        
        self.attendance_combo = ttk.Combobox(Left_inside_frame, font=(
            "comicsansns 11 bold"), width=20, state="readonly")
        self.attendance_combo["values"] = ("Status", "Present", "Absent")
        self.attendance_combo.current(0)  # positioning tuples
        self.attendance_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        
         # button frame #
        btn_frame = Frame(Left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=250, width=720, height=36)
        # Save button
        save_btn = Button(btn_frame, text="Import csv",width=17, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        # update buttpon
        Update_btn = Button(btn_frame, text="Export csv", width=17, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)
        # delete button
        Delete_btn = Button(btn_frame, text="Update", width=17,font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Delete_btn.grid(row=0, column=2)
        # reset button
        Reset_btn = Button(btn_frame, text="Reset", width=18, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)


        
        
        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=(
            "time new roman", 12, "bold"))  # ridge is border style
        Right_frame.place(x=780, y=10, width=700, height=510)
        
        Table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        Table_frame.place(x=5, y=5, width=680, height=460)
        
        #  scroll bar
        scrollx = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.attendanceReporttb=ttk.Treeview(Table_frame,columns=("id","Name","Time","date","Attendance"),xscrollcommand=scrollx,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.attendanceReporttb.xview)
        scrolly.config(command=self.attendanceReporttb.yview)
        
        self.attendanceReporttb.heading("id",text="Atendance_ID")
        self.attendanceReporttb.heading("Name",text="Student_Name")
        self.attendanceReporttb.heading("Time",text="Time")
        self.attendanceReporttb.heading("date",text="Date")
        self.attendanceReporttb.heading("Attendance",text="Atendance")
        self.attendanceReporttb["show"]="headings"  #removing spaces
        self.attendanceReporttb.column("id",width=120)
        self.attendanceReporttb.column("Name",width=120)
        self.attendanceReporttb.column("Time",width=120)
        self.attendanceReporttb.column("date",width=120)
        self.attendanceReporttb.column("Attendance",width=120)
        
        
        self.attendanceReporttb.pack(fill=BOTH,expand=1)
        


        

        





 
        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
