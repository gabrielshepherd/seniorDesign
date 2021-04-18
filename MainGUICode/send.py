import requests
import tkinter as tkinter
from tkinter import messagebox

def data_transmit(location):        # location is a string
    print("we are here")
    try:
        response = requests.get('http://172.16.0.1:5000/transmit', json={'location': str(location)})
    except:
            messagebox.showerror("Connection Error", "Check Connection")
    print(response.status_code)
    print(response.text)
    return "data sent"