import tkinter as tk
from login import*
from hotel import hotelman
import mysql.connector

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    login()
   # mainWindow()

    root.mainloop()
