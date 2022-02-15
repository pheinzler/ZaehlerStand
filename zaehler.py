#!/usr/bin/python3
import tkinter as tk
import tkinter.font
from tkinter import END, RIGHT, ttk
import modules
import pickle

#TITLE_FONT = tkinter.font.Font(family= 'Avantgarde', size=18)

#colours
DARK_ENTRIES = 'grey50'
RED = 'red'

#actual color settings

DARK_USERS = DARK_ENTRIES

class Main(tk.Frame):
    def __init__(self, master =None):
        tk.Frame.__init__(self, master)
        self.root = master      
        #gemeinsam klasse: ww,wc,h
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
        entries_kitchen = [tk.Entry(frame, width=20,background= DARK_USERS,justify=RIGHT) for _ in range(3)]
        entries_bath = [tk.Entry(frame, width=20, background= DARK_USERS,justify=RIGHT) for _ in range(3)]
        kitchenprev= [tk.Label(frame, text= str(self.kitchen.warm)),tk.Label(frame, text= str(self.kitchen.cold)),tk.Label(frame, text= str(self.kitchen.heater))]
        bathprev= [tk.Label(frame, text= str(self.bath.warm)),tk.Label(frame, text= str(self.bath.cold)),tk.Label(frame, text= str(self.bath.heater))]
        
        #labels und entries fuer Einzelzimmer
        einzel_lablenames=['Patrick' , 'Simon' , 'Jule']
        einzel_lables = [tk.Label(frame,text=i) for i in einzel_lablenames]
        einzel_entries = [tk.Entry(frame, width=20, background=DARK_USERS,justify=RIGHT) for _ in range(3)]
        user_labels = [tk.Label(frame, text= x.heater) for x in [self.user1, self.user2, self.user3]]

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

        #Einzellabels
        cnt = 0
        for i in range(6,11,2):
            einzel_lables[cnt].grid(row=i, column=0)
            einzel_entries[cnt].grid(row=i, column=2)
            user_labels[cnt].grid(row=i+1, column= 2, sticky=tk.E)
            cnt+=1

        def save():
            #pickleaufbau: 1 liste mit 3 dicts mit je 2 listen einträgen: zählerstände + differences
            for i, x in enumerate(entries_kitchen):
                val = int(x.get())
                if i == 0:
                    self.kitchen.warm_set(val)
                elif i == 1:
                    self.kitchen.cold_set(val)
                else:
                    self.kitchen.heater_set(val)

            for i, x in enumerate(entries_bath):
                val = int(x.get())
                if i == 0:
                    self.bath.warm_set(val)
                elif i == 1:
                    self.bath.cold_set(val)
                else:
                    self.bath.heater_set(val)
            
            for i, x in enumerate(einzel_entries):
                val = int(x.get())
                if i == 0:
                    self.user1.heater_set(val)
                elif i == 1:
                    self.user2.heater_set(val)
                else:
                    self.user3.heater_set(val)
            
            final_lis = [self.kitchen.getall(), self.bath.getall(), self.user1.getall(), self.user2.getall(), self.user3.getall()]
            file = open('aktuelle_stats', 'wb')
            pickle.dump(final_lis, file)
            file.close()
            
        def clear():
            for x in entries_kitchen:
                x.delete(0,END)
            for x in entries_bath:
                x.delete(0,END)
            for x in einzel_entries:
                x.delete(0,END)
        
        def show():
            print('show')

        #buttons
        btn_frame = tk.Frame(self.root,background= 'blue')
        btn_frame.grid(row=12, column=1)
        save_btn = tk.Button(btn_frame, text='Save', background= DARK_USERS, command= save)
        save_btn.grid(row=0,column=0)
        clear_btn = tk.Button(btn_frame, text='Clear', background= DARK_USERS, command= clear)
        clear_btn.grid(row=0, column=1)
        show_btn = tk.Button(btn_frame, text= 'ShowStats' , background= DARK_USERS, command=show)
        show_btn.grid(row= 0, column= 2)
        quit_btn = tk.Button(btn_frame, text= 'Quit', background='red', command= self.root.destroy)
        quit_btn.grid(row= 0 , column=3)


if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()