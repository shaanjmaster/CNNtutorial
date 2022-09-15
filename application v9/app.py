################
# UCL Third Year Project app
# Updates include:
#   Now importing content from tcont
# Written by Shaan Master
# 24 Jan 2020
################

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tcont import homepage

if __name__ == '__main__':
    #Create root widget
    root = tk.Tk()
    # Create instance of homepage on parent root
    app = homepage.HomePage(master=root)
    # keep root running
    root.mainloop()
