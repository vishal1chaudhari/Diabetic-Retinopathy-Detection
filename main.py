# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:46:34 2022

@author: Lenovo
"""



import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="grey")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Diabetic Retinopathy Detection ")

# 

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('reg3.png')
image2 = image2.resize((2000, 1000), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  


def log():
    from subprocess import call
    call(["python","login.py"])

def reg():
    from subprocess import call
    call(["python","registration.py"])


  
def window():
  root.destroy()

        

button1 = tk.Button(root, text="Sign In ", command=log, width=15, height=1,font=('times', 20, ' bold '), bg="Blue", fg="white")
button1.place(x=50, y=300)

button2 = tk.Button(root, text="Sign Up", command=reg, width=15, height=1,font=('times', 20, ' bold '), bg="Blue", fg="white")
button2.place(x=330, y=300)



button4 = tk.Button(root, text="Exit",command=window,width=15, height=1,font=('times', 20, ' bold '), bg="Red", fg="white")
button4.place(x=170, y=400)

root.mainloop()
