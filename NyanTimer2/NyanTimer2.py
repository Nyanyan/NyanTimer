import tkinter as tk
import RPi.GPIO as GPIO

root= tk.Tk()
root.geometry('320x240')

ao5 = tk.StringVar(master=root,value="Ao5")
ao5label = tk.Label(root, textvariable=ao5)
ao5label.grid(row=0, column=0, padx=5, pady=5)

time = tk.StringVar(master=root,value="Time")
timelabel = tk.Label(root, textvariable=time)
timelabel.grid(row=0, column=1, padx=5, pady=5)

ao12 = tk.StringVar(master=root,value="Ao12")
ao12label = tk.Label(root, textvariable=ao12)
ao12label.grid(row=0, column=2, padx=5, pady=5)


ao5num = tk.StringVar(master=root,value="-.---")
ao5numlabel = tk.Label(root, textvariable=ao5num)
ao5numlabel.grid(row=1, column=0, padx=5, pady=5)

timenum = tk.StringVar(master=root,value="-.---")
timenumlabel = tk.Label(root, textvariable=timenum)
timenumlabel.grid(row=1, column=1, padx=5, pady=5)

ao12num = tk.StringVar(master=root,value="-.---")
ao12numlabel = tk.Label(root, textvariable=ao12num)
ao12numlabel.grid(row=1, column=2, padx=5, pady=5)



bestao5 = tk.StringVar(master=root,value="Best Ao5")
bestao5label = tk.Label(root, textvariable=bestao5)
bestao5label.grid(row=2, column=0, padx=5, pady=5)

besttime = tk.StringVar(master=root,value="Best Time")
besttimelabel = tk.Label(root, textvariable=besttime)
besttimelabel.grid(row=2, column=1, padx=5, pady=5)

bestao12 = tk.StringVar(master=root,value="Best Ao12")
bestao12label = tk.Label(root, textvariable=bestao12)
bestao12label.grid(row=2, column=2, padx=5, pady=5)


bestao5num = tk.StringVar(master=root,value="-.---")
bestao5numlabel = tk.Label(root, textvariable=bestao5num)
bestao5numlabel.grid(row=3, column=0, padx=5, pady=5)

besttimenum = tk.StringVar(master=root,value="-.---")
besttimenumlabel = tk.Label(root, textvariable=besttimenum)
besttimenumlabel.grid(row=3, column=1, padx=5, pady=5)

bestao12num = tk.StringVar(master=root,value="-.---")
bestao12numlabel = tk.Label(root, textvariable=bestao12num)
bestao12numlabel.grid(row=3, column=2, padx=5, pady=5)




root.mainloop()