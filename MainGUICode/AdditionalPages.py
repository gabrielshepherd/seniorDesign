# Parts Inventory Display
# Design III
#
# This file contains the additional pages used in the GUI for the Parts Inventory Display Team.
# All of the contents are for the Quick Search, Specific Search, and Recently Searched.
#
# Author: Dylan Carlson



# ----- Imports -----
# Both needed to use tkinter
import tkinter as tkinter
import tkinter.font as tkFont
from tkinter import messagebox
# Using the main file that has the main structure of the GUI.
import StartingPages as Main
# Needed for parsing excel spreadsheet
import excel as spreadsheet
# For sending data to other pi
import send as output

#Need to install this on Pi
#from PIL import ImageTk, Image

# This is needed for the Recently searched page. The first list contains what the button face will
# say, and the second will contain the location of the LEDS for what was searched.
RecentlySearchedName = [None, None, None, None, None, None, None]
RecentlySearchedLEDLocation = [None, None, None, None, None, None, None]
RecentlySearched = []
# Function for adding to list:
# addButtonToList("<Name you want to appear on button>", "<insert location of LEDS here>")
def addButtonToList(name, location):
    if name not in RecentlySearchedName:
        # This keeps the length of the list at 7
        if len(RecentlySearchedName) == 7:
            #RecentlySearched.pop()
            RecentlySearchedLEDLocation.pop()
            RecentlySearchedName.pop()
        #RecentlySearched.insert(0, [name, location])
        RecentlySearchedName.insert(0, name)
        RecentlySearchedLEDLocation.insert(0, location)

#------Main 3 pages--------
class SpecificSearch(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")
        tkinter.Label(self, width = 50, borderwidth=2, relief="solid", bg="#F6B022",text="Specified Search", font=('Helvetica', 25, "bold")).grid(row=0, columnspan=3, pady=4)
     
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)
        self.L1 = tkinter.Label(self, text = "Enter part here:", bg = "white", font=('Helvetica', 18)).grid(row = 1, column = 1, pady = 10)

        value = tkinter.StringVar()
        e = tkinter.Entry(self, width=40, relief="solid", textvariable=value).grid(row=2, column =1, pady = 40, ipady = 10)

        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 30, height=3,
            font = MainFontStyle, command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=4, column=1, pady = 40, sticky="W"+"E")

        self.searchButton = tkinter.Button(self, text = "Search", relief = "ridge",width = 30, height=3,
            font = MainFontStyle, command=lambda: [print(value.get()) , spreadsheet.search(value.get()), searchButton_Click()])
        self.searchButton.grid(row=3, column = 1, pady = 40, sticky="W"+"E")

        def searchButton_Click():
            returnedString = spreadsheet.search(value.get())
            #If the item is not found, excel.py will return BAD.
            #So if the string is bad, don't add it to recently searched.
            if returnedString != "BAD":
                addButtonToList(value.get(), returnedString)
        
        #---These lines are for the NDSU Logo at bottom-----
        #img2 = Image.open(r"C:\NDSU_Logo2.png")
        #img2 = img2.resize((300,50), Image.ANTIALIAS)
        #Logo2 = ImageTk.PhotoImage(img2)
        #Logo2_label = tkinter.Label(self,image=Logo2, bg="white")
        #Logo2_label.image = Logo2
        #Logo2_label.grid(row=5, column = 1, pady = 30)
        #--------------------------------------------------
        
        #Logo2_label.place(x=100, y =10)
