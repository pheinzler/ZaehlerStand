#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import modules

class Main(tk.Frame):
    def __init__(self, master =None):
        tk.Frame.__init__(self, master)
        self.root = master       
        self.create_widgets()
        self.count = 0
    
    def create_widgets(self):
        def cnt():
            self.lable = tk.Label(self.root, text= str(self.count))
            self.count +=1
            self.lable.grid(row=0, column=0)
        self.button = tk.Button(self.root, command= cnt, text="Count")
        self.button.grid(row=1, column= 0)

if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()