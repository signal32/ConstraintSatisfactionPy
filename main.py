#import lm_Conditions as lmcs
from sys import maxsize
from tkinter.ttk import Treeview
import LetsMeet as lm
from datetime import date, datetime

import tkinter as tk
import tkinter.ttk as ttk

from forms import *
# Setup conditions for event
#https://www.askpython.com/python-modules/tkinter/tkinter-treeview-widget

class Application(tk.Frame):
    def __init__(self, root) -> None:
        self.root = root
        self.UI()

    # Initilaise UI
    def UI(self):
        #Configure application root
        self.root.title("Let's Meet Tech Demo")
        self.root.grid_rowconfigure(1, minsize=1)
        self.root.grid_columnconfigure(4, minsize=1)

        #Define UI widgets
        self.setDatesButton = tk.Button(self.root,text="Add event date",command=lambda: EnterDateRange(self.root,self.setDateRange))
        self.setDatesButton.grid(row=0,column=0,sticky='nsew')

        self.setUsersButton = tk.Button(self.root,text="Add required user")
        self.setUsersButton.grid(row=0,column=1,sticky='nsew')

        self.idnumber_label = tk.Label(self.root, text="ID")
        self.idnumber_entry = tk.Entry(self.root)
        self.idnumber_label.grid(row=1, column=0, sticky=tk.W)
        self.idnumber_entry.grid(row=1, column=1)
 
        self.submit_button = tk.Button(self.root, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=1, column=1, sticky=tk.W)
 
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=3)

        # Set treeview
        self.tree = ttk.Treeview(self.root,columns=('Value','Type','ID'))

        # Set headings
        self.tree.heading('#0',text='Item')
        self.tree.heading('#1',text='Value')
        self.tree.heading('#2',text='Type')
        self.tree.heading('#3',text='ID')

        # Set attribites
        self.tree.column('#0', width=150, minwidth=100, stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)        
        self.tree.column('#3', stretch=tk.YES)

        self.eventFolder = self.tree.insert("",0,text="Event",values=(str(eventManager.event.name),"Collection",str(eventManager.event.uuid)))        
        self.userFolder = self.tree.insert("",1,text="Users",values=("","Collection"))

        self.tree.grid(row=4, columnspan=9, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def popupUser(self):
        self.popupUser

    def insert_data(self):
        self.treeview.insert('', 'end', iid=self.iid, text="Item_" + str(self.id),
                            values=("Name: " + self.name_entry.get(),
                                    self.idnumber_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1

    def insertDomain(self,event:bool, name, value, id, ):
        if event:
            x = self.eventFolder
        else:
            x = 'User'
        self.treeview.insert(x,'end',iid=self.iid,text=str(name),values=(str(value),"Domain",str(id)))
        self.iid = self.iid + 1
        self.id = self.id + 1

    def openSetDates(self):
        #setDatesWindow = tk.Toplevel(self.root)
        setDatesWindow = EnterDateRange(self.root,self.setDateRange)

        val = conditionManager.setDateRange(datetime(2019,1,9),datetime(2019,1,20))
        self.insertDomain(True,"Date","09/10/20 -> 12/10/20",val)
        
    def setDateRange(self,d1_d,d1_m,d1_y,d2_d,d2_m,d2_y):
        val = conditionManager.setDateRange(datetime(d1_y,d1_m,d1_d),datetime(d2_y,d2_m,d1_d))
        self.insertDomain(True,"Date","%s/%s/%s -> %s/%s/%s" %(d1_d,d1_m,d1_y,d2_d,d2_m,d2_y) ,val)
           

if __name__ == "__main__":
    
    # Get ourselves a manager
    eventManager = lm.EventManager.Manager()
    eventManager.initBlank()

    # get an condition manager
    conditionManager = lm.ConditionManager.Manager()
    conditionManager.event = eventManager.event # This is a bodge to get around lack of pointers in python
    c1 = conditionManager.getID()
    
    print(conditionManager.conditionSet)

    app = Application(tk.Tk())
    app.root.mainloop()