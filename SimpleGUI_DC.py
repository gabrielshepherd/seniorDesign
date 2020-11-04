'''
This Program has 3 buttons on the home page, which all lead to 3 seperate pages.
'''
import tkinter as tkinter
import tkinter.messagebox as messagebox

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
        self._frame.pack()


class StartPage(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self,master)
        super().__init__(master)
        self.master = master
        self.pack()
        self.grid_columnconfigure(10)
        #self.create_buttons()

    # By making this a seperate function, "master" loses its value
    #def create_buttons(self):
       # tkinter.Frame.__init__(self,master)
        self.resButton = tkinter.Button(self, text="Resistors",
            command=lambda: master.switch_frame(Resistors))
        self.resButton.grid(row=0, column=0, sticky="W"+"E")
        self.capButton = tkinter.Button(self, text="Capacitors",
            command=lambda: master.switch_frame(Capacitors))
        self.capButton.grid(row=1,column=0,  sticky="W"+"E")
        self.indButton = tkinter.Button(self, text="Inductors",
            command=lambda: master.switch_frame(Inductors))
        #self.indButton.pack(side="top")
        self.indButton.grid(row=2, column=0, sticky="W"+"E")
        L1 = tkinter.Label(self, text="Part Search")
        L1.grid( row=3, column=0)
        E1 = tkinter.Entry(self, bd =5)
        E1.grid(row=4, column=0)

class Resistors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Resistors", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")

class Capacitors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Capacitors", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")

class Inductors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Inductors", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")
        self.create_scrollWheel()

    def create_scrollWheel(self):
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        #self.grid_propagate(False)

        #Adding a canvas to contain the Scroll bar
        canvas = tkinter.Canvas(self, bg="yellow")
        canvas.grid(row=1, rowspan=10,  sticky="news")
        
        scrollbar = tkinter.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.grid( row=0, column=1, rowspan=10, sticky='nes' )
        canvas.configure(yscrollcommand=scrollbar.set)

        #Create a frame to contain the canvas
        frame_Data = tkinter.Frame(canvas)
        canvas.create_window((0,0), window=frame_Data, anchor='nw')

        # Add 9-by-5 buttons to the frame
        rows = 20
        columns = 2
        buttons = [[tkinter.Button() for j in range(columns)] for i in range(rows)]
        for i in range(0, rows):
            for j in range(0, columns):
                buttons[i][j] = tkinter.Button(frame_Data, text="Range:" +("%d,%d" % (i+1, j+1)))
                buttons[i][j].grid(row=i, column=j, sticky='news')

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_Data.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 2)])
        first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 2)])
        frame_Data.config(width=first5columns_width + scrollbar.winfo_width(),
                                height=first5rows_height)


        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))

#---------- Start of Main Page ---------------


app = Application()
app.geometry('800x400')
app.title('Parts Inventory Display')
app.mainloop()