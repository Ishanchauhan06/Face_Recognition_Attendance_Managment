from argparse import FileType
from ast import Delete
from cProfile import label
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class AttendanceStu:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        # Text variables
        self.var_attendance=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_year=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendstatus=StringVar()
        
        
        
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
        Studentid_label = Label(Left_inside_frame, text="AttendanceID:",bg="white", font=(
            "time new roman", 12, "bold"))
        Studentid_label.grid(row=0, column=0, pady=8, sticky=W)

        Studentid_entry = ttk.Entry(
            Left_inside_frame, width=20, font=("time new roman", 12, "bold"),textvariable=self.var_attendance)
        Studentid_entry.grid(row=0, column=1, pady=8, sticky=W)
        #  Name 
        Student_name_label = Label(Left_inside_frame, text="Student Name:", bg="white", font=(
            "time new roman", 12, "bold"))
        Student_name_label.grid(row=0, column=2,pady=8, sticky=W)
        Student_name_entry = ttk.Entry(
            Left_inside_frame, width=20, font=("time new roman", 12, "bold"), textvariable=self.var_name)
        Student_name_entry.grid(row=0, column=3, pady=8, sticky=W, )
        
        #  Dept
        time_label = Label(Left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        time_label.grid(row=1,column=0)
        
        atten_time=ttk.Entry(Left_inside_frame,width=20,font="comicsansns 11 bold",textvariable=self.var_dept)
        atten_time.grid(row=1,column=1,pady=8)
        
        # Year
        time_label = Label(Left_inside_frame,text="Year:",bg="white",font="comicsansns 11 bold")
        time_label.grid(row=1,column=2)
        
        atten_time=ttk.Entry(Left_inside_frame,width=20,font="comicsansns 11 bold",textvariable=self.var_year)
        atten_time.grid(row=1,column=3,pady=8)
        
        
         #  time
        time_label = Label(Left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        time_label.grid(row=2,column=0)
        
        atten_time=ttk.Entry(Left_inside_frame,width=20,font="comicsansns 11 bold",textvariable=self.var_time)
        atten_time.grid(row=2,column=1,pady=8)
        
        
        #  date
        date_label = Label(Left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        date_label.grid(row=2,column=2)
        
        atten_date=ttk.Entry(Left_inside_frame,width=20,font="comicsansns 11 bold",textvariable=self.var_date)
        atten_date.grid(row=2,column=3,pady=8)
        
        #  Attendance
        
        attendance_label = Label(Left_inside_frame, text="Attendance:",
                             bg="white", font=("time new roman", 12, "bold"))
        attendance_label.grid(row=3, column=0,)
        
        self.attendance_combo = ttk.Combobox(Left_inside_frame, font=(
            "comicsansns 11 bold"), textvariable=self.var_attendstatus,width=20, state="readonly")
        self.attendance_combo["values"] = ("Status", "Present", "Absent")
        self.attendance_combo.current(0)  # positioning tuples
        self.attendance_combo.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        
         # button frame #
        btn_frame = Frame(Left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=250, width=720, height=36)
        # Import csv button
        save_btn = Button(btn_frame, text="Import csv",command=self.importcsv,width=17, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        # Export buttpon
        Update_btn = Button(btn_frame, text="Export csv", command=self.exportcsv,width=17, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)
        # delete button
        Delete_btn = Button(btn_frame, text="Update", width=17,font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Delete_btn.grid(row=0, column=2)
        # reset button
        Reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,width=18, font=(
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
        
        self.attendanceReporttb=ttk.Treeview(Table_frame,columns=("id","Name","Dept","Year","Time","date","Attendance"),xscrollcommand=scrollx,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.attendanceReporttb.xview)
        scrolly.config(command=self.attendanceReporttb.yview)
        
        self.attendanceReporttb.heading("id",text="Atendance_ID")
        self.attendanceReporttb.heading("Name",text="Student_Name")
        self.attendanceReporttb.heading("Dept",text="Dpartment")
        self.attendanceReporttb.heading("Year",text="Year")
        self.attendanceReporttb.heading("Time",text="Time")
        self.attendanceReporttb.heading("date",text="Date")
        self.attendanceReporttb.heading("Attendance",text="Atendance")
        self.attendanceReporttb["show"]="headings"  #removing spaces
        self.attendanceReporttb.column("id",width=120)
        self.attendanceReporttb.column("Name",width=120)
        self.attendanceReporttb.column("Dept",width=120)
        self.attendanceReporttb.column("Year",width=120)
        self.attendanceReporttb.column("date",width=120)
        self.attendanceReporttb.column("Time",width=120)
        self.attendanceReporttb.column("Attendance",width=120)
        
        self.attendanceReporttb.pack(fill=BOTH,expand=1)
        
        self.attendanceReporttb.bind("<ButtonRelease>",self.get_cursor)
        
        
    # fetching data from database
    def fetchdata(self,rows):
        self.attendanceReporttb.delete(*self.attendanceReporttb.get_children())
        for i in rows:
            self.attendanceReporttb.insert("",END,values=i)
    
    def importcsv(self):
        global mydata
        mydata.clear()
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(filename) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
            
    # Export data
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data found to Export!",parent=self.root)
                return False
            filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(filename,mode="w",newline="") as myfile:
                export_file=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_file.writerow(i)
                messagebox.showinfo("exported Data", "Dta Exported to "+os.path.basename(filename)+" Succesfully!")
        except Exception as es:
                messagebox.showerror(
                        "Error", f"Due to :{str(es)}", parent=self.root)
                
    
    def get_cursor(self,event=""):
        cursor_row=self.attendanceReporttb.focus()
        content=self.attendanceReporttb.item(cursor_row)
        rows=content['values']
        self.var_attendance.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_year.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendstatus.set(rows[6])
        
    def reset_data(self):
        self.var_attendance.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_year.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendstatus.set("Status")
       
        
         
           
        
        
    
            
            
        
        


        

        





 
        

if __name__ == "__main__":
    root = Tk()
    obj = AttendanceStu(root)
    root.mainloop()
