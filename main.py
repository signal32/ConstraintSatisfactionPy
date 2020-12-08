#import lm_Conditions as lmcs
from tkinter import IntVar
from LetsMeet.ConditionManager import variable
from LetsMeet.ConditionManager.ConditionSet import ConditionSet
from sys import maxsize
from tkinter.ttk import Treeview
import LetsMeet as lm
from datetime import date, datetime, time
import time

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from forms import *


class Application(tk.Frame):
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.UI()
        self.events = []
        self.selection = {}
        self.eastereggCount = 0

        self.root.iconphoto(True, tk.PhotoImage(file='icon.png'))

    # Devines UI layout and configuration
    def UI(self):
        #Configure application root
        self.root.title("Let's Meet Tech Demo")
        #self.root.geometry("800x600")
        self.root.grid_rowconfigure(2, minsize=10)
        self.root.grid_columnconfigure(4, minsize=1)
        

        #Define UI widgets
        self.addEventButton = tk.Button(self.root,text="+",command=self.addEvent)
        self.addEventButton.grid(row=1,column=1,sticky='nsew')

        self.setDatesButton = tk.Button(self.root,text="Add event date",command=lambda: EnterDateRange(self.root,self.setDateRange))
        self.setDatesButton.grid(row=3,column=0,columnspan=2,sticky='nsew')

        self.setUsersButton = tk.Button(self.root,text="Add user date",command=lambda: EnterDateRange(self.root,self.addUserdateRange))
        self.setUsersButton.grid(row=4,column=0,columnspan=2,sticky='nsew')

        self.idnumber_label = tk.Label(self.root, text="Add Event:")
        self.idnumber_entry = tk.Entry(self.root)
        self.idnumber_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        self.idnumber_entry.grid(row=1, column=0,sticky='nsew')

        self.spewButton = tk.Button(self.root, text="Debug Selected", command=self.debug)
        self.spewButton.grid(row=7,column=0,columnspan=2,sticky='nsew')

        self.exportButton = tk.Button(self.root, text="Print Event Config", command=self.printConfig)
        self.exportButton.grid(row=6,column=0,sticky='nsew')

        self.exportButtonValue = IntVar()
        self.exportButton = tk.Checkbutton(self.root, text="All",variable=self.exportButtonValue)
        self.exportButton.grid(row=6,column=1)
        
        self.solveButton = tk.Button(self.root,background="red",foreground="white", text="Run Solver", command=self.solveEvent)
        self.solveButton.grid(row=9,rowspan=2,column=0,columnspan=2,sticky='nsew')

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

        #self.eventFolder = self.tree.insert("",0,text="Event",values=(str(eventManager.event.name),"Collection",str(eventManager.event.uuid)))        
        #self.userFolder = self.tree.insert("",1,text="Users",values=("","Collection"))

        self.tree.grid(row=0,rowspan=10, column=2,columnspan=9)
        self.treeview = self.tree
        self.id = 0
        self.iid = 0

    def popupUser(self):
        self.popupUser

    # Print values to terminal
    def debug(self):
        print("______Selected_______")
        print("ID: ",self.getCurrentValues())
        print("Contents: ",self.getCurrentTreeID())
        print("Children: ", self.treeview.get_children(self.getCurrentTreeID()))
        print("_______Global________")
        print("Events: ", self.events)

    # Print the configuration of an event to the terminal
    def printConfig(self):
        text = "Export - " + str(datetime.now()) + "\n " + str(len(self.events)) + "\n"
        if (self.exportButtonValue.get()==0):
            print("\n_______Event______")
            self.getEvent(self.getCurrentValues()[2]).printFull()
        else:
            for event in self.events:
                if isinstance(event,lm.EventManager.Event):
                    print("\n_______Event______")
                    event.printFull()
        return

    # Get's the entry ID of the currently selected element in the treeview
    def getCurrentTreeID(self):
        try:
            return self.treeview.selection()[0]
        except Exception as err:
            exception_type = type(err).__name__
            warning = messagebox.showerror("Error",exception_type + "\nAn event must be selected.")
            print(exception_type)

    # Gets the data from a row in the treeview as array. [0] = string, [1] = type, [2] = UUID (if a LM object)
    def getCurrentValues(self):
        try:
            return self.treeview.item(self.treeview.focus())['values']
        except Exception as err:
            exception_type = type(err).__name__
            warning = messagebox.showerror("Error",exception_type + "\nAn event must be selected.")
            print(exception_type)
 

    # Returns the event object with specified UUID
    def getEvent(self,uuid)-> lm.EventManager.Event:
        for event in self.events:
            if str(event.uuid) == uuid:
                return event
        raise Exception("ERR: Event not found") 
    
    # Depreciated, use treeInsert()
    def insert_data(self):
        self.treeview.insert('', 'end', iid=self.iid, text="Item_" + str(self.id),
                            values=("Name: " + self.name_entry.get(),
                                    self.idnumber_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1

    # Creates a new event and stores it in global event array
    def addEvent(self):
        if self.eastereggCount >3:
            box = messagebox.askyesnocancel("Based on your estimated age...","Would you like to hire a bouncy castle?")
            self.eastereggCount = -5
        event = lm.EventManager.Manager()
        event.initBlank()
        if(len(self.idnumber_entry.get())>1):
            event.setProperty('name',self.idnumber_entry.get())
        self.events.append(event.event)
        root = self.treeInsert(event.event)
        self.treeInsert("DOMAINHOLDER",root)
        self.treeInsert("CONSTRAINTHOLDER",root)
        self.treeInsert("USERHOLDER",root)
        self.idnumber_entry.delete(0,'end')
        self.eastereggCount += 1

    # Depreciated - use setdaterange()
    def insertDomain(self,event:bool, name, value, id, ):
        if event:
            x = self.eventFolder
        else:
            x = 'User'
        self.treeview.insert(x,'end',iid=self.iid,text=str(name),values=(str(value),"Domain",str(id)))
        self.iid = self.iid + 1
        self.id = self.id + 1

    # Put's the given element into the treeview below parent (if specified)
    def treeInsert(self,element,parent = None):
        #current = self.treeview.item(self.treeview.focus())
        #item = self.treeview.selection()[0]
        self.iid = self.iid + 1
        self.id = self.id + 1

        insertID = self.iid
        if isinstance(element,lm.EventManager.Event):
            self.treeview.insert('','end',iid=self.iid,text=str(element.name),values=("","Event",str(element.uuid)))
        elif isinstance(element,variable.Variable):
            self.treeview.insert(parent,'end',iid=self.iid,text=str(element.name),values=(str(element.domain),"Variable",str(element.uuid)))
        elif isinstance(element,lm.ConditionManager.ConditionSet):
            id=self.treeview.insert(parent,'end',iid=self.iid,text=str(element.name),values=("","ConditionSet",str(element.uuid)))
            print("id:",id)
            for x in element.variables:
                self.treeInsert(element.variables,id) 
            for x in element.constraints:
                self.treeInsert(element.constraints,id) 
            pass
        elif element == "CONSTRAINTHOLDER":
            self.treeview.insert(parent,'end',iid=self.iid,text=str("Constraints"),values=("","ui_ConstraintGroup",str(self.iid)))
        elif element == "DOMAINHOLDER":
            self.treeview.insert(parent,'end',iid=self.iid,text=str("Domains"),values=("","ui_DomainGroup",str(self.iid)))
        elif element == "USERHOLDER":
            self.treeview.insert(parent,'end',iid=self.iid,text=str("Users"),values=("","ui_UserGroup",str(self.iid)))
        else:
            print(parent)
            self.treeview.insert(parent,'end',iid=self.iid,text=str("UNDEFINED"),values=(str(element),"UNDEFINED",str(self.iid)))
        return insertID
    
    # Sets date range on selected event
    def setDateRange(self,d1_d,d1_m,d1_y,d1_thh,d1_tmm,d2_d,d2_m,d2_y,d2_thh,d2_tmm):
        try:
            event = self.getEvent(self.getCurrentValues()[2])
            #variable = lm.ConditionManager.Variable((datetime(d1_y,d1_m,d1_d),datetime(d2_y,d2_m,d1_d)))
            variable = lm.ConditionManager.Variable([lm.ConditionManager.types.DateRange(datetime(d1_y,d1_m,d1_d,d1_thh,d1_tmm),datetime(d2_y,d2_m,d2_d,d2_thh,d2_tmm))])
            event.eventMain = variable.uuid
            event.event.addVariable(variable)
            self.treeInsert(variable,self.treeview.get_children(self.getCurrentTreeID())[0])
        except Exception as err:
            exception_type = type(err).__name__
            warning = messagebox.showerror("Error",exception_type + "\nAn event must be selected.")
            print(exception_type)

    """Creates conditionSet for user which specifies their avaliability"""      
    def addUserdateRange(self,d1_d,d1_m,d1_y,d1_thh,d1_tmm,d2_d,d2_m,d2_y,d2_thh,d2_tmm):
        try:
            #Create the data structure
            event = self.getEvent(self.getCurrentValues()[2])

        except Exception as err:
            exception_type = type(err).__name__
            warning = messagebox.showerror("Error",exception_type + "\nAn event must be selected.")
            print(exception_type)
            return
        
        try:
            participant2 = event.addUserConditionSet(lm.ConditionManager.ConditionSet())
            event.users[participant2.uuid].name = " (participant" + str(len(event.users)) +")"
            userDate2 = event.users[participant2.uuid].addVariable(lm.ConditionManager.Variable([lm.ConditionManager.types.DateRange(datetime(d1_y,d1_m,d1_d,d1_thh,d1_tmm),datetime(d2_y,d2_m,d2_d,d2_thh,d2_tmm))]))
            event.users[participant2.uuid].addConstraint(lm.ConditionManager.Constraint((event.event.variables[event.eventMain], userDate2), "="))

            #Populate the UI
            self.treeInsert(participant2,self.treeview.get_children(self.getCurrentTreeID())[2])
        except Exception as err:
            exception_type = type(err).__name__
            warning = messagebox.showerror("Error",exception_type + "\nEvent must have valid date")
            print(exception_type)

    #Will solve the currently selected event
    def solveEvent(self):
        try:
            event  = self.getEvent(self.getCurrentValues()[2])
            print("run solver and print in terminal")
            solver = lm.EventManager.Solver(event)
            
            solver.solve()
            print(solver.matches)
            if len(solver.matches)==0:
                warning = messagebox.showwarning("No matches","No matches found.")
            else:
                confirmation = messagebox.showinfo("Results","Matches:\n"+ str(solver.matches)+"\nBest Match:\n"+str(solver.matchesMax()))
        except Exception as err:
            exception_type = type(err).__name__
            warning = messagebox.showerror("Error",exception_type + "\nAn event must be selected.")
            print(exception_type)


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