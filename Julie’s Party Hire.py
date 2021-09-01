from tkinter import *
from tkinter import Tk
from tkinter.font import Font



def delete_one():
    pass

def delete_several():
    pass

def print():
    pass

def print():
    pass

main_window = Tk()
main_window.title(" Julia's Party Hire ")
main_window.geometry('500x500')
main_window.iconbitmap('E:/Document/DGT/Programming/My Assement/logo.jpg')

fontButton = Font(
    family="Times",
    size=10,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0)

fontLabel = Font(
    family="Menlo",
    size=12,
    weight="normal",
    slant="roman",
    underline=0,
    overstrike=0)

#Creating Label 
customer_name_label = Label(main_window, text="Customer Name", font=fontLabel)
receipt_number_label = Label(main_window, text="Receipt Number", font=fontLabel)
item_hired_label = Label(main_window, text="Item Hired", font=fontLabel)
number_hired_label = Label(main_window, text="Number Hired", font=fontLabel)

#Creating Entry Box
customer_name_entry = Entry(main_window, width=50)
receipt_number_entry = Entry(main_window, width=50)
item_hired_entry = Entry(main_window, width=50)
number_hired_entry = Entry(main_window, width=50)

#Creating Button
delete_one = Button(main_window, text='Delete', width=7, command=delete_one)
delete_several = Button(main_window, text='Delete More', width=12, command=delete_several)
quit = Button(main_window, text='Quit', width=7, command=quit)
print = Button(main_window, text='Print', width=7, command=print)


'''I decided to position Label,EntryBox,Button and other widget different from its
original line becuase it looks cleaner and more organise.'''
#Position of Lable
customer_name_label.grid(row=2, column=0, ipady=7, ipadx=7)
receipt_number_label.grid(row=3, column=0, ipady=7, ipadx=7)
item_hired_label.grid(row=4, column=0, ipady=7, ipadx=7)
number_hired_label.grid(row=5, column=0, ipady=7, ipadx=7)
#Position of Entry Box
customer_name_entry.grid(row=2, column=1, ipady=4, ipadx=4)
receipt_number_entry.grid(row=3, column=1, ipady=4, ipadx=4)
item_hired_entry.grid(row=4, column=1, ipady=4, ipadx=4)
number_hired_entry.grid(row=5, column=1, ipady=4, ipadx=4)
#Position of Button
delete_one.grid(row=0, column=3, ipadx=5, ipady=5, padx=30)
delete_several.grid(row=0, column=2, ipadx=5, ipady=5, padx=30)
quit.grid(row=0, column=0, ipadx=5, ipady=5)
print.grid(row=0, column=1, ipadx=5, ipady=5)



main_window.mainloop()
