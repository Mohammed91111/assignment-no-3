# Importing the necessary module for creating the GUI
import tkinter as tk
# Importing the GUI class from the gui module
from gui import GUI

# Check if this script is being run directly
if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()
    # Create an instance of the GUI class, passing the root window as an argument
    app = GUI(root)
    # Start the Tkinter event loop, allowing the GUI to be interactive
    root.mainloop()