#Future addition - Have the sender also send the leds to light up. Change the button to light up leds insead
class RecentSearches(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        count = 0
        global RecentlySearchedLEDLocation
        global RecentlySearchedName
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg='')
        tkinter.Label(self, width = 50, borderwidth=2, relief="solid", bg="#F6B022",text="Recent Searches", font=('Helvetica', 25, "bold")).grid(row=0, columnspan=3)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)
        
        buttons = [None, None, None, None, None, None, None]
        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", font=MainFontStyle,
            width = 30, height=2, command=lambda: master.switch_frame(Main.StartPage) )
        self.homeButton.grid(row=13, column=1, sticky="W"+"E")

        self.resetButton = tkinter.Button(self, text="Reset", relief = "ridge", font=MainFontStyle,
            width = 30, height=2,command=lambda: [RecentlySearchedName.clear(), RecentlySearchedLEDLocation.clear()] )
        self.resetButton.grid(row=12, column=1, pady = 10, sticky="W"+"E")

        #for recent in RecentlySearched:
        #    b = tkinter.Button(self, text = recent[0], relief = "ridge", font = MainFontStyle,
        #        #Switch Main.StartPage with recentFrame to go to part page/Call Code to turn LEDS on
        #         command=lambda: output.data_transmit(recent[1])).grid(row=count+1, column = 1, sticky="W"+"E", pady = 3)
        #    print(recent[0])
        #   print(recent[1]])
        #    count = count + 1

        #For some reason this does not work with a loop
        try:
            b1 = tkinter.Button(self, text = RecentlySearchedName[0], relief = "ridge", font = MainFontStyle,
            command=lambda: output.data_transmit(RecentlySearchedLEDLocation[0])).grid(row=1, column = 1, sticky="W"+"E", pady = 3)
            b2 = tkinter.Button(self, text = RecentlySearchedName[1], relief = "ridge", font = MainFontStyle,
            command=lambda: output.data_transmit(RecentlySearchedLEDLocation[1])).grid(row=2, column = 1, sticky="W"+"E", pady = 3)
            b3 = tkinter.Button(self, text = RecentlySearchedName[2], relief = "ridge", font = MainFontStyle,
            command=lambda: output.data_transmit(RecentlySearchedLEDLocation[2])).grid(row=3, column = 1, sticky="W"+"E", pady = 3)
            b4 = tkinter.Button(self, text = RecentlySearchedName[3], relief = "ridge", font = MainFontStyle,
            command=lambda: output.data_transmit(RecentlySearchedLEDLocation[3])).grid(row=4, column = 1, sticky="W"+"E", pady = 3)
            b5 = tkinter.Button(self, text = RecentlySearchedName[4], relief = "ridge", font = MainFontStyle,
            command=lambda: output.data_transmit(RecentlySearchedLEDLocation[4])).grid(row=5, column = 1, sticky="W"+"E", pady = 3)
            b6 = tkinter.Button(self, text = RecentlySearchedName[5], relief = "ridge", font = MainFontStyle,
            command=lambda: output.data_transmit(RecentlySearchedLEDLocation[5])).grid(row=6, column = 1, sticky="W"+"E", pady = 3)
            b7 = tkinter.Button(self, text = RecentlySearchedName[6], relief = "ridge", font = MainFontStyle,
            command=lambda: output.data_transmit(RecentlySearchedLEDLocation[6])).grid(row=7, column = 1, sticky="W"+"E", pady = 3)
        except:
            messagebox.showerror("Error", "Item not found")

        #for count in range(len(RecentlySearchedName)):
        #    buttons[count] = tkinter.Button(self, text = RecentlySearchedName[count], relief = "ridge", font = MainFontStyle,
        #                    command=lambda: output.data_transmit(RecentlySearchedLEDLocation[count])).grid(row=count+1, column = 1, sticky="W"+"E", pady = 3)
        #    print(RecentlySearchedName[count])
        #   print(RecentlySearchedLEDLocation[count])
            
class QuickSearch(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")
        tkinter.Label(self, width = 50, borderwidth=2, relief="solid", bg="#F6B022",text="Quick Search", font=('Helvetica', 25, "bold")).grid(row=0, columnspan=2, pady=4)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)


        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 30, height=2,
                font = MainFontStyle,command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, pady=4, columnspan=2)

        self.Resistors= tkinter.Button(self, text="Resistors", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [master.switch_frame(Resistors), output.data_transmit("resistors")])
        self.Resistors.grid(row=1, column=0, pady=4)

        self.Inductors= tkinter.Button(self, text="Inductors", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [master.switch_frame(Inductors), output.data_transmit("inductors")])
        self.Inductors.grid(row=2, column=0, pady=4)

        self.OpAmps= tkinter.Button(self, text="Op Amps", width=30,font = MainFontStyle,relief = "ridge", 
                            height=2, command=lambda: [save(self.OpAmps, 0), output.data_transmit("opamps"),
                            addButtonToList("Op Amps", "opamps")])
        self.OpAmps.grid(row=3, column=0, pady=4)

        self.Diodes= tkinter.Button(self, text="Diodes", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Diodes, 1),output.data_transmit("diodes"),
                           addButtonToList("Diodes", "diodes")])
        self.Diodes.grid(row=4, column=0, pady=4)

        self.VoltageReg= tkinter.Button(self, text="Voltage Regulators", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.VoltageReg, 2),output.data_transmit("voltreg"),
                           addButtonToList("Voltage Regulators", "voltreg")])
        self.VoltageReg.grid(row=5, column=0, pady=4)

        self.Capacitors= tkinter.Button(self, text="Capacitors", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [master.switch_frame(Capacitors), output.data_transmit("capacitors")])
        self.Capacitors.grid(row=1, column=1, pady=4)

        #May need to break this down more
        self.Transistors= tkinter.Button(self, text="Transistors", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Transistors, 3), output.data_transmit("transistors"),
                           addButtonToList("Transistors", "transistors")])
        self.Transistors.grid(row=2, column=1, pady=4)

        self.Pots= tkinter.Button(self, text="Potentiometers", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Pots, 4), output.data_transmit("B31"),
                           addButtonToList("Potentiometers", "B31")])
        self.Pots.grid(row=3, column=1, pady=4)

        self.Logic= tkinter.Button(self, text="Logic", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(LogicComponents) )
        self.Logic.grid(row=4, column=1, pady=4)

        self.Other= tkinter.Button(self, text="Other", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: master.switch_frame(OtherComponents))
        self.Other.grid(row=5, column=1, pady=4)


        #This list keeps track of which button is pressed
        pressed = [False, False, False, False, False]
        Buttons = [self.OpAmps, self.Diodes, self.VoltageReg, self.Transistors, self.Pots]
        orig_color = self.homeButton.cget("background")
        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(4):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

