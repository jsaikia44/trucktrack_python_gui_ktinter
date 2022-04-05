# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:45:58 2022

@author: Jyotish
"""
import tkinter as tk
import pyttsx3 
  
root= tk.Tk()

engine = pyttsx3.init()

canvas1 = tk.Canvas(root, width = 400, height = 330,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Truck Tracking System')
label1.config(font=('helvetica', 20,"bold"))
canvas1.create_window(200, 35, window=label1)

label2 = tk.Label(root, text='Type the registration Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 130, window=entry1)

label10 = tk.Label(root, text='Type the Gate Number:')
label10.config(font=('helvetica', 10))
canvas1.create_window(200, 170, window=label10)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 200, window=entry2)

def reset_file():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    
def submit_file():
    truckreg = entry1.get()
    truckregnew = " ".join(truckreg)
    gateno = entry2.get()
    
    engine.setProperty("rate", 90)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume',1)  
    engine.say('truck number ' + truckregnew+ ' please go to gate number '+gateno)  
    engine.runAndWait()


button1 = tk.Button(text='Play', width=10, command=submit_file,
                    height=2, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(150, 260, window=button1)
button2 = tk.Button(text='Reset', width=10, 
                    height=2, command=reset_file, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(250, 260, window=button2)

root.mainloop()