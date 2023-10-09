from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",38,"bold"),fg="white",bg="blue") 
        title_lbl.place(x=0,y=0,width=1366,height=55)


        img_top = Image.open("img/help1.jpg")
        img_top = img_top.resize((1366,685), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1366, height=685)


        dev_lable=Label(f_lbl,text="Email : vvadoliya616@rku.ac.in",font=("times new roman",19,"bold"),bg="white",fg="blue")
        dev_lable.place(x=600,y=430)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop() 

