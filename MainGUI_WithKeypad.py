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

def code(value, e):

    # inform function to use external/global variable
    global pin

    if value == '*':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e.delete('0', 'end')
        e.insert('end', pin)

    elif value == '#':
        # check pin

        if pin == "3529":
            print("PIN OK")
        else:
            print("PIN ERROR!", pin)
            # clear `pin`
            pin = ''
            # clear `entry`
            e.delete('0', 'end')

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e.insert('end', value)

    print("Current:", pin)

#---------------------------------Start Page-----------------------------------------
class StartPage(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # Edit this value once we test on actual display
        master.geometry('800x400')
        master.title('Parts Inventory Display')
        self.create_keypad_and_search()
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
 

    def create_keypad_and_search(self):
        canvas = tkinter.Canvas(self, bg="Green")
        canvas.grid(row=0, column=1,rowspan=10,  sticky="news")
        keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['*', '9', '#'],    
        ]
    

        # place to display pin
        e = tkinter.Entry(canvas)
        e.grid(row=0, column=0, columnspan=3, ipady=5)

        # create buttons using `keys`
        for y, row in enumerate(keys, 1):
            for x, key in enumerate(row):
                # `lambda` inside `for` has to use `val=key:code(val)` 
                # instead of direct `code(key)`
                b = tkinter.Button(canvas, text=key, width = 10, height =3, command=lambda val=key:code(val, e))
                b.grid(row=y, column=x)


    

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




#---------- Start of Main Function---------------

# create global variable for pin
pin = '' # empty string
app = Application()
app.mainloop()


  