from tkinter import *
from tkinter import ttk
from tkinter.font import Font

def delete_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
count=0
row=0
def delete_several():
    x = my_tree.selection()[0]
    for record in x:
        my_tree.delete(record)

def quit():
    main_window.destroy()

def print():
    global count
    my_tree.insert(parent='', index='end', iid=count, text='',
               values=(customer_name_entry.get(), receipt_number_entry.get(),
                       number_hired_entry.get(), item_hired_entry.get()))
    count +=1
    row +=1
    customer_name_entry.delete(0,END)
    receipt_number_entry.delete(0,END)
    number_hired_entry.delete(0,END)
    item_hired_entry.delete(0,END)

def validate():
    input_check = 0
    if len(customer_name_entry.get()) == 0:
        c_error['text']="Required"
        input_check = 1
    if len(receipt_number_entry.get()) == 0:
        r_error['text']="Required.   Type in number only"
        input_check = 1
    if len(number_hired_entry.get()) == 0:
        n_error['text']="Required.   Type in number between 1-500 only"
        input_check = 1
    if len(item_hired_entry.get()) == 0:
        i_error['text']="Required"
        input_check = 1


 #Changing btn colour when hover and when leave
def quitColour_hover(e):
    quit['bg']="#555555"
    quit['fg']="White"
def printColour_hover(e):
    print['bg']="#555555"
    print['fg']="White"
def delColour_hover(e):
    delete_one['bg']="#555555"
    delete_one['fg']="White"
def dColour_hover(e):
    delete_several['bg']="#555555"
    delete_several['fg']="White"
def validateColour_hover(e):
    validate['bg']="#555555"
    validate['fg']="White"
    
def quitColour_leave(e):
    quit['bg']="SystemButtonFace"
    quit['fg']="Black"
def printColour_leave(e):
    print['bg']="SystemButtonFace"
    print['fg']="Black"
def delColour_leave(e):
    delete_one['bg']="SystemButtonFace"
    delete_one['fg']="Black"
def dColour_leave(e):
    delete_several['bg']="SystemButtonFace"
    delete_several['fg']="Black"
def validateColour_leave(e):
    validate['bg']="SystemButtonFace"
    validate['fg']="Black"


main_window = Tk()
main_window.title(" Julia's Party Hire ")
main_window.geometry('800x550')
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
customer_name_label = Label(main_window, text="Customer Name:", fg='#020c0a', font=fontLabel)
c_error = Label(main_window, text="", fg='red')
receipt_number_label = Label(main_window, text="Receipt Number:", fg='#020c0a', font=fontLabel)
r_error = Label(main_window, text="", fg='red')
item_hired_label = Label(main_window, text="Item Hired:", fg='#020c0a', font=fontLabel)
i_error = Label(main_window, text="", fg='red')
number_hired_label = Label(main_window, text="Number Hired:", fg='#020c0a', font=fontLabel)
n_error = Label(main_window, text="", fg='red')

#Creating Entry Box
customer_name_entry = Entry(main_window, width=47)
receipt_number_entry = Entry(main_window, width=47)
item_hired_entry = Entry(main_window, width=47)
number_hired_entry = Entry(main_window, width=47)



#This section of coding is related to BUTTON (hovering and styling)
#Creating Button
delete_one = Button(main_window, text='Delete One', font=fontButton, fg="#00030a", width=12, command=delete_one)
delete_several = Button(main_window, text='Delete More', font=fontButton, fg="#00030a", width=12, command=delete_several)
quit = Button(main_window, text='Quit', font=fontButton, fg="#00030a", width=7, command=quit)
print = Button(main_window, text='Print', font=fontButton, fg="#00030a", width=7, command=print)
validate = Button(main_window, text='Validate Input', font=fontButton, fg="#00030a", width=12, command=validate)
#Changing buttons' colour when hovering
quit.bind("<Enter>", quitColour_hover)
quit.bind("<Leave>", quitColour_leave)
print.bind("<Enter>", printColour_hover)
print.bind("<Leave>", printColour_leave)
delete_one.bind("<Enter>", delColour_hover)
delete_one.bind("<Leave>", delColour_leave)
delete_several.bind("<Enter>", dColour_hover)
delete_several.bind("<Leave>", dColour_leave)
validate.bind("<Enter>", validateColour_hover)
validate.bind("<Leave>", validateColour_leave)



#This section of coding are related to TREEVIEW WEDGIT
#Creating a Treeview widget for the information to be print out
my_tree = ttk.Treeview(main_window)
'''Define the column of the Treeview.
In this case I decide to have 5 column one for each Label and another one is for ROW'''
#Define the column
my_tree['columns'] =('Row', 'Customer Name', 'Receipt Number', 'Item Hire', 'Number Hire')
#Formate Our columns
my_tree.column('#0', width=0, minwidth=0)
my_tree.column('Row', anchor=W, width=60)
my_tree.column('Customer Name', anchor=CENTER, width=125)
my_tree.column('Receipt Number', anchor=CENTER, width=105)
my_tree.column('Item Hire', anchor=CENTER, width=95)
my_tree.column('Number Hire', anchor=CENTER, width=85)
#Create Heading
my_tree.heading('#0', text="", anchor=W)
my_tree.heading('Row', text="Row No.", anchor=W)
my_tree.heading('Customer Name', text="Customer Name", anchor=CENTER)
my_tree.heading('Receipt Number', text="Receipt Number", anchor=CENTER)
my_tree.heading('Item Hire', text="Item Hire", anchor=CENTER)
my_tree.heading('Number Hire', text='Number Hire', anchor=CENTER)



#This section of coding are related to POSITION of wedgit
'''I decided to position Label,EntryBox,Button and other widgets different from its
original line becuase it looks cleaner and more organise.'''
#Position of Lable
customer_name_label.grid(row=2, column=0, ipadx=5, ipady=5, sticky=E)
receipt_number_label.grid(row=3, column=0, ipadx=5, ipady=5, sticky=E)
item_hired_label.grid(row=5, column=0, ipadx=5, ipady=5, sticky=E)
number_hired_label.grid(row=4, column=0, ipadx=5, ipady=5, sticky=E)
c_error.grid(row=2, column=3, ipadx=5, sticky=W)
r_error.grid(row=3, column=3, ipadx=5, sticky=W)
i_error.grid(row=5, column=3, ipadx=5, sticky=W)
n_error.grid(row=4, column=3, ipadx=5, sticky=W)
#Position of Entry Box
customer_name_entry.grid(row=2, column=1, ipady=4, pady=9, ipadx=4, sticky=W)
receipt_number_entry.grid(row=3, column=1, ipady=4, pady=9, ipadx=4, sticky=W)
item_hired_entry.grid(row=5, column=1, ipady=4, pady=9, ipadx=4, sticky=W)
number_hired_entry.grid(row=4, column=1, ipady=4, ipadx=4, sticky=W)
#Position of Button
delete_one.grid(row=10, column=3, ipadx=5, ipady=3, padx=10, sticky=W)
delete_several.grid(row=11, column=3, ipadx=5, ipady=3, padx=10, sticky=W)
quit.grid(row=0, column=0, ipady=5, pady=10, padx=50, sticky=E)
print.grid(row=9, column=3, ipadx=5, ipady=2, pady=10, padx=10, sticky=W)
validate.grid(row=8, column=3, ipadx=5, ipady=2, pady=10, padx=10, sticky=W)
#Position of Treeview
my_tree.grid(row=7, columnspan=2, rowspan=5, padx=25, pady=10, ipady=5, sticky=W)


main_window.mainloop()
