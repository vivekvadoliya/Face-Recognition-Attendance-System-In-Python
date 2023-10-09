from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from datetime import datetime
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

#first image ................
        img = Image.open("E:/project/img/7.jpg")
        img = img.resize((455, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=455, height=130)


#second image ................
        img1 = Image.open("E:/project/img/4.jpg")
        img1 = img1.resize((456, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=455, y=0, width=456, height=130)

#third image ................
        img2 = Image.open("E:/project/img/7.jpg")
        img2 = img2.resize((455, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=911, y=0, width=455, height=130)

#bg image ................
        img3 = Image.open("E:/project/img/bg.jpg")
        img3 = img3.resize((1366,768), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1366, height=768)


        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 30 , "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1366, height=45)  

# =================time==========================
       # def time():
        #         string=datetime.strftime("%H:%M:%S %p")
        #         self.lbl_clock.config(text=string)
        #         self.lbl_clock.after(1000,self.time)


        # lbl= Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        # lbl.place(x=0,y=0,width=110,height=50)
        # time()


 # Student Button.....................       
        img4 = Image.open("E:/project/img/student.jpg")
        img4 = img4.resize((210,190), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=120, y=100, width=210, height=190)


        b1_1 = Button(bg_img,text='STUDENT DETAILS',command=self.student_details,cursor="hand2",font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b1_1.place(x=120, y=290, width=210, height=40)

 # face scanner Button.....................       
        img5 = Image.open("E:/project/img/face.jpg")
        img5 = img5.resize((210,190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.Face_data) 
        b2.place(x=420, y=100, width=210, height=190)


        b2_1 = Button(bg_img,text='FACE SCANNER', cursor="hand2",command=self.Face_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b2_1.place(x=420, y=290, width=210, height=40)

# attendance Button.....................       
        img6 = Image.open("E:/project/img/attendance.jpg")
        img6 = img6.resize((210,190), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=720, y=100, width=210, height=190)


        b3_1 = Button(bg_img,text='ATTENDANCE', cursor="hand2",command=self.attendance_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b3_1.place(x=720, y=290, width=210, height=40)


# help Button.....................       
        img7 = Image.open("E:/project/img/help.jpg")
        img7 = img7.resize((210,190), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b4.place(x=1020, y=100, width=210, height=190)


        b4_1 = Button(bg_img,text='HELP', cursor="hand2",command=self.help_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b4_1.place(x=1020, y=290, width=210, height=40)


# Train Button.....................       
        img8 = Image.open("E:/project/img/training.jpg")
        img8 = img8.resize((210,190), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=120, y=370, width=210, height=190)


        b5_1 = Button(bg_img,text='TRAIN', cursor="hand2",command=self.train_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b5_1.place(x=120, y=550, width=210, height=40)


# Photos Button.....................       
        img9 = Image.open("E:/project/img/photo.jpg")
        img9 = img9.resize((210,190), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=420, y=370, width=210, height=190)


        b6_1 = Button(bg_img,text='PHOTOS', cursor="hand2",command=self.open_img,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b6_1.place(x=420, y=550, width=210, height=40)



# Developer  Button.....................       
        img10 = Image.open("E:/project/img/developer.jpg")
        img10 = img10.resize((210,190), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b7.place(x=720, y=370, width=210, height=190)


        b7_1 = Button(bg_img,text='DEVELOPER', cursor="hand2",command=self.developer_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b7_1.place(x=720, y=550, width=210, height=40)


# Exit Button.....................       
        img11 = Image.open("E:/project/img/exit.jpg")
        img11 = img11.resize((210,190), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b8.place(x=1020, y=370, width=210, height=190)


        b8_1 = Button(bg_img,text='EXIT', cursor="hand2",command=self.iExit,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b8_1.place(x=1020, y=550, width=210, height=40)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition System", "do you want to exit",parent=self.root)
        if  self.iExit > 0:
            self.root.destroy()
        else:
            return


# ==============================Function Buttons====================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
 