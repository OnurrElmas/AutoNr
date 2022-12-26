import tkinter as tk    
from tkinter import ttk
from tkinter import *

lues=["Choice 1","Second choice","Something","Else"]
boxes=["Tesxt1","Tesxt2","Tesxt3","Tesxt4"]
class ComboboxSelectionWindow():
    def __init__(self, master):
        self.master=master
        self.entry_contents=None
        self.labelTop = tk.Label(master,text = "Select one of the SW Version")
        self.labelTop.place(x = 30, y = 10, width=140, height=10)
        self.comboBox_example = ttk.Combobox(master,values=lues)
        self.comboBox_example.current(0)
        self.comboBox_example.place(x = 20, y = 30, width=140, height=25)

        self.okButton = tk.Button(master, text='OK',command = self.callback)
        self.okButton.place(x = 20, y = 60, width=140, height=25)

    def callback(self):
        """ get the contents of the Entry and exit
        """
        self.comboBox_example_contents=self.comboBox_example.get()
        self.master.destroy()
        
def ComboboxSelection():

    app = tk.Tk()
    app.geometry('500x250')
    Selection=ComboboxSelectionWindow(app)
    app.mainloop()

    #print("Selected interface: ", Selection.comboBox_example_contents)

    return Selection.comboBox_example_contents


class CheckBoxSelectionWindow():
    def __init__(self, master):
        self.master=master
        self.entry_contents=None
        self.chvar = tk.IntVar()
        self.chvar.set(0)
        self.checkbox_example = ttk.Checkbutton(master,text=box,variable=self.chvar).grid(row,column)
        

        self.okButton = tk.Button(master, text='OK',command = self.callback)
        self.okButton.place(x = 20, y = 60, width=140, height=25)

    def callback(self):
        """ get the contents of the Entry and exit
        """
        #print(self.chvar.get())
        self.master.destroy()

def CheckBoxSelection():

    app = tk.Tk()
    app.geometry('500x250')
    Selection=CheckBoxSelectionWindow(app)
    app.mainloop()
    
    #print("Selected interface: ", Selection.comboBox_example_contents)

    return Selection.chvar.get()



comboselection = ComboboxSelection()
seconselection = CheckBoxSelection()
print(comboselection)
print(seconselection)