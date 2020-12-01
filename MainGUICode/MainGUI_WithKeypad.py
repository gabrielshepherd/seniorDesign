'''
This Program has a base level start to what we may potentially want as the GUI
'''
import tkinter as tkinter
import tkinter.font as tkFont
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
        self._frame.pack()
    
#------------------------------------------------------------------------------------

def code(value, e):

    # inform function to use external/global variable
    global pin

    if value == 'Backspace':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e.delete('0', 'end')
        e.insert('end', pin)

    elif value == 'Enter':
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
        self.create_units()
        self.create_blankspace(1,1)
        self.create_blankspace(1,3)

        L1fontStyle = tkFont.Font(family = "Lucida Grande", size =20)
        L1 = tkinter.Label(self, height=2, text="Parts Inventory Display", bg="yellow", font = L1fontStyle)
        L1.grid( row=0, column=2)
        self.adminButton = tkinter.Button(self, width=15, height=1, text="Admin")
        self.adminButton.grid(row=0, column=4)

        L2fontStyle = tkFont.Font(family = "Lucida Grande", size =15)
        L2 = tkinter.Label(self, width=10, text="Parts", bg="yellow", font = L2fontStyle)
        L2.grid( row=1, column=0)

        #------------------------ Creating buttons -------------------------
        self.resButton = tkinter.Button(self, text="Resistors",width=15,
                           height=2, command=lambda: master.switch_frame(Resistors))
        self.resButton.grid(row=2, column=0, pady=2)

        self.capButton = tkinter.Button(self, width=15, height=2, text="Capacitors")
        self.capButton.grid(row=3,column=0)

        self.indButton = tkinter.Button(self, width=15, height=2, text="Inductors")
        self.indButton.grid(row=4, column=0)

        self.icButton = tkinter.Button(self, width=15, height=2, text="IC Chips")
        self.icButton.grid(row=5, column=0)

        self.tranButton = tkinter.Button(self, width=15, height=2, text="Transistors")
        self.tranButton.grid(row=6, column=0)

        self.otherButton = tkinter.Button(self, width=15, height=2, text="Other")
        self.otherButton.grid(row=7, column=0)
        #-------------------------------------------------------------------
 
    def create_blankspace(self,rowNum,colNum):
        canvas = tkinter.Canvas(self, width=40)
        canvas.grid(row=rowNum, column=colNum,rowspan=10)

    def create_keypad_and_search(self):
        canvas = tkinter.Canvas(self)
        canvas.grid(row=1, column=2,rowspan=10,  sticky="news")
        keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['Backspace', '0', 'Enter'],    
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
                b.grid(row=y, column=x, ipadx=10)

        self.recentsButton = tkinter.Button(canvas, width=25, height=2, text="Recent Searches")
        self.recentsButton.grid(row=6,column=0, columnspan=3, pady=5)


    

    def create_units(self):
        L3fontStyle = tkFont.Font(family = "Lucida Grande", size =15)
        L1 = tkinter.Label(self, width=10, text="Units", bg="yellow", font = L3fontStyle)
        L1.grid( row=1, column=4)
        self.unit1 = tkinter.Button(self, width=15, height=2, text="Nano")
        self.unit1.grid(row=2, column=4, pady=2)
        self.unit2 = tkinter.Button(self, width=15, height=2, text="Micro")
        self.unit2.grid(row=3,column=4, pady=2)
        self.unit3 = tkinter.Button(self,width=15, height=2, text="Mili")
        self.unit3.grid(row=4, column=4, pady=2)
        self.unit4 = tkinter.Button(self,width=15, height=2, text="None")
        self.unit4.grid(row=5, column=4, pady=2)
        self.unit5 = tkinter.Button(self,width=15, height=2, text="Kilo")
        self.unit5.grid(row=6, column=4, pady=2)
        self.unit5 = tkinter.Button(self,width=15, height=2, text="Mega")
        self.unit5.grid(row=7, column=4, pady=2)

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

# create global variable for pin
pin = '' # empty string
app = Application()
app.mainloop()


  