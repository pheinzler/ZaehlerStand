#!/usr/bin/python3
import tkinter as tk
import tkinter.font
from tkinter import ttk
import modules

#TITLE_FONT = tkinter.font.Font(family= 'Avantgarde', size=18)

#colours
DARK_ENTRIES = 'grey50'

class Main(tk.Frame):
    def __init__(self, master =None):
        tk.Frame.__init__(self, master)
        self.root = master      

        self.kitchen = modules.Gemeinsam('kitchen' , 1,1,1)
        self.bath = modules.Gemeinsam('bath', 1,1,1) 
        self.user1 = modules.Zimmer('Patrick', 1)
        self.user2 = modules.Zimmer('Simon', 1)
        self.user3 = modules.Zimmer('Jule', 1)

        self.create_widgets()
    
    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0,column=0)
        title = tk.Label(frame, text= "Zählerstände" )
        title.grid(row=0 , column= 0)

        kitchenlable = tk.Label(frame, text='Kitchen: ')
        kitchenlable.grid(row=2, column=0)
        bathlable = tk.Label(frame, text='Bath: ')
        bathlable.grid(row=4, column=0)

        #lables und entires fuer kueche und bad
        lablenames = ['Water Warm:','Water Cold:', 'Heater:']        
        lables_kitchen = [tk.Label(frame, text= i) for i in lablenames]
        lables_bath = [tk.Label(frame, text= i) for i in lablenames]
        entries_kitchen = [tk.Entry(frame, width=30,background= DARK_ENTRIES) for _ in range(3)]
        entries_bath = [tk.Entry(frame, width=30, background= DARK_ENTRIES) for _ in range(3)]
        kitchenprev= [tk.Label(frame, text= str(self.kitchen.warm)),tk.Label(frame, text= str(self.kitchen.cold)),tk.Label(frame, text= str(self.kitchen.heater))]
        bathprev= [tk.Label(frame, text= str(self.bath.warm)),tk.Label(frame, text= str(self.bath.cold)),tk.Label(frame, text= str(self.bath.heater))]
        
        #labels und entries fuer Einzelzimmer
        einzel_lablenames=['Patrick' , 'Simon' , 'Jule']
        einzel_lables = [tk.Label(frame,text=i) for i in einzel_lablenames]
        einzel_entries = [tk.Entry(frame, width=30, background=DARK_ENTRIES) for _ in range(3)]

        #Kueche und Bad Lable und Entries anzeigen
        cnt = 0
        for i in range(1,7):
            if i % 2 == 1:
                lables_kitchen[cnt].grid(row= 2, column=i)
                lables_bath[cnt].grid(row= 4, column=i)

            else:
                entries_kitchen[cnt].grid(row=2, column=i)
                kitchenprev[cnt].grid(row=3, column=i, sticky=tk.E)
                entries_bath[cnt].grid(row=4, column=i)
                bathprev[cnt].grid(row=5, column=i, sticky=tk.E)
                cnt += 1

        for i  in range(3):
            einzel_lables[i].grid(row=i+6, column=0)
            einzel_entries[i].grid(row=i+6, column=2)
if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()