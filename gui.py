#gui for sr design
from tkinter import *

root = Tk()




def click():
    myLabel = Label(root, text="button pressed")
    myLabel.pack()
#buttons
myButton = Button(root, text = "click", padx=10, pady=10, command=click, fg="gold",bg="green")

myButton.pack()

#mainloop
root.mainloop()