#Only pages related to quick search below
class Resistors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 50, bg="#F6B022",text="Resistors", relief = "solid", font=('Helvetica', 25, "bold")).grid(row=0, columnspan=2, pady = 20)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)

        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=1, pady=20)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=10, column=0, pady=20)

        self.Quarter= tkinter.Button(self, text="1/4 Watt", width=30,font = MainFontStyle,relief = "ridge", 
                        height=2, command=lambda: [master.switch_frame(QuarterWResistors), output.data_transmit("quarterwatt")])
        self.Quarter.grid(row=1, column=0, pady=20)

        self.Half= tkinter.Button(self, text="1/2 Watt", width=30,font = MainFontStyle,relief = "ridge", 
                        height=2, command=lambda: [save(self.Half, 0), RecentlySearchedName.append("1/2 Watt"),
                        RecentlySearchedLEDLocation.append("A41") ,output.data_transmit("A41")])
        self.Half.grid(row=1, column=1, pady=20, padx = 4)
        
        self.OneW= tkinter.Button(self, text="1 Watt", width=30,font = MainFontStyle,relief = "ridge", 
                            height=2, command=lambda: [save(self.OneW, 1), RecentlySearchedName.append("1 Watt Resistors"),
                            RecentlySearchedLEDLocation.append("A42") ,output.data_transmit("A42")])
        self.OneW.grid(row=2, column=0, pady=20, padx = 4)

        self.TwoW = tkinter.Button(self, text="2 Watt", width=30,font = MainFontStyle,relief = "ridge", 
                        height=2, command=lambda: [save(self.TwoW, 2), RecentlySearchedName.append("2 Watt"),
                        RecentlySearchedLEDLocation.append("A43"),output.data_transmit("A43")])
        self.TwoW.grid(row=2, column=1, pady=20, padx = 4)

            #Going to Bulk Resistors page with 3 Buttons
        self.Bulk= tkinter.Button(self, text="Bulk", width=30,font = MainFontStyle,relief = "ridge", 
                        height=2, command=lambda: [master.switch_frame(BulkResistors), output.data_transmit("bulk")])
        self.Bulk.grid(row=3, column=0, pady=20, columnspan=2)


       #This list keeps track of which button is pressed
        pressed = [False, False, False]
        Buttons = [self.Half, self.OneW, self.TwoW]
        orig_color = self.homeButton.cget("background")

        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(2):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

class QuarterWResistors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 50, bg="#F6B022",text="1/4 Watt Resistors", relief = "solid", font=('Helvetica', 25, "bold")).grid(row=0, pady = 20)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)


        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, pady=10)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Resistors))
        self.backButton.grid(row=9, column=0, pady=10)

        self.Range1= tkinter.Button(self, text="1Ω - 360Ω", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range1, 0), addButtonToList("1Ω - 360Ω Resistors", "A31"), output.data_transmit("A31")])
        self.Range1.grid(row=1, column=0, pady=10)

        self.Range2= tkinter.Button(self, text="390Ω - 110kΩ", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range2, 1), addButtonToList("390Ω - 110kΩ Resistors", "A32"), output.data_transmit("A32")])
        self.Range2.grid(row=2, column=0, pady=10, padx = 4)

        self.Range3= tkinter.Button(self, text="120kΩ - 25MΩ", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range3, 2), addButtonToList("120kΩ - 25MΩ Resistors", "A33"), output.data_transmit("A33")])
        self.Range3.grid(row=3, column=0, pady=10, padx = 4)

        #This list keeps track of which button is pressed
        pressed = [False, False, False]
        Buttons = [self.Range1, self.Range2, self.Range3]
        orig_color = self.homeButton.cget("background")
        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(2):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

