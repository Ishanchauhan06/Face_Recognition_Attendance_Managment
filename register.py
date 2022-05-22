from email import message
from tkinter import*
from tkinter import ttk
from turtle import onclick
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from setuptools import Command 
from loginpage import LoginWindow

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")
        self.root.wm_iconbitmap("face.ico")
        
        img = Image.open(
            r"My_images\loginbg.jpg")
        img = img.resize((1530, 790), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg = ImageTk.PhotoImage(img)
        
        #  text variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security=StringVar()
        self.var_securityans=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #  bgimage
        bgimage = Label(self.root, image=self.photoimg)
        bgimage.place(x=0, y=13, relwidth=1, relheight=1)
        
        # left image
        img2 = Image.open(
            r"My_images\Facey.jpg")
        img2 = img2.resize((470, 550), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bgimage = Label(self.root, image=self.photoimg2)
        bgimage.place(x=80, y=150, width=470, height=550)

        
        title_lbl = Label(self.root, text=" REGISTER ", font=(
            "times new roman", 35, "bold"), bg="Darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1540, height=45)
        # ******************main farme*******************
        frame = Frame(self.root, bg="white")
        frame.place(x=540,y=150, width=800, height=550)
        
        register_lbl=Label(frame,text=" REGISTER HERE ",font=("times new roman", 25, "bold"),bg="white",fg="blue")
        register_lbl.place(x=20,y=20)
       #    Labels and entry filles
    #    first name Label
        fname=Label(frame, text="First Name: ",font=("times new roman",15, "bold"),bg="white")
        fname.place(x=50,y=100)
        
        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname,width=20, font=("time new roman", 15, "bold"))
        self.fname_entry.place(x=50,y=140,width=250)
        # last anme
        fname=Label(frame, text="Last Name: ",font=("times new roman",15, "bold"),bg="white")
        fname.place(x=380,y=100)
        
        self.fname_entry = ttk.Entry(
            frame, width=20,  textvariable=self.var_lname,font=("time new roman", 15, "bold"))
        self.fname_entry.place(x=380,y=140,width=250)
        
        # contact number
        
        contact= Label(frame,text="Contact Number:",font=("times new roman",15, "bold"),bg="white")
        contact.place(x=50,y=185)
        
        self.cont_entry = ttk.Entry(
            frame,  textvariable=self.var_contact,width=20, font=("time new roman", 15, "bold"))
        self.cont_entry.place(x=50,y=220,width=250)
        #  emailid
        Email= Label(frame,text="EmailID:",font=("times new roman",15, "bold"),bg="white")
        Email.place(x=380,y=185)
        
        self.Email_entry = ttk.Entry(
            frame, width=20,  textvariable=self.var_email,font=("time new roman", 15, "bold"))
        self.Email_entry.place(x=380,y=220,width=250)
        
        # security question
        security= Label(frame,text="Select Security Question:",font=("times new roman",15, "bold"),bg="white")
        security.place(x=50,y=270)
        
        self.security_combo = ttk.Combobox(frame, font=(
            "time new roman", 15, "bold"),  textvariable=self.var_security, state="read only")
        self.security_combo["values"] = ("Select", "Your Birth PLace", "Your Pet Name", "First school name","Favourite Location")
        self.security_combo.current(0)  # positioning tuples
        self.security_combo.place(x=50,y=300,width=250)

        #  Security ans
        Ans= Label(frame,text="Security Answer:",font=("times new roman",15, "bold"),bg="white")
        Ans.place(x=370,y=270)
        
        self.ans_entry = ttk.Entry(
            frame, width=20,  textvariable=self.var_securityans,font=("time new roman", 15, "bold"))
        self.ans_entry.place(x=380,y=300,width=250)
        
        # password
        pswd = Label(frame,text="Password:",font=("times new roman",15, "bold"),bg="white")
        pswd.place(x=50,y=345)
        
        self.pswd_entry = ttk.Entry(
            frame, width=20, font=("time new roman", 15, "bold"),textvariable=self.var_pass)
        self.pswd_entry.place(x=50,y=380,width=250)
        
        confirm_pswd = Label(frame,text="Confirm Password:",font=("times new roman",15, "bold"),bg="white")
        confirm_pswd.place(x=385,y=340)
        
        self.confirm_pswd_entry = ttk.Entry(
            frame, width=20, font=("time new roman", 15, "bold"),textvariable=self.var_confpass)
        self.confirm_pswd_entry.place(x=380,y=380,width=250)
        
        #  Check button
        self.var_checkbtn=IntVar()
        checkbtn=Checkbutton(frame,text="I agree the Terms & condition",variable=self.var_checkbtn,font=("time new roman", 12, "bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=420)
        
        # buttons  Register and login
        img4 = Image.open(
            r"My_images\register-now-button1.jpg")
        img4 = img4.resize((100, 50), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(frame,image=self.photoimg4, command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=60, y=460, width=100)
        
        img5 = Image.open(
            r"My_images\loginpng.png")
        img5 = img5.resize((100, 40), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(frame,  image=self.photoimg5, borderwidth=0,cursor="hand2")
        b1.place(x=390, y=460, width=100)
       
       
        #  function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security.get()=="Select" :
            messagebox.showerror("error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
           messagebox.showerror("error","Password and confirm password must be same")
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error", "Please Agree terms and Condition")
        else:
            conn = mysql.connector.connect(
            host="localhost", username="root", password="Ishan@2506", database="registerinfo")
            my_cursor = conn.cursor()
            query=("select * from userinformation where EmailID=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another Enail")
            else:
                my_cursor.execute("insert into userinformation values(%s,%s,%s,%s,%s,%s,%s)",(
                                                              self.var_fname.get(),
                                                              self.var_lname.get(),
                                                              self.var_contact.get(),
                                                              self.var_email.get(),
                                                              self.var_security.get(),
                                                              self.var_securityans.get(),
                                                              self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")
                
             
            
        
        
        
        





if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()

