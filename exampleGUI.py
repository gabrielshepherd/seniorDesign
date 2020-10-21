#2/20/2020
#2/27/2020
#3/5/2020 Button_picture dup

'''
Issue unable to light up one neopixel indivudually line 57 (FIXED/SOlved) 2-27-2020
Notes to self NEED .pack() at the end of statements
**Must HAVE double perentheses around pixels.fill((0, 0, 0)) to prevent arugment error
#Trying to get a jpg also might try changing pack into grids? //Cannot have packs and grids at the same time
'''
# import board
# import neopixel
#import Image 
from tkinter import *
import tkinter as tk



# pixels = neopixel.NeoPixel(board.D18, 150)

############# FORMAT!!
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def led(self,pixelsnum,greenn,redd,bluee):
        pixels[pixelsnum] = (greenn, redd, bluee)
        
    #def image():
        
    
############# HOME PAGE
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome to Parts Inventory Finder", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
    
        tk.Button(self, text="Resistors",
                  command=lambda: master.switch_frame(PageOne)).pack(fill="x")
        tk.Button(self, text="Transistors",
                  command=lambda: master.switch_frame(PageTwo)).pack(fill="x")
        tk.Button(self, text="Capacitors",
                  command=lambda: master.switch_frame(PageThree)).pack(fill="x")
        tk.Button(self, text="Other",
                  command=lambda: master.switch_frame(Page4)).pack(fill="x")
        
        tk.Button(self, text="Photo Directory",
                  command=lambda: master.switch_frame(Page5)).pack(fill="x")
        
        tk.Button(self, text="Test",
                  command=lambda: pixels.fill((255, 255, 0))).pack(fill="x")
        
        tk.Button(self, text="Clear",
                  command=lambda: pixels.fill((0, 0, 0))).pack(fill="x")
        
    

        
#############RESISTORS
class PageOne(tk.Frame):
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='')
        tk.Label(self, bg='Green',text="Resistors", font=('Helvetica', 18, "bold")).pack(side="top", fill="both", pady=0)
        
        '''tk.Button(self, text=" ",command=lambda: SampleApp.led(self,#LEDSpot 0 - Num_of_LED,red 0-255,blue 0-255,green0-255)).pack(fill="x")'''
        tk.Button(self, text="1K Ω Brown/Black/Red/Gold",command=lambda: SampleApp.led(self,149,255,255,0)).pack(fill="x")
        tk.Button(self, text="2k Ω",command=lambda: SampleApp.led(self,50,0,255,0)).pack(fill="x")
        tk.Button(self, text="3k Ω",command=lambda: SampleApp.led(self,50,255,0,0)).pack(fill="x")
        
        tk.Button(self, text="4k Ω",command=lambda: SampleApp.led(self,50,255,255,0)).pack(fill="x")
        tk.Button(self, text="5k Ω",command=lambda: SampleApp.led(self,6,255,255,0)).pack(fill="x")
        tk.Button(self, text="6k Ω",command=lambda: SampleApp.led(self,7,255,255,0)).pack(fill="x")
        
        tk.Button(self, text="hehe Ω",command=lambda: SampleApp.led(self,8,255,255,0)).pack(fill="x")
        
        tk.Button(self, text="Reset", command=lambda: pixels.fill((0, 0, 0))).pack(side="bottom")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(StartPage)).pack(side="bottom")

#############TRANSISTORS
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='')
        tk.Label(self,bg="Gold",text="Transistors", font=('Helvetica', 18, "bold")).pack(side="top", fill="both", pady=0)
        
        tk.Button(self, text="1K Ω",command=lambda: SampleApp.led(self,30,255,255,0)).pack(fill="x")
        tk.Button(self, text="2k Ω",command=lambda: SampleApp.led(self,31,255,255,0)).pack(fill="x")
        tk.Button(self, text="3k Ω",command=lambda: SampleApp.led(self,32,255,255,0)).pack(fill="x")
        tk.Button(self, text="4k Ω",command=lambda: SampleApp.led(self,33,255,255,0)).pack(fill="x")
        tk.Button(self, text="5k Ω",command=lambda: SampleApp.led(self,34,255,255,0)).pack(fill="x")
        tk.Button(self, text="6k Ω",command=lambda: SampleApp.led(self,35,255,255,0)).pack(fill="x")
        
        tk.Button(self, text="Reset", command=lambda: pixels.fill((0,0, 0))).pack()
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(StartPage)).pack()

#############CAPACITORS
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='Dark Green')
        tk.Label(self, text="Capacitors", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Reset",
                  command=lambda: pixels.fill((0, 0, 0))).pack()
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        
#############Other       
class Page4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='Dark Green')
        tk.Label(self, text="OTHER", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Reset",
                  command=lambda: pixels.fill((0, 0, 0))).pack()
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        
class Page5(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='Green')
        tk.Label(self, text="OTHER", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Reset",
                  command=lambda: pixels.fill((0, 0, 0))).pack()
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        
################# MISC
if __name__ == "__main__":
    app = SampleApp()
    app.title('Inventory Database')
    app.geometry('500x300')
    app.mainloop()




