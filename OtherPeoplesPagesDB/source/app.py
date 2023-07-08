#store client info, name, url, email, how case was settled if there was one, how much i charged

from tkinter import *
import backend


def getSelectedRow(event):
    global selectedRowData
    index=displayField.curselection()[0]
    selectedRowData = displayField.get(index)
    entrybox1.delete(0,END)
    entrybox1.insert(END,selectedRowData[1])
    entrybox2.delete(0,END)
    entrybox2.insert(END,selectedRowData[4])
    entrybox3.delete(0,END)
    entrybox3.insert(END,selectedRowData[2])
    entrybox4.delete(0,END)
    entrybox4.insert(END,selectedRowData[5])
    entrybox5.delete(0,END)
    entrybox5.insert(END,selectedRowData[3])    

def view_command():
    displayField.delete(0,END)
    for row in backend.view():
        displayField.insert(END, row)

def search_command():
    displayField.delete(0,END)
    for row in backend.search(Client_Name.get(),Client_Email.get(),Resolution.get(),Client_URL.get(),Charged.get()):
        displayField.insert(END,row)

def add_command():
    backend.insert(Client_Name.get(),Client_Email.get(),Resolution.get(),Client_URL.get(),Charged.get())
    displayField.delete(0,END)
    view_command()

def update_command():
    backend.update(selectedRowData[0],Client_Name.get(),Client_Email.get(),Resolution.get(),Client_URL.get(),Charged.get())
    view_command() 

def delete_command():
    backend.delete(selectedRowData[0])
    view_command()

window = Tk()
window.wm_title("Other People's Pages Client Database")
photo = PhotoImage(file = "opp_icon.png")
window.iconphoto(False, photo)

data1 = Label(window,text="Client Name:")
data1.grid(row=0,column=0)
data2 = Label(window,text="URL:")
data2.grid(row=1,column=0)
data3 = Label(window,text="Client Email:")
data3.grid(row=0,column=2)
data4 = Label(window,text="How Much I Charged:")
data4.grid(row=1,column=2)
data5 = Label(window,text="Case Resolution:")
data5.grid(row=0,column=4)

Client_Name = StringVar()
entrybox1 = Entry(window,textvariable=Client_Name)
entrybox1.grid(row=0,column=1)
Client_URL = StringVar()
entrybox2 = Entry(window,textvariable=Client_URL)
entrybox2.grid(row=1,column=1)
Client_Email = StringVar()
entrybox3 = Entry(window,textvariable=Client_Email)
entrybox3.grid(row=0,column=3)
Charged = StringVar()
entrybox4 = Entry(window,textvariable=Charged)
entrybox4.grid(row=1,column=3)
Resolution = StringVar()
entrybox5 = Entry(window,textvariable=Resolution)
entrybox5.grid(row=0,column=5)

displayField = Listbox(window, height = 6, width = 90)
displayField.grid(row=2,column=0,rowspan=6,columnspan=6)
fieldScrollBar = Scrollbar(window)
fieldScrollBar.grid(row=2,column=5,rowspan=6)

displayField.configure(yscrollcommand=fieldScrollBar.set)
fieldScrollBar.configure(command=displayField.yview)

displayField.bind('<<ListboxSelect>>', getSelectedRow)

displayButton = Button(window,text="Display All", width=14,command=view_command)
displayButton.grid(row=8,column=0)
displayButton = Button(window,text="Search for Entry", width=14,command=search_command)
displayButton.grid(row=8,column=1)
displayButton = Button(window,text="Add Entry", width=14,command=add_command)
displayButton.grid(row=1,column=4)
displayButton = Button(window,text="Update Entry", width=14,command=update_command)
displayButton.grid(row=8,column=4)
displayButton = Button(window,text="Delete Entry", width=14,command=delete_command)
displayButton.grid(row=8,column=5)


window.mainloop()