#gui for sr design
from tkinter import *
#from PIL import ImageTk, Image
root = Tk()
root.title("NDSU ECE INVENTORY")
root.iconbitmap('c:/ndsuicon.ico')
#frames for each GUI section
frame_for_keypad = LabelFrame(root, text= "Enter Part Value Here", padx=5, pady=5,fg="green",bg="gold")
frame_for_keypad.grid(row=1, column=0, padx=50, pady=50)
frame_for_parts = LabelFrame(root, text= "Choose Part Type Here", padx=5, pady=5,fg="green",bg="gold")
frame_for_parts.grid(row=2, column=0, padx=50, pady=50)
frame_for_units = LabelFrame(root, text= "Select Unit", padx=5, pady=5,fg="green",bg="gold")
frame_for_units.grid(row=1, column=1, padx=50, pady=50)
frame_for_features = LabelFrame(root, text= "Misc Features", padx=5, pady=5,fg="green",bg="gold")
frame_for_features.grid(row=2, column=1, padx=50, pady=50)


#img = ImageTk.PhotoImage(image.open(bison.png))

#Bison = Label(image=img)
#Bison.grid(row=5, column=1, columnspan=3)

#######################Keypad Code#############################################################
#entrybox
e= Entry(frame_for_keypad, fg="gold",bg="green", width=35, borderwidth=5)
e.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

def click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def enter():
    return


#buttons
Keypad_0 = Button(frame_for_keypad, text = "0", padx=45, pady=10, command=lambda: click(0), fg="gold",bg="green")
Keypad_1 = Button(frame_for_keypad, text = "1", padx=45, pady=10, command=lambda: click(1), fg="gold",bg="green")
Keypad_2 = Button(frame_for_keypad, text = "2", padx=45, pady=10, command=lambda: click(2), fg="gold",bg="green")
Keypad_3 = Button(frame_for_keypad, text = "3", padx=45, pady=10, command=lambda: click(3), fg="gold",bg="green")
Keypad_4 = Button(frame_for_keypad, text = "4", padx=45, pady=10, command=lambda: click(4), fg="gold",bg="green")
Keypad_5 = Button(frame_for_keypad, text = "5", padx=45, pady=10, command=lambda: click(5), fg="gold",bg="green")
Keypad_6 = Button(frame_for_keypad, text = "6", padx=45, pady=10, command=lambda: click(6), fg="gold",bg="green")
Keypad_7 = Button(frame_for_keypad, text = "7", padx=45, pady=10, command=lambda: click(7), fg="gold",bg="green")
Keypad_8 = Button(frame_for_keypad, text = "8", padx=45, pady=10, command=lambda: click(8), fg="gold",bg="green")
Keypad_9 = Button(frame_for_keypad, text = "9", padx=45, pady=10, command=lambda: click(9), fg="gold",bg="green")
Keypad_dec = Button(frame_for_keypad, text = ".", padx=45, pady=10, command=lambda: click(0.), fg="gold",bg="green")
Keypad_enter = Button(frame_for_keypad, text = "enter", padx=129, pady=10, command=lambda: enter(), fg="gold",bg="green")
Keypad_clear = Button(frame_for_keypad, text = "clear", padx=129, pady=10, command=lambda: clear(), fg="gold",bg="green")
#put buttons on screen
Keypad_0.grid(row=4 , column=0)
Keypad_dec.grid(row=4 , column=1)
Keypad_enter.grid(row=4 , column=2)

Keypad_1.grid(row=3 , column=0)
Keypad_2.grid(row=3 , column=1)
Keypad_3.grid(row=3 , column=2)

Keypad_4.grid(row=2 , column=0)
Keypad_5.grid(row=2 , column=1)
Keypad_6.grid(row=2 , column=2)

Keypad_7.grid(row=1 , column=0)
Keypad_8.grid(row=1 , column=1)
Keypad_9.grid(row=1 , column=2)

Keypad_clear.grid(row=5 , column=0,columnspan=3)
Keypad_enter.grid(row=6 , column=0,columnspan=3)
##########################################################end of keypad############################################################

####################################start part type#########################################################

MODES = [
    ("Resistors(ohms)", "Resistors(ohms)"),
    ("Capacitors(farads)", "Capacitors(farads)"),
    ("Inductors(henry)", "Inductors(henry)"),
    ("OP-Amps(volts)", "OP-Amps(volts)"),
    ("IC-chips", "IC-chips"),
    ("NPN Transistors", "NPN Transistors"),
    ("PNP Transistors", "PNP Transistors"),
    ("H-Bridges", "H-Bridges"),   
    ("Other", "Other"),

]

Part = StringVar()
Part.set("Resistors")

for text, mode in MODES:
    Radiobutton(frame_for_parts, text = text, variable = Part, value = mode, fg="black",bg="green").pack(anchor=W)


def clicked(value):
    partlable = Label(frame_for_parts, text = value,fg="gold",bg="green")
    partlable.pack()


partbutton = Button(frame_for_parts, text = "Enter",fg="gold",bg="green", padx=20, pady=10 , command = lambda: clicked(Part.get()))
partbutton.pack()

###########################end part type################################################

#########################start unit#####################################################
MODES = [
    ("pico(10^-12)", "pico(10^-12)"),
    ("nano(10^-9)", "nano(10^-9)"),
    ("micro(10^-6)", "micro(10^-6)"),
    ("mili(10^-3)", "mili(10^-3)"),
    ("Base(10^0)", "Base(10^0)"),
    ("kilo(10^+3)", " kilo(10^+3)"),
   
]

Parts = StringVar()
Parts.set("Resistors")

for text, mode in MODES:
    Radiobutton(frame_for_units, text = text, variable = Parts, value = mode, fg="black",bg="green").pack(anchor=W)


def clicked_(value):
    partlable_ = Label(frame_for_units, text = value,fg="gold",bg="green")
    partlable_.pack()


partbutton = Button(frame_for_units, text = "Enter",fg="gold",bg="green", padx=20, pady=10 , command = lambda: clicked_(Parts.get()))
partbutton.pack()

#######################################end units#######################################################

#########################################features######################################################
button_logout = Button(frame_for_features, text = "EXIT NDSU ECE INVENTORY", command = root.quit, fg="gold",bg="green", padx=20, pady=5)
button_logout.pack()

button_admin = Button(frame_for_features, text = "Admin", fg="gold",bg="green", padx=20, pady=5)
button_admin.pack()

button_Search_History =Button(frame_for_features, text = "Search History", fg="gold",bg="green", padx=20, pady=5)
button_Search_History.pack()

#mainloop
root.mainloop()


