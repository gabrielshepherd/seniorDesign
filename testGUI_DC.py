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
        self.create_scrollWheel()

    def create_buttons(self):
        self.resButton = tkinter.Button(self, text="Resistors")
        self.resButton.grid(row=0, column=1, sticky="W"+"E")
        self.capButton = tkinter.Button(self, text="Capacitors")
        self.capButton.grid(row=1,column=1,  sticky="W"+"E")
        self.indButton = tkinter.Button(self, text="Inductors")
        #self.indButton.pack(side="top")
        self.indButton.grid(row=2, column=1, sticky="W"+"E")
        L1 = tkinter.Label(self, text="Part")
        L1.grid( row=0, column=0)
        E1 = tkinter.Entry(self, bd =5)
        E1.grid(row=1, column=0)

    def create_scrollWheel(self):
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        #self.grid_propagate(False)

        #Adding a canvas to contain the Scroll bar
        canvas = tkinter.Canvas(self, bg="yellow")
        canvas.grid(row=0, column=2,rowspan=10,  sticky="news")
        
        scrollbar = tkinter.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.grid( row=0, column=3, rowspan=10, sticky='nes' )
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
        '''
        mylist = tkinter.Listbox(mainPage, yscrollcommand = scrollbar.set )
        for line in range(3):
            mylist.insert("end",components[line])

        mylist.grid( row=0,column=3 )
        scrollbar.config( command = mylist.yview )
       '''


components = ["Resistor", "Capacitor", "Inductor"]

#---------- Start of Main Page ---------------
mainPage = tkinter.Tk()

app = Application(master=mainPage)
app.mainloop()


  