import tkinter as tk
import RPi.GPIO as GPIO

root= tk.Tk()
root.geometry('320x240')

time = tk.DoubleVar(master=root,value=0.000)
timelabel = tk.Label(root, textvariable=videolabelvar)
time.grid(row=3, column=3, padx=5, pady=5)

root.mainloop()