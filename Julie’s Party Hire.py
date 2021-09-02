from tkinter import *
from tkinter import ttk
from tkinter.font import Font

def delete_one():
    pass

def delete_several():
    pass

def quit():
    main_window.destroy()

def print():
    pass


main_window = Tk()
main_window.title(" Julia's Party Hire ")
main_window.geometry('500x500')
main_window.iconbitmap('E:/Document/DGT/Programming/My Assement/logo.jpg')

#Creating a font-style for text in Button
fontButton = Font(
    family="Hack",
    size=11,
    weight="normal",
    slant="roman",
    underline=0,
    overstrike=0)
#Creating a font-style for label text
fontLabel = Font(
    family="DejaVu Sans Mono",
    size=11,
    weight="normal",
    slant="roman",
    underline=0,
    overstrike=0)

#Creating Label 
customer_name_label = Label(main_window, text="Customer Name", fg='#020c0a', font=fontLabel)
receipt_number_label = Label(main_window, text="Receipt Number", fg='#020c0a', font=fontLabel)
item_hired_label = Label(main_window, text="Item Hired", fg='#020c0a', font=fontLabel)
number_hired_label = Label(main_window, text="Number Hired", fg='#020c0a', font=fontLabel)

#Creating Entry Box
customer_name_entry = Entry(main_window, width=50)
receipt_number_entry = Entry(main_window, width=50)
item_hired_entry = Entry(main_window, width=50)
number_hired_entry = Entry(main_window, width=50)

#Creating Button
delete_one = Button(main_window, text='Delete', font=fontButton, fg="#00030a", width=7, command=delete_one)
delete_several = Button(main_window, text='Delete More', font=fontButton, fg="#00030a", width=12, command=delete_several)
quit = Button(main_window, text='Quit', font=fontButton, fg="#00030a", width=7, command=quit)
print = Button(main_window, text='Print', font=fontButton, fg="#00030a", width=7, command=print)

#Creating a Treeview widget for the information to be print out
my_tree = ttk.Treeview(main_window)
'''Define the column of the Treeview.
In this case I decide to have 5 column one for each Label and another one is for ROW'''
#Define our column
my_tree['columns'] =('Row', 'Customer Name', 'Receipt Number', 'Item Hire', 'Number Hire')
#Formate Our columns
my_tree.column('#0', width=0, minwidth=0)
my_tree.column('Row', anchor=W, width=90)
my_tree.column('Customer Name', anchor=W, width=140)
my_tree.column('Receipt Number', anchor=W, width=140)
my_tree.column('Item Hire', anchor=W, width=120)
my_tree.column('Number Hire', anchor=W, width=120)
#Create Heading
my_tree.heading('#0', text="", anchor=W)
my_tree.heading('Row', text="Row", anchor=W)
my_tree.heading('Customer Name', text="Customer Name", anchor=W)
my_tree.heading('Receipt Number', text="Receipt Number", anchor=W)
my_tree.heading('Item Hire', text="Item Hire", anchor=W)
my_tree.heading('Number Hire', text='Number Hire', anchor=W)


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
#Position of Treeview
my_tree.grid(row=7, columnspan=3)


main_window.mainloop()
