from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",38,"bold"),fg="white",bg="blue") 
        title_lbl.place(x=0,y=0,width=1366,height=55)


        img_top = Image.open("E:/project/img/dev3.jpg")
        img_top = img_top.resize((1366,685), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1366, height=685)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=865,y=0,width=500,height=550)


        img_top1=Image.open("E:/project/img/pic1.jpg")
        img_top1=img_top1.resize((200,300),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=300)

# developer info.....................................
        dev_lable=Label(main_frame,text="Hello, My name is Vivek.",font=("times new roman",19,"bold"),bg="white",fg="blue")
        dev_lable.place(x=0,y=5)

        dev_lable=Label(main_frame,text="I am B.TECH student.",font=("times new roman",19,"bold"),bg="white",fg="blue")
        dev_lable.place(x=0,y=40)

        img2 = Image.open("E:/CHINTAN/SEM 4/python/project/img/main1.jpg")
        img2 = img2.resize((500, 300), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=250, width=500, height=300)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop() 