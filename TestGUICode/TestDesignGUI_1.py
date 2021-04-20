'''
This Program has a base level start to what we may potentially want as the GUI
'''
import tkinter as tkinter
import tkinter.messagebox as messagebox

#-----------------------------Startup and Initialization----------------------------
class Application(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
#------------------------------------------------------------------------------------

#---------------------------------Start Page-----------------------------------------
class StartPage(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # Edit this value once we test on actual display
        master.geometry('800x400')
        master.title('Parts Inventory Display')
        self.create_search()
        self.create_part_ranges()

        L1 = tkinter.Label(self, text="Parts", bg="yellow")
        L1.grid( row=0, column=0)

        #------------------------ Creating buttons -------------------------
        self.resButton = tkinter.Button(self, text="Resistors",width=15,
                           height=1, command=lambda: master.switch_frame(Resistors))
        self.resButton.grid(row=1, column=0, sticky="W"+"E" +"N" +"S")
        self.capButton = tkinter.Button(self, text="Capacitors")
        self.capButton.grid(row=2,column=0, sticky="W"+"E" +"N" +"S")
        self.indButton = tkinter.Button(self, text="Inductors")
        self.indButton.grid(row=3, column=0, sticky="W"+"E" +"N" +"S")
        #-------------------------------------------------------------------


    def create_search(self):
        canvas = tkinter.Canvas(self, bg="Green")
        canvas.grid(row=0, column=1,rowspan=10,  sticky="news")

        L1 = tkinter.Label(canvas, text="Part")
        L1.grid( row=0, column=0)
        E1 = tkinter.Entry(canvas, bd =5)
        E1.grid(row=1, column=0)

    def create_part_ranges(self):
        L1 = tkinter.Label(self, text="Part Ranges", bg="yellow")
        L1.grid( row=0, column=2)
        self.range1 = tkinter.Button(self, text="Range 1")
        self.range1.grid(row=1, column=2, sticky="W"+"E" +"N" +"S")
        self.range2 = tkinter.Button(self, text="Range 2")
        self.range2.grid(row=2,column=2, sticky="W"+"E" +"N" +"S")
        self.range3 = tkinter.Button(self, text="Range 3")
        self.range3.grid(row=3, column=2, sticky="W"+"E" +"N" +"S")

#------------------------------------------------------------------------------------

class Resistors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Resistors", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")



#---------- Start of Main Function---------------


app = Application()
app.mainloop()


  