import tkinter as tk
import RPi.GPIO as GPIO

def changesession:
    return 0

root= tk.Tk()
root.geometry('320x240')

scramble = ""
scramblevar = tk.StringVar(master=root, value=scramble)

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
scramblenums = [25, ]
session = 0

sessionbutton = tk.Button(root, text='Change Session', command=changesession)
sessionbutton.grid(row=0, column=0, padx=5, pady=5)

sessionvar = tk.StringVar(master=root,value=sessions[session])
sessionlabel = tk.Label(root, textvariable=sessionvar)
sessionlabel.grid(row=0, column=1, padx=5, pady=5)

ao5 = tk.StringVar(master=root,value="Ao5")
ao5label = tk.Label(root, textvariable=ao5)
ao5label.grid(row=1, column=0, padx=5, pady=5)

time = tk.StringVar(master=root,value="Time")
timelabel = tk.Label(root, textvariable=time)
timelabel.grid(row=1, column=1, padx=5, pady=5)

ao12 = tk.StringVar(master=root,value="Ao12")
ao12label = tk.Label(root, textvariable=ao12)
ao12label.grid(row=1, column=2, padx=5, pady=5)


ao5num = tk.StringVar(master=root,value="-.---")
ao5numlabel = tk.Label(root, textvariable=ao5num)
ao5numlabel.grid(row=2, column=0, padx=5, pady=5)

timenum = tk.StringVar(master=root,value="-.---")
timenumlabel = tk.Label(root, textvariable=timenum)
timenumlabel.grid(row=2, column=1, padx=5, pady=5)

ao12num = tk.StringVar(master=root,value="-.---")
ao12numlabel = tk.Label(root, textvariable=ao12num)
ao12numlabel.grid(row=2, column=2, padx=5, pady=5)


'''
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
'''
root.grid_columnconfigure(1, weight=1)
#root.grid_rowconfigure(1, weight=1)


root.mainloop()