from cProfile import label
from email import message
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from setuptools import Command 
from main import Face_Recoginition_System

  
  
def main():
    win=Tk()
    app=LoginWindow(win)
    win.mainloop()
    
class LoginWindow:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")
        self.root.wm_iconbitmap("face.ico")
        
        img = Image.open(
            r"My_images\loginbg.jpg")
        img = img.resize((1530, 790), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg = ImageTk.PhotoImage(img)

        self.var_txtuser=StringVar()
        self.var_txtpass=StringVar()
        
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
        # fname 
        Username_label = Label(frame, text="Username: ",
                           font=("time new roman", 15, "bold"),fg="white", bg="black")
        Username_label.place(x=55,y=170)
        # Entry fill
        self.User_entry = ttk.Entry(
            frame, width=20,font=("time new roman", 15, "bold"),textvariable=self.var_txtuser)
        self.User_entry.place(x=35,y=200,width=280)
        # icon
        img3 = Image.open(
            r"My_images\LoginIconAppl.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg3 = ImageTk.PhotoImage(img3)
        firstlabel = Label(image=self.photoimg3,bg="black",borderwidth=0)
        firstlabel.place(x=640, y=340, width=25, height=25)
        
        img4 = Image.open(
            r"My_images\lock-512.png")
        img4 = img4.resize((25, 25), Image.ANTIALIAS)
        # antilias converts high level image to low level
        self.photoimg4 = ImageTk.PhotoImage(img4)
        firstlabel = Label(image=self.photoimg4,bg="black",borderwidth=0)
        firstlabel.place(x=640, y=413, width=25, height=25)
        
        
        # Password
        Username_label = Label(frame, text="Password: ",
                           font=("time new roman", 15, "bold"),fg="white", bg="black")
        Username_label.place(x=55,y=240)
        # Password fill
        self.Pass_entry = ttk.Entry(
            frame, width=20, font=("time new roman", 15, "bold"),textvariable=self.var_txtpass)
        self.Pass_entry.place(x=35,y=270,width=280)
        #  Login button
        b1 = Button(frame,text="Login",command=self.login,font=("time new roman", 15, "bold"),bd=3,fg="white",bg="red",activeforeground="white", activebackground="red")
        b1.place(x=110, y=330, width=120, height=35)
        
        # Register button 
        b2 = Button(frame,text="New user Register",font=("time new roman", 10, "bold"),command=self.registerwindow,borderwidth=0,fg="white",bg="black",activeforeground="white", activebackground="black")
        b2.place(x=10, y=370, width=160)
        # Forget password
        b3 = Button(frame,text="Forget Password",command=self.forget_pass,font=("time new roman", 10, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white", activebackground="black")
        b3.place(x=10, y=400, width=160)
        
    def registerwindow(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
     
     
        
    def login(self):
        if self.User_entry.get()=="" or self.Pass_entry.get()=="":
            messagebox.showerror("Error", "All fields are required")
        elif self.User_entry.get()=="Ishan" and self.Pass_entry.get()=="1234":
                messagebox.showinfo("success","Welcome to the Application")
        else:
            conn = mysql.connector.connect(
            host="localhost", username="root", password="Ishan@2506", database="registerinfo")
            my_cursor = conn.cursor()
            my_cursor.execute("select *from userinformation where EmailID=%s and Password=%s",(
                                                                       self.var_txtuser.get(),
                                                                       self.var_txtpass.get()
                                                                        ))
                
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("yes","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recoginition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
   #  *******************Reset Password************************
        self.var_new_txt_pass= StringVar()
  
    def  reset_pass(self):
        if self.security_combo.get()=="select":
            messagebox.showerror("Error","select the security question")
        elif self.ans_entry.get()=="":
            messagebox.showerror("Error","Please Enter the Answer")
        elif self.new_pass_entry.get()=="":
            messagebox.showerror("Error","Please Enter New Password")
        else:
            conn = mysql.connector.connect(
            host="localhost", username="root", password="Ishan@2506", database="registerinfo")
            my_cursor = conn.cursor()
            qury=("select * from userinformation where EmailID=%s and Security=%s and SecurityAns=%s")
            value=(self.var_txtuser.get(),self.security_combo.get(),self.ans_entry.get())
            my_cursor.execute(qury,value)
            row= my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please enter correct answer")
            else:
                query=("update userinformation set Password=%s where EmailID=%s")
                value=(self.new_pass_entry.get(),self.var_txtuser.get())
                my_cursor.execute(query, value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("info","your Password has been reset, now Login with new one!")                
            
            
            
    # *********************Forget Password window*******************************
    def forget_pass(self):
        if self.var_txtuser.get()=="":
            messagebox.showerror("Please enter the EmailID to reset Password")
        else:
            conn = mysql.connector.connect(
            host="localhost", username="root", password="Ishan@2506", database="registerinfo")
            my_cursor = conn.cursor()
            query=("select * from userinformation where EmailID=%s")
            value=(self.var_txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Invalid Username!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                l= Label(self.root2,text="Forget Password",font=("time new roman", 20, "bold"),fg="blue",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                # security question
                security= Label(self.root2,text="Select Security Question:",font=("times new roman",15, "bold"),bg="white")
                security.place(x=50,y=80)
                
                self.security_combo = ttk.Combobox(self.root2, font=(
                    "time new roman", 15, "bold"),state="read only")
                self.security_combo["values"] = ("Select", "Your Birth PLace", "Your Pet Name", "First school name","Favourite Location")
                self.security_combo.current(0)  # positioning tuples
                self.security_combo.place(x=50,y=110,width=250)

                #  Security ans
                Ans= Label(self.root2,text="Security Answer:",font=("times new roman",15, "bold"),bg="white")
                Ans.place(x=50,y=150)
                
                self.ans_entry = ttk.Entry(
                    self.root2, width=20,font=("time new roman", 15, "bold"))
                self.ans_entry.place(x=50,y=180,width=250)
                # NewPassword 
                new_pass= Label(self.root2,text="Enter New Password:",font=("times new roman",15, "bold"),bg="white")
                new_pass.place(x=50,y=220)
                
                self.new_pass_entry = ttk.Entry(
                    self.root2, width=20,font=("time new roman", 15, "bold"))
                self.new_pass_entry.place(x=50,y=250,width=250)
                
                # button
                
                btn = Button(self.root2,text="Reset", font=("time new roman", 15, "bold"), command=self.reset_pass,fg="white", bg="green")
                btn.place(x=130,y=300)
                
                        
                
                       
                
           
                
        
 
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")
        
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
    main()
