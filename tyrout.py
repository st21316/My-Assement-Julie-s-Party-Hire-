#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Define a function to change the value
def change_text(txt):
   text.delete(0,END)
   text.insert(0,txt)

#Set the geometry of frame
win.geometry("600x250")

#Create an Entry Widget
text= Entry(win)
text.pack()

#Create a button to change/set the content
btn= Button(win,text="Set", command=lambda:change_text("My New Text"))
btn.pack(pady=20)
win.mainloop()
