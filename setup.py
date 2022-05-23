import cx_Freeze
import sys
import os 
base = None        

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\hp\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\hp\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognition_Software.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'My_images','data','database','attendanceReport']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By IshanChauhan",
    executables = executables
    )