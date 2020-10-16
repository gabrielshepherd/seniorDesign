# import dependancies
import tkinter as tk

# define classes and functions
class MainApplication(tk.Frame):
    def __init__(self, parent):
        # frame = tk.Frame.__init__(self, parent, width=1024, height=600)
        # self.parent = parent
        tk.Tk.__init__(self)
        frame = tk.Frame(self, width=1024, height=600)

# main
def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()