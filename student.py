from ast import Delete
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 


class Student:
    # calling construction
    def __init__(self, root):
        self.root = root
        # setting geometry i.e height and width of window + X and Y axis starting point
        # size of widow as per device available
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")

        #  Variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_name = StringVar()

  # For inserting the images
        img1 = Image.open(
            r"C:\Users\hp\OneDrive\Desktop\facerecoginition\My_images\studying.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
 # antilias converts high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(img1)

        firstlabel = Label(self.root, image=self.photoimg1)
        firstlabel.place(x=0, y=0, width=500, height=130)
  # 2nd image
        img2 = Image.open(
            r"C:\Users\hp\OneDrive\Desktop\facerecoginition\My_images\face-recognition.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        firstlabel = Label(self.root, image=self.photoimg2)
        firstlabel.place(x=500, y=0, width=500, height=130)
  # 3 image
        img = Image.open(
            r"C:\Users\hp\OneDrive\Desktop\facerecoginition\My_images\student.jpg")
        img = img.resize((550, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        firstlabel = Label(self.root, image=self.photoimg)
        firstlabel.place(x=1000, y=0, width=550, height=130)


# bg image
        img3 = Image.open(
            r"C:\Users\hp\OneDrive\Desktop\facerecoginition\My_images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bgimage = Label(self.root, image=self.photoimg3)
        bgimage.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bgimage, text="SUDENT  MANAGEMENT  PORTAL", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

     # creating a frame
        main_frame = Frame(bgimage, bd=2, bg="white")
        main_frame.place(x=8, y=55, width=1500, height=625)

    #    left side label frame for details
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "time new roman", 12, "bold"))  # ridge is border style
        Left_frame.place(x=10, y=10, width=750, height=590)

        img_left = Image.open(
            r"C:\Users\hp\OneDrive\Desktop\facerecoginition\My_images\students.jpeg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

     # inserting image for left frame
        firstlabel = Label(Left_frame, image=self.photoimg_left)
        firstlabel.place(x=7, y=0, width=720, height=130)

        #  current course information
        Current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information:-", font=("time new roman", 12, "bold"))  # ridge is border style
        Current_course_frame.place(x=5, y=135, width=720, height=150)
       # department label
        dep_label = Label(Current_course_frame, text="Department",
                          bg="white", font=("time new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_dept, font=(
            "time new roman", 12, "bold"), width=20, state="read only")
        dep_combo["values"] = ("Select Department", "Computer Science",
                               "Mechanical", "Civil", "Electrical", "ECE")
        dep_combo.current(0)  # positioning tuples
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
      
        # Year
        Year_label = Label(Current_course_frame, text="Year",
                           bg="white", font=("time new roman", 12, "bold"))
        Year_label.grid(row=0, column=2, padx=10)

        Year_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_year, font=(
            "time new roman", 12, "bold"), width=20, state="read only")
        Year_combo["values"] = ("Select Year", "2018-22",
                                "2019-23", "2020-24", "2021-25", "2022-26")
        Year_combo.current(0)  # positioning tuples
        Year_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
    
    # Course
        Course_label = Label(Current_course_frame, text="Course",
                             bg="white", font=("time new roman", 12, "bold"))
        Course_label.grid(row=1, column=0, padx=10)

        Course_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_course, font=(
            "time new roman", 12, "bold"), width=20, state="read only")
        Course_combo["values"] = ("Select course", "FE", "SE", "TE", "BE")
        Course_combo.current(0)  # positioning tuples
        Course_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

    # Semester
        Semester_label = Label(Current_course_frame, text="Semester", bg="white", font=(
            "time new roman", 12, "bold"))
        Semester_label.grid(row=1, column=2, padx=10)

        Semester_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_semester, font=(
            "time new roman", 12, "bold"), width=20, state="read only")
        Semester_combo["values"] = (
            "Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        Semester_combo.current(0)  # positioning tuples
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

    #  Class student information
        Class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Info:-", font=("time new roman", 12, "bold"))  # ridge is border style
        Class_student_frame.place(x=5, y=300, width=720, height=265)
    # student_id
        Studentid_label = Label(Class_student_frame, text="StudentID:", bg="white", font=(
            "time new roman", 12, "bold"))
        Studentid_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        Studentid_entry = ttk.Entry(
            Class_student_frame, textvariable=self.var_std_id, width=20, font=("time new roman", 12, "bold"))
        Studentid_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student_Name
        Student_name_label = Label(Class_student_frame, text="Student Name:", bg="white", font=(
            "time new roman", 12, "bold"))
        Student_name_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        Student_name_entry = ttk.Entry(
            Class_student_frame, textvariable=self.var_name, width=20, font=("time new roman", 12, "bold"))
        Student_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Gender
        Gender_label = Label(Class_student_frame, text="Gender:",
                             bg="white", font=("time new roman", 12, "bold"))
        Gender_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        # Gender_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_gender, font=(
        #     "time new roman", 12, "bold"))
        # Gender_entry.grid(row=1, column=1, padx=10, sticky=W)
        Gender_combo = ttk.Combobox(Class_student_frame, textvariable=self.var_gender, font=(
            "time new roman", 12, "bold"), width=20, state="read only")
        Gender_combo["values"] = ("Select", "Male", "Female", "Other")
        Gender_combo.current(0)  # positioning tuples
        Gender_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)


        # Mail id
        Gender_label = Label(Class_student_frame, text="MailID:",
                             bg="white", font=("time new roman", 12, "bold"))
        Gender_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Gender_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_email, font=(
            "time new roman", 12, "bold"))
        Gender_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Contact Number
        Contact_number_label = Label(
            Class_student_frame, text="Contact Number:", bg="white", font=("time new roman", 12, "bold"))
        Contact_number_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        Contact_number_entry = ttk.Entry(
            Class_student_frame, width=20, textvariable=self.var_phone, font=("time new roman", 12, "bold"))
        Contact_number_entry.grid(row=2, column=1, padx=10, sticky=W)

        # Address
        Address_label = Label(Class_student_frame, text="Address:", bg="white", font=(
            "time new roman", 12, "bold"))
        Address_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        Address_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_address, font=(
            "time new roman", 12, "bold"))
        Address_entry.grid(row=2, column=3, padx=10, sticky=W)

        # radio Buttons
        self.var_radio = StringVar()
        radio_button1 = ttk.Radiobutton(
            Class_student_frame, variable=self.var_radio, text="Take Photo Sample", value="Yes")
        radio_button1.grid(row=3, column=0)

        self.var_radio = StringVar()
        radio_button = ttk.Radiobutton(
            Class_student_frame, variable=self.var_radio, text="No Photo Sample", value="No")
        radio_button.grid(row=3, column=1)

        # button frame #
        btn_frame = Frame(Class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=170, width=685, height=36)
        # Save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        # update buttpon
        Update_btn = Button(btn_frame, text="Update", command=self.update_data,width=17, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)
        # delete button
        Delete_btn = Button(btn_frame, text="Delete", width=17,command=self.delete_data, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Delete_btn.grid(row=0, column=2)
        # reset button
        Reset_btn = Button(btn_frame, text="Reset", width=16,command=self.reset_data, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)

        # Take a photo sample second button frame for take and update photo

        btn_frame1 = Frame(Class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=2, y=205, width=685, height=36)

        # Take photo button
        Takephoto_btn = Button(btn_frame1, text="Take Photo", width=35, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Takephoto_btn.grid(row=0, column=0)
        # Update button
        Update_btn = Button(btn_frame1, text="Update Photo", width=35, font=(
            "time new roman", 12, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)

    #    Right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "time new roman", 12, "bold"))  # ridge is border style
        Right_frame.place(x=780, y=10, width=690, height=590)

        img_Right = Image.open(
            r"C:\Users\hp\OneDrive\Desktop\facerecoginition\My_images\smart-attendance.jpg")
        img_Right = img_Right.resize((680, 130), Image.ANTIALIAS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)
        firstlabel = Label(Right_frame, image=self.photoimg_Right)
        firstlabel.place(x=7, y=0, width=680, height=130)

        # *************Search System****************
        Search_student_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Search System:-", font=("time new roman", 12, "bold"))  # ridge is border style
        Search_student_frame.place(x=5, y=135, width=680, height=70)
        # search label
        Search_label = Label(Search_student_frame, text="Search By:",
                             bg="green", fg="white", font=("time new roman", 12, "bold"))
        Search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        Search_combo = ttk.Combobox(Search_student_frame, font=(
            "time new roman", 12, "bold"), width=15, state="readonly")
        Search_combo["values"] = (
            "Select", "Roll number", "Phone number", "Name")
        Search_combo.current(0)  # positioning tuples
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(Search_student_frame,
                                 width=16, font=("time new roman", 10, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, sticky=W)

        # Search button
        Search_btn = Button(Search_student_frame, text="Search", width=12, font=(
            "time new roman", 10, "bold"), bg="blue", fg="white")
        Search_btn.grid(row=0, column=3, padx=2, pady=5, sticky=W)
        # Show All button
        Reset_btn = Button(Search_student_frame, text="Show All", width=12, font=(
            "time new roman", 10, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=4, padx=2, pady=5, sticky=W)

        # *********Table frame*************
        Table_frame = Frame(Right_frame, bd=2, bg="white",
                            relief=RIDGE,)  # ridge is border style
        Table_frame.place(x=5, y=210, width=680, height=350)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame, column=("Department", "Year", "Course", "Semester", "StudentID","Name",
                                          "Gender", "MailID", "Phone Number","Address", "Photosample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("StudentID", text="StudentID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("MailID", text="Email_ID")
        self.student_table.heading("Phone Number", text="Phone Number")
        self.student_table.heading("Address", text="Phone Number")
        self.student_table.heading("Photosample", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("StudentID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("MailID", width=100)
        self.student_table.column("Phone Number", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Photosample", width=100)
      

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # **************Functions Declaration*************

    def add_data(self):
        if self.var_dept.get() == "Slect Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror(
                    "Error", "All fields are Required", parent=self.root)
        else:
            try:
              conn = mysql.connector.connect(
              host="localhost", username="root", password="Ishan@2506", database="face_recognitiondb")
              my_cursor = conn.cursor()
              my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_dept.get(),
                        self.var_year.get(),
                        self.var_course.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio.get()
                    ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo(
                        "success", "Student details has beem added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                        "Error", f"Due to :{str(es)}", parent=self.root)

      # *************Fetching a data from database *****************
    def fetch_data(self):
        conn = mysql.connector.connect(
              host="localhost", username="root", password="Ishan@2506", database="face_recognitiondb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()
        
# ****************get cursor***************
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dept.set(data[0]),
        self.var_year.set(data[1]),
        self.var_course.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_address.set(data[9]),
        self.var_radio.set(data[10])
        
        #*************Update function*********
    def update_data(self):
        if self.var_dept.get() == "Slect Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror( "Error", "All fields are Required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to update student details", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Ishan@2506", database="face_recognitiondb")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dept=%s, Year=%s, Course=%s, Semester=%s, Name=%s, Gender=%s, MailId=%s, Phone Number=%s, Address=%s, Photosample=%s where StudentId=%s",(
                        self.var_dept.get(),
                        self.var_year.get(),
                        self.var_course.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                    
                    
         #  Delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "StudentID must required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page", "Do you want to delete the details", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Ishan@2506", database="face_recognitiondb")
                    my_cursor = conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        messagebox.showinfo("Delete","student details deleted successfully", parent=self.root)
                        
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                    
                    
    # Reset**********
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_year.set("Select Year")
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio.set("")
        
        
         
        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
