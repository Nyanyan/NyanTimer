import tkinter as tk
#import RPi.GPIO as GPIO
import random

def changesession():
    sessionOKbutton.grid(row=0, column=0, padx=5, pady=0)
    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    ao5label.grid_forget()
    timelabel.grid_forget()
    ao12label.grid_forget()
    ao5numlabel.grid_forget()
    timenumlabel.grid_forget()
    ao12numlabel.grid_forget()
    scramblelabel1.grid_forget()
    scramblelabel2.grid_forget()

def closechangesession():
    sessionOKbutton.grid_forget()
    sessionbutton.grid(row=0, column=0, padx=5, pady=0)
    sessionlabel.grid(row=0, column=1, padx=5, pady=0)
    ao5label.grid(row=1, column=0, padx=5, pady=0)
    timelabel.grid(row=1, column=1, padx=5, pady=0)
    ao12label.grid(row=1, column=2, padx=5, pady=0)
    ao5numlabel.grid(row=2, column=0, padx=5, pady=0)
    timenumlabel.grid(row=2, column=1, padx=5, pady=0)
    ao12numlabel.grid(row=2, column=2, padx=5, pady=0)
    scramblelabel1.grid(row=3, column=0, columnspan=3, padx=5, pady=0)
    scramblelabel2.grid(row=4, column=0, columnspan=3, padx=5, pady=0)

def delete():
    return 0

def stat():
    return 0

def next():
    global scramblevar1, scramblevar2
    scramble = ""
    scramble1 = ""
    scramble2 = ""
    pre = ""
    rotation = 0
    rotations = [['R', 'L', 'U', 'D', 'F', 'B'], ['R', 'L', 'U', 'D', 'F', 'B', 'Rw', 'Lw', 'Uw', 'Dw', 'Fw', 'Bw']]
    adds = ['', '\'', '2']
    for i in range(scramblenums[session]):
        rot = rotations[rotation][random.randint(0, len(rotations[rotation]) - 1)]
        while pre == rot:
            rot = rotations[rotation][random.randint(0, len(rotations[rotation]) - 1)]
        add = adds[random.randint(0, 2)]
        scramble += rot + add + ' '
        pre = rot
    if len(scramble) > 40:
        i = 40
        while scramble[i] in adds:
            i += 1
        scramble1 = scramble[:i]
        scramble2 = scramble[i:]
    else:
        scramble1 = scramble
        scramble2 = ""
    scramblevar1.set(scramble1)
    scramblevar2.set(scramble2)

root= tk.Tk()
root.geometry('320x240')

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
scramblenums = [25]
session = 0

scramble1 = ""
scramble2 = ""




sessionbutton = tk.Button(root, text='Session', command=changesession)
sessionbutton.grid(row=0, column=0, padx=5, pady=0)

sessionOKbutton = tk.Button(root, text='  OK  ', command=closechangesession)

sessionvar = tk.StringVar(master=root,value=sessions[session])
sessionlabel = tk.Label(root, textvariable=sessionvar)
sessionlabel.grid(row=0, column=1, padx=5, pady=0)

ao5 = tk.StringVar(master=root,value="Ao5")
ao5label = tk.Label(root, textvariable=ao5)
ao5label.grid(row=1, column=0, padx=5, pady=0)

time = tk.StringVar(master=root,value="Time")
timelabel = tk.Label(root, textvariable=time)
timelabel.grid(row=1, column=1, padx=5, pady=0)

ao12 = tk.StringVar(master=root,value="Ao12")
ao12label = tk.Label(root, textvariable=ao12)
ao12label.grid(row=1, column=2, padx=5, pady=0)


ao5num = tk.StringVar(master=root,value="-.---")
ao5numlabel = tk.Label(root, textvariable=ao5num)
ao5numlabel.grid(row=2, column=0, padx=5, pady=0)

timenum = tk.StringVar(master=root,value="-.---")
timenumlabel = tk.Label(root, textvariable=timenum)
timenumlabel.grid(row=2, column=1, padx=5, pady=0)

ao12num = tk.StringVar(master=root,value="-.---")
ao12numlabel = tk.Label(root, textvariable=ao12num)
ao12numlabel.grid(row=2, column=2, padx=5, pady=0)


scramblevar1 = tk.StringVar(master=root, value=scramble1)
scramblelabel1 = tk.Label(root, textvariable=scramblevar1)
scramblelabel1.grid(row=3, column=0, columnspan=3, padx=5, pady=0)

scramblevar2 = tk.StringVar(master=root, value=scramble2)
scramblelabel2 = tk.Label(root, textvariable=scramblevar2)
scramblelabel2.grid(row=4, column=0, columnspan=3, padx=5, pady=0)

root.columnconfigure(0, weight=1, uniform='group1')
root.columnconfigure(1, weight=1, uniform='group1')
root.columnconfigure(2, weight=1, uniform='group1')

deletebutton = tk.Button(root, text='  Delete  ', command=delete)
deletebutton.grid(row=5, column=0, padx=5, pady=10)

statbutton = tk.Button(root, text='  Status  ', command=stat)
statbutton.grid(row=5, column=1, padx=5, pady=10)

nextbutton = tk.Button(root, text='   Next   ', command=next)
nextbutton.grid(row=5, column=2, padx=5, pady=10)


root.mainloop()