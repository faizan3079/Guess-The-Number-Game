# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *
import tkinter.messagebox as mb
import random as rd
a=rd.randint(0,100)
# creating tkinter window
root = Tk()
root.geometry('800x600+410+110')
root.title("Guessing The Number Game")
pic= PhotoImage(file= r'F:\Mini Projects\Guess The Number\num.png')
root.iconphoto(False, pic)
# Adding widgets to the root window
  
# Creating a photoimage object to use image
bg = PhotoImage(file = r"F:\Mini Projects\Guess The Number\back.png")

def task():
    num=e1.get()

    if(int(num)==a):
        mb.showinfo("Congrats","This is The number You selected")
    
    elif(int(num)>100):
        mb.showerror("Error","The Number should be between 1 and 100")

    elif(int(num)>a):
        mb.showwarning("Oops","Enter a smaller number")    

    elif(int(num)<a):
        mb.showwarning("Oops","Enter a larger number")  
    elif(num!=int(num)):
        mb.showerror("Error","enter an Integer value")




# here, image option is used to
# set image 
label = Label(root, image = bg)
label.place(x=0,y=0,relheight=1,relwidth=1)
b1=Button(root,text="Enter the number:",command=task)
e1=Entry(root,  width=20, font=('Ubuntu', 15))
e1.place(x=300,y=400)
b1.place(x=350,y=350)

mainloop()