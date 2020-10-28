import tkinter as tkinter
import tkinter.messagebox as messagebox

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        master.geometry('800x400')
        master.title('Parts Inventory Display')
        self.grid_columnconfigure(10)
        self.create_buttons()
        self.create_search()
        self.create_part_ranges()

    def create_buttons(self):
        L1 = tkinter.Label(self, text="Parts", bg="yellow")
        L1.grid( row=0, column=0)
        self.resButton = tkinter.Button(self, text="Resistors", command=lambda: master.switch_frame(Resistors))
        self.resButton.grid(row=1, column=0, sticky="W"+"E" +"N" +"S")
        self.capButton = tkinter.Button(self, text="Capacitors")
        self.capButton.grid(row=2,column=0, sticky="W"+"E" +"N" +"S")
        self.indButton = tkinter.Button(self, text="Inductors")
        #self.indButton.pack(side="top")
        self.indButton.grid(row=3, column=0, sticky="W"+"E" +"N" +"S")

    def create_search(self):
        canvas = tkinter.Canvas(self, bg="Green")
        canvas.grid(row=0, column=2,rowspan=10,  sticky="news")

        L1 = tkinter.Label(canvas, text="Part")
        L1.grid( row=0, column=0)
        E1 = tkinter.Entry(canvas, bd =5)
        E1.grid(row=1, column=0)

    def create_part_ranges(self):
        L1 = tkinter.Label(self, text="Part Ranges", bg="yellow")
        L1.grid( row=0, column=3)
        self.range1 = tkinter.Button(self, text="Range 1")
        self.range1.grid(row=1, column=3, sticky="W"+"E" +"N" +"S")
        self.range2 = tkinter.Button(self, text="Range 2")
        self.range2.grid(row=2,column=3, sticky="W"+"E" +"N" +"S")
        self.range3 = tkinter.Button(self, text="Range 3")
        self.range3.grid(row=3, column=3, sticky="W"+"E" +"N" +"S")



   

components = ["Resistor", "Capacitor", "Inductor"]

#---------- Start of Main Page ---------------
mainPage = tkinter.Tk()

app = Application(master=mainPage)
app.mainloop()


  