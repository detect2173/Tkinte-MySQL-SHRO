from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
    def __init__(self, root):
        self.root = root
        titlespace = ' '
        self.root.title(95 * titlespace + "SHRO Inventory Database")
        self.root.geometry('770x700+300+0')
        self.root.resizable(width=False, height=False)


if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()