class BulkResistors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 50, bg="#F6B022",text="Bulk Resistors", relief = "solid", font=('Helvetica', 25, "bold")).grid(row=0, pady = 20)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)


        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, pady=10)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Resistors))
        self.backButton.grid(row=9, column=0, pady=10)

        self.Range1= tkinter.Button(self, text="150Ω - 200kΩ, 1% Tolerance", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range1, 0),
                           addButtonToList("150Ω - 200kΩ, 1% Tolerance Resistors", "B41"), output.data_transmit("B41")])
        self.Range1.grid(row=1, column=0, pady=10)

        self.Range2= tkinter.Button(self, text="100kΩ - 1MΩ+, 5% Tolerance", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range2, 1), 
                           addButtonToList("100kΩ - 1MΩ+, 5% Tolerance Resistors", "B42"), output.data_transmit("B42")])
        self.Range2.grid(row=2, column=0, pady=10, padx = 4)

        self.Range3= tkinter.Button(self, text="4.7Ω - 62kΩ, 5% Tolerance", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range3, 2),
                           addButtonToList("4.7Ω - 62kΩ, 5% Tolerance Resistors", "C41"), output.data_transmit("C41")])
        self.Range3.grid(row=3, column=0, pady=10, padx = 4)


        #This list keeps track of which button is pressed
        pressed = [False, False, False]
        Buttons = [self.Range1, self.Range2, self.Range3]
        orig_color = self.homeButton.cget("background")
        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(2):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

class Inductors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 50, bg="#F6B022",text="Inductors", relief = "solid", font=('Helvetica', 25, "bold")).grid(row=0, pady = 20)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =15)


        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, pady=10)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=9, column=0, pady=10)

        self.Range1= tkinter.Button(self, text=".22uH - 68mH", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range1, 0),
                           addButtonToList(".22uH - 68mH, Inductors", "C32"), output.data_transmit("C32")])
        self.Range1.grid(row=1, column=0, pady=10)

        self.Range2= tkinter.Button(self, text="100mH - 1H", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range2, 1), 
                           addButtonToList("100mH - 1H, Inductors", "C33"), output.data_transmit("C33")])
        self.Range2.grid(row=2, column=0, pady=10, padx = 4)


        #This list keeps track of which button is pressed
        pressed = [False, False, False]
        Buttons = [self.Range1, self.Range2]
        orig_color = self.homeButton.cget("background")
        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(1):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

class Capacitors(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 50, bg="#F6B022",text="Capacitors", relief = "solid", font=('Helvetica', 25, "bold")).grid(row=0, pady = 20)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)


        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, pady=10)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=9, column=0, pady=10)

        self.Range1= tkinter.Button(self, text=".5pF - 470pF", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range1, 0),
                           addButtonToList(".5pF - 470pF, Capacitors", "B32"), output.data_transmit("B32")])
        self.Range1.grid(row=1, column=0, pady=10)

        self.Range2= tkinter.Button(self, text="500pF - 4.7uF", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range2, 1),
                           addButtonToList("500pF - 4.7uF, Capacitors", "B33"), output.data_transmit("B33")])
        self.Range2.grid(row=2, column=0, pady=10, padx = 4)

        self.Range3= tkinter.Button(self, text="6.8uF - 3300uF", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Range3, 2),
                           addButtonToList(".5pF - 470pF, Capacitors", "C31"), output.data_transmit("C31")])
        self.Range3.grid(row=3, column=0, pady=10, padx = 4)

        #This list keeps track of which button is pressed
        pressed = [False, False, False]
        Buttons = [self.Range1, self.Range2, self.Range3]
        orig_color = self.homeButton.cget("background")
        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(2):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

