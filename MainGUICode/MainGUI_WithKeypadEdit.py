'''
This Program has a base level start to what we may potentially want as the GUI
'''
import tkinter as tkinter
import tkinter.font as tkFont
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
import AdditionalPages as AddP

#img = ImageTk.PhotoImage(Image.open("NDSU_Logo.png"))
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
    

#---------------------------------Start Page-----------------------------------------
class StartPage(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.configure(bg = "white")
        master.configure(bg = "white")
        # Edit this value once we test on actual display
        master.geometry('800x350') #1024x600 is size, I tested with 800x350
        master.title('Parts Inventory Display')
    
        self.create_greenspace(1,0)
        self.create_greenspace(1,2)
        
        #--------Making Images-------------------
        img1 = Image.open(r"C:\NDSU_Logo2.png")
        img1 = img1.resize((100,50), Image.ANTIALIAS)
        Logo1 = ImageTk.PhotoImage(img1)
        Logo1_label = tkinter.Label(self,image=Logo1, bg="white")
        Logo1_label.image = Logo1
        Logo1_label.place(x=0, y =10)

        img2 = Image.open(r"C:\NDSU_Logo.png")
        img2 = img2.resize((100,50), Image.ANTIALIAS)
        Logo2 = ImageTk.PhotoImage(img2)
        Logo2_label = tkinter.Label(self,image=Logo2, bg="white")
        Logo2_label.image = Logo2
        Logo2_label.place(x=670, y =10)
        
 
        #Making the Title and the admin button
        L1fontStyle = tkFont.Font(family = "Lucida Grande", size =20)
        L1 = tkinter.Label(self, height=2, width= 35, text="Parts Inventory Display", bg="#F6B022", font = L1fontStyle )
        L1.grid( row=0, column=1)
        self.adminButton = tkinter.Button(self, width=15, height=1, text="Admin",relief = "ridge",
                                        command=lambda: master.switch_frame(Admin))
        self.adminButton.grid(row=5, column=1)

        L2fontStyle = tkFont.Font(family = "Lucida Grande", size =15)
        L2 = tkinter.Label(self, width=80, bg = "#F6B022")
        L2.grid( row=8, columnspan = 3)

        #------------------------ Creating buttons -------------------------
        self.QuickSearch = tkinter.Button(self, text="Quick Search", font = L2fontStyle,  width=20, relief = "ridge", #bg = "#202124",
                           height=2, command=lambda: master.switch_frame(AddP.QuickSearch))
        self.QuickSearch.grid(row=2, column=1, pady=2)

        self.SpecifiedSearch = tkinter.Button(self, width=20, height=2, text="Specified Search",font = L2fontStyle,relief = "ridge",
                                        command=lambda: master.switch_frame(AddP.SpecificSearch))
        self.SpecifiedSearch.grid(row=3,column=1, pady=2)

        self.RecentButton = tkinter.Button(self, width=20, height=2, text="Recent Searches",font = L2fontStyle,relief = "ridge",
                                        command=lambda: master.switch_frame(AddP.RecentSearches))
        self.RecentButton.grid(row=4, column=1, pady=2)

        #-------------------------------------------------------------------
 
    def create_blankspace(self,rowNum,colNum):
        canvas = tkinter.Canvas(self, width=40, bg="green")
        canvas.grid(row=rowNum, column=colNum,rowspan=10)

    #will be picture in future
    def create_greenspace(self,rowNum,colNum):
        canvas = tkinter.Canvas(self, width=100, bg="#0A5640")
        canvas.grid(row=rowNum, column=colNum,rowspan=10)

#------------------------------------------------------------------------------------

class Admin(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")
        tkinter.Label(self, width = 45, borderwidth=2, relief="solid", bg="#F6B022",text="Admin", font=('Helvetica', 18, "bold")).grid(row=0, columnspan=3, pady=4)

        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=20, column=1, sticky="W"+"E", pady=4)
        self.create_keypad_and_search(self.master)

    def create_keypad_and_search(self, master):
        canvas = tkinter.Canvas(self, bg = "white", bd=0, highlightthickness=0, relief='ridge')
        canvas.grid(row=1, column=1,rowspan = 10,pady=4)
        keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['Backspace', '0', 'Enter'],    
        ]

        # place to display search value
        e = tkinter.Entry(canvas, relief = "solid")
        e.grid(row=0, column=0, columnspan = 3,  ipady=5, pady = 5)

        # create buttons using `keys`
        for y, row in enumerate(keys, 1):
            for x, key in enumerate(row):
                # `lambda` inside `for` has to use `val=key:code(val)` 
                # instead of direct `code(key)`
                b = tkinter.Button(canvas, text=key, relief = "ridge", width = 10, height =3, command=lambda val=key:self.code(master, val, e))
                b.grid(row=y, column=x, ipadx=10)
    
    #------------------------Code to Make the Keypad work---------------------------------

    def code(self,master,value, e):

        # inform function to use external/global variable
        global pin, check

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
                master.switch_frame(AdminONLY)
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

class AdminONLY(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")
        tkinter.Label(self, width = 45, borderwidth=2, relief="solid", bg="#F6B022",text="Admin ONLY", font=('Helvetica', 18, "bold")).grid(row=0, columnspan=3, pady=4)

        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge",
            command=lambda: master.switch_frame(StartPage))
        self.homeButton.grid(row=2, column=1, sticky="W"+"E")

        L1 = tkinter.Label(self,text = "You are Admin", bg = "white")
        L1.grid(row=1, column = 1)

#---------- Start of Main Function---------------

# create global variable for pin
pin = '' # empty string
app = Application()

app.mainloop()


  