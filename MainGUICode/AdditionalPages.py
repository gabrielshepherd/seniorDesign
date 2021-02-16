import tkinter as tkinter
import tkinter.font as tkFont
import MainGUI_WithKeypadEdit as Main

#Global List of what was recently searched
RecentlySearchedName = []
RecentlySearchedFrame = []

class SpecificSearch(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Specified Search", font=('Helvetica', 18, "bold")).grid(row=0)

        e = tkinter.Entry(self).grid(row=1, pady = 10)
        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=3, column=0, sticky="W"+"E")

        self.searchButton = tkinter.Button(self, text = "Search").grid(row=2, pady = 10, sticky="W"+"E")

class RecentSearches(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        count = 0
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg="#F6B022",text="Recent Searches", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(Main.StartPage) )
        self.homeButton.grid(row=12, column=0, sticky="W"+"E")

        for recentFrame in RecentlySearchedFrame:
            b = tkinter.Button(self, text = RecentlySearchedName[count],
                #Switch Main.StartPage with recentFrame to go to part page/Call Code to turn LEDS on
                 command=lambda: master.switch_frame(Main.StartPage)).grid(row=count+1, sticky="W"+"E", pady = 3)
            count = count + 1

class QuickSearch(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")
        tkinter.Label(self, width = 45, borderwidth=2, relief="solid", bg="#F6B022",text="Quick Search", font=('Helvetica', 18, "bold")).grid(row=0, columnspan=3, pady=4)
        L2fontStyle = tkFont.Font(family = "Lucida Grande", size =12)

        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", 
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=1, sticky="W"+"E", pady=4)

        self.Resistors= tkinter.Button(self, text="Resistors", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: [master.switch_frame(Resistors), RecentlySearchedName.append("Resistors"),
                           RecentlySearchedFrame.append(self)])
        self.Resistors.grid(row=1, column=0, pady=4)

        self.Inductors= tkinter.Button(self, text="Inductors", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: [master.switch_frame(Inductors), RecentlySearchedName.append("Inductors"),
                           RecentlySearchedFrame.append(self)])
        self.Inductors.grid(row=2, column=0, pady=4)

        self.Capacitors= tkinter.Button(self, text="Capacitors", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.Capacitors.grid(row=1, column=2, pady=4)

        self.Transistors= tkinter.Button(self, text="Transistors", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.Transistors.grid(row=2, column=2, pady=4)

        self.Pots= tkinter.Button(self, text="Potentiometers", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.Pots.grid(row=3, column=2, pady=4)

        self.OpAmps= tkinter.Button(self, text="Op Amps", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.OpAmps.grid(row=3, column=0, pady=4)

        self.DigitalIC= tkinter.Button(self, text="Digital ICs", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.DigitalIC.grid(row=4, column=2, pady=4)

        self.Filters= tkinter.Button(self, text="Filters", width=20,font = L2fontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.Filters.grid(row=4, column=0, pady=4)



class Resistors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 45, bg="#F6B022",text="Resistors", font=('Helvetica', 18, "bold")).grid(row=0, columnspan=3, pady = 10)
        tkinter.Label(self, text = "Power", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=1, column=0)
        tkinter.Label(self, text = "Tolerance", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=5, column=0)
        tkinter.Label(self, text = "Range", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=1, column=2)
        tkinter.Label(self, text = " ", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=8, column=2, pady = 5)
        tkinter.Label(self, text = " ", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=4, column=2, pady = 5)

        #Contains the variables selected from the radio buttons
        def sel():
            selection = "Selection: " + str(Select.get()) + " in the range " + str(Range.get())
            tkinter.Label(self, text = selection, bg = "white").grid(row = 8, column =1, sticky = "W" + "E", pady = 5)

        def ranges():
            if Select.get() == "High Power":
                Ranges = [".1 - 820", "825 - 390k", "430k - 18M"]
            if Select.get() == "Low Power":
                Ranges = ["1 - 360", "390 - 110k", "120k - 25M"]
            if Select.get() == "1%":
                Ranges = ["150-200k", "   None   ", "   None   "]
            if Select.get() == "5%":
                Ranges = ["4.7 - 62k", "100k - 1M", "   None   "]
            count1=1
            for names in Ranges:
                tkinter.Radiobutton(self, variable = Range, value = names, text = names, bg="white", justify = "right", command=sel).grid(row=count1+1, column=2, sticky = "W" + "E")
                count1 = count1 + 1

        #Initialization of the radio buttons
        Buttons = ["High Power", "Low Power", "1%", "5%"]
        Select = tkinter.StringVar()
        Select.set("Low Power")
        Range = tkinter.StringVar()
        Range.set("Not Seleted")
        count = 1

        #Making Radio buttons
        for names in Buttons:
            if count < 3:
                tkinter.Radiobutton(self, variable = Select, value = names, text = names,bg="white", justify = "right", command=lambda:[sel(), ranges()]).grid(row=count+1, column=0)
            else:
                tkinter.Radiobutton(self, variable = Select, value = names, text = names,bg="white", justify = "right", command=lambda:[sel(), ranges()]).grid(row=count+3, column=0)
            count = count + 1

        self.searchButton = tkinter.Button(self, text="Search", relief = "ridge", width = 30,
            command=lambda: master.switch_frame(Main.StartPage))
        self.searchButton.grid(row=10, column=1, pady = 5)

        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 30,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=11, column=1)


class Inductors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 45, bg="#F6B022",text="Inductors", font=('Helvetica', 18, "bold")).grid(row=0, columnspan=3, pady = 10)
        tkinter.Label(self, text = "Range", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=1, column=1)
        tkinter.Label(self, text = " ", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=8, column=0, pady =5)

        def sel():
            selection = "Selection: " + str(Range.get()) 
            tkinter.Label(self, text = selection, bg = "white").grid(row = 8, column =1, sticky = "W" + "E", pady = 5)

        Ranges = [".22u - 68m", "100m - 1"]
        Range = tkinter.StringVar()
        Range.set("Low Power")
        count = 1
        #Making Radio buttons
        for names in Ranges:
            tkinter.Radiobutton(self, variable = Range, value = names, text = names,bg="white", justify = "right", command=sel).grid(row=count+1, column=1)
            count = count + 1

        self.searchButton = tkinter.Button(self, text="Search", relief = "ridge",width = 30,
            command=lambda: master.switch_frame(Main.StartPage))
        self.searchButton.grid(row=9, column=1, pady = 5)

        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 30,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=1)