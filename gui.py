from tkinter import *
import os
from PIL import ImageTk, Image

#Main Screen
master = Tk()
master.title('Banking App')

#Import Image
img = Image.open('bank-thumbnail.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "Custom Banking", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "Best Banking Solution", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)