class LogicComponents(tkinter.Frame):

    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 50, bg="#F6B022",text="Logic", relief = "solid", font=('Helvetica', 25, "bold")).grid(row=0, pady = 20)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)


        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, pady=10)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=9, column=0, pady=10)

        self.CMOSLogic= tkinter.Button(self, text="CMOS Logic", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.CMOSLogic, 0),
                           addButtonToList("CMOS Logic", "A22"), output.data_transmit("A22")])
        self.CMOSLogic.grid(row=1, column=0, pady=10)

        self.TTLLogic= tkinter.Button(self, text="TTL Logic", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.TTLLogic, 1),
                           addButtonToList("TTL Logic", "ttl"), output.data_transmit("ttl")])
        self.TTLLogic.grid(row=2, column=0, pady=10, padx = 4)

        self.Multiplexors= tkinter.Button(self, text="Multiplexors", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Multiplexors, 2),
                           addButtonToList("Multiplexors", "B21"), output.data_transmit("B21")])
        self.Multiplexors.grid(row=3, column=0, pady=10, padx = 4)


        #This list keeps track of which button is pressed
        pressed = [False, False, False]
        Buttons = [self.CMOSLogic, self.TTLLogic, self.Multiplexors]
        orig_color = self.homeButton.cget("background")
        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(2):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

class OtherComponents(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 50, bg="#F6B022",text="Other Components", relief = "solid", font=('Helvetica', 25, "bold")).grid(row=0, pady = 20)
        MainFontStyle = tkFont.Font(family = "Helvetica", size =18)


        self.homeButton = tkinter.Button(self, text="Home", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(Main.StartPage))
        self.homeButton.grid(row=10, column=0, pady=10)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 20, height=2, font = MainFontStyle,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=9, column=0, pady=10)

        self.Crystals= tkinter.Button(self, text="Crystals", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Crystals, 0),
                           addButtonToList("Crystals", "C12"), output.data_transmit("C12")])
        self.Crystals.grid(row=1, column=0, pady=10)

        self.Micros= tkinter.Button(self, text="Microcontrollers", width=30,font = MainFontStyle,relief = "ridge", 
                           height=2, command=lambda: [save(self.Micros, 1), 
                           addButtonToList("Microcontrollers", "C13"), output.data_transmit("C13")])
        self.Micros.grid(row=2, column=0, pady=10, padx = 4)

        #This list keeps track of which button is pressed
        pressed = [False, False]
        Buttons = [self.Crystals, self.Micros]
        orig_color = self.homeButton.cget("background")
        #This function is used to make the button green when pressed.
        def save(button, buttonNum):
            if pressed[buttonNum] == False:
                button.config(relief="sunken", bg = "green")
                pressed[buttonNum] = True
                #Set all other buttons to off / unpressed
                for x in range(1):
                    if x != buttonNum:
                        Buttons[x].config(relief="ridge", bg = orig_color)
            else:
                button.config(relief="ridge", bg = orig_color)
                pressed[buttonNum] = False

#Old Code -- It had a lot of good methods to have push buttons update others in the same frame.
class ResistorsOLD(tkinter.Frame):
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


        #The search button needs search the value of what is requested and get the location, and then send out the location to LED code
        self.searchButton = tkinter.Button(self, text="Search", relief = "ridge", width = 30,
            command=lambda: master.switch_frame(Main.StartPage))
        self.searchButton.grid(row=10, column=1, pady = 5)

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 30,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=11, column=1)

class InductorsOLD(tkinter.Frame):
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

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 30,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=10, column=1)

class CapacitorsOLD(tkinter.Frame):
    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        tkinter.Frame.configure(self,bg="white")

        #Setting Up Labels
        tkinter.Label(self, width = 45, bg="#F6B022",text="Capacitors", font=('Helvetica', 18, "bold")).grid(row=0, columnspan=3, pady = 10)
        tkinter.Label(self, text = "Range", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=1, column=1)
        tkinter.Label(self, text = " ", bg = "white", font =('Helvetica', 12, "bold") ).grid(row=8, column=0, pady =5)

        def sel():
            selection = "Selection: " + str(Range.get()) 
            tkinter.Label(self, text = selection, bg = "white").grid(row = 8, column =1, sticky = "W" + "E", pady = 5)

        Ranges = [".5pF - 470pF", "500pF - 4.7uF", "6.8uF - 3300uF"]
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

        self.backButton = tkinter.Button(self, text="Back", relief = "ridge", width = 30,
            command=lambda: master.switch_frame(QuickSearch))
        self.backButton.grid(row=10, column=1)
