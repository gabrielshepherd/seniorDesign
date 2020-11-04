'''
This Program Simply has the 5x5 array of buttons
'''

import tkinter as tk


#Creates a 5x5 grid of buttons
class GridValues(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = tk.Frame(frame_main)
        frame_canvas.grid(row=2, column=2, pady=(5, 0), sticky='e')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = tk.Canvas(frame_canvas, bg="yellow")
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        # Create a frame to contain the buttons
        frame_buttons = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

        # Add 9-by-5 buttons to the frame
        rows = 9
        columns = 5
        buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
        for i in range(0, rows):
            for j in range(0, columns):
                buttons[i][j] = tk.Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
                buttons[i][j].grid(row=i, column=j, sticky='news')

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_buttons.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
        first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height)


        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))


root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

root = GridValues(master=frame_main)

# Launch the GUI
root.mainloop()