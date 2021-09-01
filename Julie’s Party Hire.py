from tkinter import *
from tkinter import Tk
from tkintet.font import Font

main_window = Tk()
main_window.title(" Julia's Party Hire ")
main_window.geometry('500x500')
main_window.iconbitmap('E:/Document/DGT/Programming/My Assement/logo.jpg')

fontButton = Font(
    family="Times",
    size=14,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0)

fontLabel = Font(
    family="Helvetica",
    size=16,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0)


customer_name_label = Label(main_window, text="Customer Name", font=fontLabel)
receipt_number_label = Label(main_window, text="Receipt Number", font=fontLabel)
item_hired_label = Label(main_window, text="Item Hired", font=fontLabel)
number_hired_label = Label(main_window, text="Number HIred", font=fontLabel)


customer_name_label.grid(row=2, column=0, ipady=7, ipadx=7)
receipt_number_label.grid(row=3, column=0, ipady=7, ipadx=7)
item_hired_label.grid(row=4, column=0, ipady=7, ipadx=7)
number_hired_label.grid(row=5, column=0, ipady=7, ipadx=7)






main_window.mainloop()
