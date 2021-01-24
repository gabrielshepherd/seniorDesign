'''
This Program has a base level start to what we may potentially want as the GUI
'''
import tkinter as tkinter
import tkinter.font as tkFont
import tkinter.messagebox as messagebox
#root.iconbitmap('c:/ndsuicon.ico')

#-----------------------------Startup and Initialization----------------------------
class Application(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self._frame = None
        self.iconphoto
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    
#------------------------Code to Make the Keypad work---------------------------------

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

        if pin == "0000":
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
    
        self.create_greenspace(1,0)
        self.create_greenspace(1,2)

        #Making the Title and the admin button
        L1fontStyle = tkFont.Font(family = "Lucida Grande", size =20)
        L1 = tkinter.Label(self, height=2, text="Parts Inventory Display", bg="yellow", font = L1fontStyle)
        L1.grid( row=0, column=1)
        self.adminButton = tkinter.Button(self, width=15, height=1, text="Admin",
                                        command=lambda: master.switch_frame(Admin))
        self.adminButton.grid(row=5, column=1)

        L2fontStyle = tkFont.Font(family = "Lucida Grande", size =15)
        L2 = tkinter.Label(self, width=10, text="--------", bg="yellow", font = L2fontStyle)
        L2.grid( row=1, column=1)

        #------------------------ Creating buttons -------------------------
        self.QuickSearch = tkinter.Button(self, text="Quick Search",width=15,
                           height=2, command=lambda: master.switch_frame(QuickSearch))
        self.QuickSearch.grid(row=2, column=1, pady=2)

        self.capButton = tkinter.Button(self, width=15, height=2, text="Specified Search",
                                        command=lambda: master.switch_frame(SpecificSearch))
        self.capButton.grid(row=3,column=1, pady=2)

        

        self.otherButton = tkinter.Button(self, width=15, height=2, text="Recent Searches",
                                        command=lambda: master.switch_frame(RecentSearches))
        self.otherButton.grid(row=4, column=1, pady=2)



        #-------------------------------------------------------------------
 
    def create_blankspace(self,rowNum,colNum):
        canvas = tkinter.Canvas(self, width=40, bg="green")
        canvas.grid(row=rowNum, column=colNum,rowspan=10)

    #will be picture in future
    def create_greenspace(self,rowNum,colNum):
        canvas = tkinter.Canvas(self, width=100, bg="green")
        
        canvas.grid(row=rowNum, column=colNum,rowspan=10)



#------------------------------------------------------------------------------------

class QuickSearch(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Quick Search", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")


class SpecificSearch(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Specified Search", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")


class RecentSearches(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Recent Searches", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")
        


class Admin(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Admin", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=20, column=0, sticky="W"+"E", pady=4)
        self.create_keypad_and_search()

    def create_keypad_and_search(self):
        canvas = tkinter.Canvas(self)
        canvas.grid(row=1, column=0,rowspan=10,  sticky="news",pady=4)
        keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['Backspace', '0', 'Enter'],    
        ]

        # place to display search value
        e = tkinter.Entry(canvas)
        e.grid(row=0, column=0, columnspan=3, ipady=5)

        # create buttons using `keys`
        for y, row in enumerate(keys, 1):
            for x, key in enumerate(row):
                # `lambda` inside `for` has to use `val=key:code(val)` 
                # instead of direct `code(key)`
                b = tkinter.Button(canvas, text=key, width = 10, height =3, command=lambda val=key:code(val, e))
                b.grid(row=y, column=x, ipadx=10)

#---------- Start of Main Function---------------

# create global variable for pin
pin = '' # empty string
app = Application()

app.mainloop()


  