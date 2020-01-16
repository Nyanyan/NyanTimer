import tkinter as tk
import RPi.GPIO as GPIO

root= tk.Tk()
root.geometry('320x240')

ao5 = tk.StringVar(master=root,value="Ao5: 0.000")
ao5label = tk.Label(root, textvariable=ao5)
ao5label.grid(row=0, column=0, padx=5, pady=5)

time = tk.StringVar(master=root,value="Time: 0.000")
timelabel = tk.Label(root, textvariable=time)
timelabel.grid(row=0, column=1, padx=5, pady=5)

ao12 = tk.StringVar(master=root,value="Ao12: 0.000")
ao12label = tk.Label(root, textvariable=ao12)
ao12label.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()