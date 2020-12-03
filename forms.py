from datetime import date
import tkinter as tk
import tkinter.ttk as ttk

class EnterDateRange(tk.Toplevel):
    def __init__(self, root,confirm_method) -> None:
        tk.Toplevel.__init__(self, root)
        self.root = root
        self.UI()
        self.confirm_method = confirm_method

    def UI(self):
        self.geometry("410x110")
        self.title("Enter Dates")
        self.grid_rowconfigure(4, minsize=1)
        self.grid_columnconfigure(4, minsize=1)

        self.d1_label = tk.Label(self,text="Start date (DD/MM/YYY:")
        self.d1_label.grid(row=0,column=0)

        self.d1_d = tk.Spinbox(self,from_=1,to=31)
        self.d1_d.grid(row=1,column=0)

        self.d1_m = tk.Spinbox(self,from_=1,to=12)
        self.d1_m.grid(row=1,column=1)

        self.d1_y = tk.Spinbox(self,from_=2000,to=2999)
        self.d1_y.grid(row=1,column=2)

        self.d2_label = tk.Label(self,text="End date (DD/MM/YYY:")
        self.d2_label.grid(row=2,column=0)

        self.d2_d = tk.Spinbox(self,from_=1,to=31)
        self.d2_d.grid(row=3,column=0)

        self.d2_m = tk.Spinbox(self,from_=1,to=12)
        self.d2_m.grid(row=3,column=1)

        self.d2_y = tk.Spinbox(self,from_=2000,to=2999)
        self.d2_y.grid(row=3,column=2)

        self.confirmButton = tk.Button(self,text="Add",command=self._onConfirmButtonClick)
        self.confirmButton.grid(row=4,column=1,sticky="nsew")

    def _onConfirmButtonClick(self):
        self.confirm_method(int(self.d1_d.get()),int(self.d1_m.get()),int(self.d1_y.get()),int(self.d2_d.get()),int(self.d2_m.get()),int(self.d2_y.get()))
        self.destroy()

class MyWindow(tk.Toplevel): #Create a window
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.title("This is title Name")

class DebugWindow(tk.Toplevel):
    def __init__(self, root,text) -> None:
        tk.Toplevel.__init__(self, root)
        self.root = root
        self.text = text
        self.UI()

    def UI(self):
        self.geometry("410x300")
        self.title("Debug")
        self.grid_rowconfigure(4, minsize=1)
        self.grid_columnconfigure(4, minsize=1)
        self.title = tk.Text("Debug output", date.ctime())
        self.text = tk.Text(self,self.text)

