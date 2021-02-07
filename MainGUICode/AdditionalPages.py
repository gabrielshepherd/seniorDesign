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

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=2, column=0, sticky="W"+"E")

class RecentSearches(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        count = 0
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Recent Searches", font=('Helvetica', 18, "bold")).grid(row=0)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(Main.StartPage) )
        self.homeButton.grid(row=12, column=0, sticky="W"+"E")

        for recentFrame in RecentlySearchedFrame:
            b = tkinter.Button(self, text = RecentlySearchedName[count],
                #Switch Main.StartPage with recentFrame to go to part page/Call Code to turn LEDS on
                 command=lambda: master.switch_frame(Main.StartPage)).grid(row=count+1)
            count = count + 1

class QuickSearch(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, width = 35,bg='Green',text="Quick Search", font=('Helvetica', 18, "bold")).grid(row=0, columnspan=3)
        L2fontStyle = tkFont.Font(family = "Lucida Grande", size =10)

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=1, sticky="W"+"E")

        self.Resistors= tkinter.Button(self, text="Resistors", width=20,font = L2fontStyle,
                           height=2, command=lambda: [master.switch_frame(Resistors), RecentlySearchedName.append("Resistors"),
                           RecentlySearchedFrame.append(self)])
        self.Resistors.grid(row=1, column=0, pady=2)
        self.Inductors= tkinter.Button(self, text="Inductors", width=20,font = L2fontStyle,
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.Inductors.grid(row=2, column=0, pady=2)

        self.Capacitors= tkinter.Button(self, text="Capacitors", width=20,font = L2fontStyle,
                           height=2, command=lambda: master.switch_frame(Main.StartPage))
        self.Capacitors.grid(row=1, column=2, pady=2)



class Resistors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, bg='Green',text="Resistors", font=('Helvetica', 18, "bold")).grid(row=0)

        buttons = ["High Power",
                    "Low Power"]
        count = 1
        for names in buttons:
            self.test = tkinter.Radiobutton(self, text = names)
            self.test.grid(row=count, column=0)
            count = count +1
        

        self.homeButton = tkinter.Button(self, text="Home",
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, sticky="W"+"E")