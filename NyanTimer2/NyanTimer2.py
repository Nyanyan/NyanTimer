import tkinter as tk
#import RPi.GPIO as GPIO
import random
import time
import csv
import numpy
import math
import os
import pandas as pd
import subprocess
import urllib

def changesession():
    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    for i in range(3):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    scramblelabel1.grid_forget()
    scramblelabel2.grid_forget()
    scramblelabel3.grid_forget()
    scramblelabel4.grid_forget()
    deletebutton.grid_forget()
    statbutton.grid_forget()
    nextbutton.grid_forget()
    startbutton.grid_forget()

    for i in range(len(sessions)):
        sessionbuttons[i].grid(row=i // 3 + 1, column=i % 3, padx=5, pady=5)


def switchsession(num):
    #print(num)
    def x():
        global session
        session = num
        sessionvar.set(sessions[session])

        sessionbutton.grid(row=0, column=0, padx=5, pady=0)
        sessionlabel.grid(row=0, column=1, padx=5, pady=0)

        arr = [1, 0, 2]
        for i in range(3):
            for j in range(2):
                guiavgstatus[arr[i]][j].grid(row=j + 1, column=i, padx=5, pady=0)
        
        scramblelabel1.grid(row=3, column=0, columnspan=3, padx=5, pady=0)
        scramblelabel2.grid(row=4, column=0, columnspan=3, padx=5, pady=0)
        scramblelabel3.grid(row=5, column=0, columnspan=3, padx=5, pady=0)
        scramblelabel4.grid(row=6, column=0, columnspan=3, padx=5, pady=0)
        deletebutton.grid(row=7, column=0, padx=5, pady=10)
        statbutton.grid(row=7, column=1, padx=5, pady=10)
        nextbutton.grid(row=7, column=2, padx=5, pady=10)
        startbutton.grid(row=8, column=1, padx=5, pady=10)

        for i in range(len(sessions)):
            sessionbuttons[i].grid_forget()

        nextscramble()
        calctime()
    return x

def delete():
    rows = numpy.asarray(pd.read_csv('data'+sessions[session] + '.csv',header=0))
    #print(rows)
    with open('data'+sessions[session] + '.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['Number', 'Scramble', 'Single', 'Best Single', 'Best Single No', 'Ao5', 'Best Ao5', 'Best Ao5 No', 'Ao12', 'Best Ao12', 'Best Ao12 No', 'Ao50', 'Best Ao50', 'Best Ao50 No', 'Ao100', 'Best Ao100', 'Best Ao100 No', 'Ao1000', 'Best Ao1000', 'Best Ao1000 No'])
    with open('data'+sessions[session] + '.csv', mode='a') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in range(len(rows) - 1):
            writer.writerow(rows[i])
    calctime()

def stat():
    calctime()
    sessionbutton.grid_forget()
    scramblelabel1.grid_forget()
    scramblelabel2.grid_forget()
    scramblelabel3.grid_forget()
    scramblelabel4.grid_forget()
    deletebutton.grid_forget()
    statbutton.grid_forget()
    nextbutton.grid_forget()
    startbutton.grid_forget()

    statbackbutton.grid(row=0, column=0, padx=5, pady=0)

    for i in range(3, len(avgnum)):
        for j in range(2):
            guiavgstatus[i][j].grid(row=j + 3, column=i - 3, padx=5, pady=0)

    arr = [1, 0, 2, 3, 4, 5]
    for i in range(len(avgnum)):
        for j in range(2):
            guibavgstatus[arr[i]][j].grid(row=j + 5 + 2 * (i // 3), column=i % 3, padx=5, pady=0)

def statback():
    statbackbutton.grid_forget()
    sessionbutton.grid(row=0, column=0, padx=5, pady=0)
    scramblelabel1.grid(row=3, column=0, columnspan=3, padx=5, pady=0)
    scramblelabel2.grid(row=4, column=0, columnspan=3, padx=5, pady=0)
    scramblelabel3.grid(row=5, column=0, columnspan=3, padx=5, pady=0)
    scramblelabel4.grid(row=6, column=0, columnspan=3, padx=5, pady=0)
    deletebutton.grid(row=7, column=0, padx=5, pady=10)
    statbutton.grid(row=7, column=1, padx=5, pady=10)
    nextbutton.grid(row=7, column=2, padx=5, pady=10)
    startbutton.grid(row=8, column=1, padx=5, pady=10)

    for i in range(3, len(avgnum)):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    for i in range(len(avgnum)):
        for j in range(2):
            guibavgstatus[i][j].grid_forget()
    
def nextscramble():
    global scramble
    '''
    global scramblevar1, scramblevar2
    scramble = ""
    scramble1 = ""
    scramble2 = ""
    pre = ""
    scramblenums = [25, 10, 40]
    rotationnum = [0,0,1]
    rotation = rotationnum[session]
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
    '''
    #res = subprocess.call('java -jar TNoodle-WCA-0.15.1.jar')
    #print(res)
    string = ['333', '222', '444', '555', '666', '777', '333ni', '333', 'clock', 'minx', 'pyram', 'skewb', 'sq1', '444ni', '555ni']
    response = urllib.request.urlopen('http://localhost:2014/scramble/.txt?e=' + string[session])
    scramble = response.read().decode('utf8', 'ignore').rstrip(os.linesep)
    response.close()
    #scramble = subprocess.check_output('curl "http://localhost:2014/scramble/.txt?e=' + string[session] + '"', shell=False).decode('utf8', 'ignore').rstrip(os.linesep)
    print(scramble)
    l = 0
    j = 0
    scrambles = ['','','','']
    while l < len(scramble) and j < 4:
        i = 45 * (j + 1)
        if i <= len(scramble)-1:
            while scramble[i] != ' ':
                i -= 1
        scrambles[j] = scramble[l:i]
        j += 1
        l = i
    scramblevar1.set(scrambles[0])
    scramblevar2.set(scrambles[1])
    scramblevar3.set(scrambles[2])
    scramblevar4.set(scrambles[3])


def timing():
    global starttime
    starttime = time.time()
    #print(starttime)

    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    for i in range(3):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    scramblelabel1.grid_forget()
    scramblelabel2.grid_forget()
    scramblelabel3.grid_forget()
    scramblelabel4.grid_forget()
    deletebutton.grid_forget()
    statbutton.grid_forget()
    nextbutton.grid_forget()
    startbutton.grid_forget()

    stopbutton.grid(row=6, column=1, padx=5, pady=10)

def stoptiming():
    global avgnum, scramble
    exceptpercentage = 5
    stoptime = time.time()
    #print(stoptime)
    single = math.floor((stoptime - starttime) * pow(10,3)) / pow(10, 3)
    print(single)
    #timenum.set(str(tmp))
    timestatus[0].set(str(single))
    rows = numpy.asarray(pd.read_csv('data'+sessions[session] + '.csv', header=0))
    number = len(rows)
    #print(number)
    if number >= 1:
        #f = open('data'+sessions[session] + '.csv', 'r')
        #f.close()
        row1 = rows[number - 1]
        rowavg = []
        for i in avgnum[1:]:
            rowavg.append(rows[max(0, number - i + 1):])
        avg = []
        for i in range(len(avgnum) - 1):
            aox = 0
            if len(rowavg[i]) == avgnum[i + 1] - 1:
                times = []
                for j in range(avgnum[i + 1] - 1):
                    times.append(rowavg[i][j][2])
                times.append(single)
                #print(times)
                times.sort()
                #print(times, avgnum[i + 1])
                exceptnum = math.ceil(avgnum[i + 1] * exceptpercentage / 100)
                for j in range(exceptnum, avgnum[i + 1] - exceptnum):
                    aox += times[j]
                aox /= avgnum[i + 1] - 2 * exceptnum
                aox = math.floor(aox * 1000) / 1000
                timestatus[i + 1].set(str(round(aox, 3)))
            avg.append(aox)
        #print(avg)
        with open('data'+sessions[session] + '.csv', mode='a') as f:
            writer = csv.writer(f, lineterminator='\n')
            no = row1[4]
            if single < row1[3]:
                no = number + 1
            newrow = [number + 1, scramble, single, min(single, row1[3]), no]
            for i in range(1, len(avgnum)):
                newrow.append(avg[i - 1])
                formerpb = row1[3 * i + 3]
                pb = min(avg[i - 1], formerpb)
                if pb == 0:
                    pb = avg[i - 1]
                no = row1[3 * i + 4]
                pb = round(pb, 3)
                if pb == avg[i - 1] and pb != formerpb:
                    no = number + 1
                newrow.append(pb)
                newrow.append(no)
            #print(newrow)
            writer.writerow(newrow)
    else:
        with open('data'+sessions[session] + '.csv', mode='a') as f:
            writer = csv.writer(f, lineterminator='\n')
            newrow = [number + 1, scramble, single, single, number + 1]
            for i in range(1, len(avgnum)):
                for j in range(3):
                    newrow.append(0)
            writer.writerow(newrow)
    sessionbutton.grid(row=0, column=0, padx=5, pady=0)
    sessionlabel.grid(row=0, column=1, padx=5, pady=0)
    arr = [1, 0, 2]
    for i in range(3):
        for j in range(2):
            guiavgstatus[arr[i]][j].grid(row=j + 1, column=i, padx=5, pady=0)
    scramblelabel1.grid(row=3, column=0, columnspan=3, padx=5, pady=0)
    scramblelabel2.grid(row=4, column=0, columnspan=3, padx=5, pady=0)
    scramblelabel3.grid(row=5, column=0, columnspan=3, padx=5, pady=0)
    scramblelabel4.grid(row=6, column=0, columnspan=3, padx=5, pady=0)
    deletebutton.grid(row=7, column=0, padx=5, pady=10)
    statbutton.grid(row=7, column=1, padx=5, pady=10)
    nextbutton.grid(row=7, column=2, padx=5, pady=10)
    startbutton.grid(row=8, column=1, padx=5, pady=10)

    stopbutton.grid_forget()
    nextscramble()

def calctime():
    rows = numpy.asarray(pd.read_csv('data'+sessions[session] + '.csv', header=0))
    number = len(rows)
    if number > 0:
        row = rows[number - 1]
        for i in range(2, number):
            row[i] = round(row[i], 3)
        for i in range(len(avgnum)):
            if row[3 * i + 2] > 0:
                timestatus[i].set(row[3 * i + 2])
                btimestatus[i].set(row[3 * i + 3])
            else:
                timestatus[i].set('--.---')
                btimestatus[i].set('--.---')
        for i in range(len(avgnum)):
            start = number - avgnum[i] + 1
            if start > 0:
                for j in range(avgnum[i]):
                    timesstatus[i][j][0].set(rows[start + j - 1][2])
                    timesstatus[i][j][1].set(rows[start + j - 1][1])
        for i in range(len(avgnum)):
            start = row[3 * i + 4] -avgnum[i] + 1
            if start > 0:
                for j in range(avgnum[i]):
                    btimesstatus[i][j][0].set(rows[start + j - 1][2])
                    btimesstatus[i][j][1].set(rows[start + j - 1][1])
    else:
        for i in range(len(avgnum)):
            timestatus[i].set('--.---')
        for i in range(len(avgnum)):
            btimestatus[i].set('--.---')


def viewtime(num):
    def x():
        return 0
    return x

def viewbtime(num):
    def x():
        return 0
    return x

root= tk.Tk()
root.geometry('320x240')

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
session = 0
avgnum = [1, 5, 12, 50, 100, 1000]

for s in sessions:
    if not os.path.isfile('data' + s + '.csv'):
        with open('data' + s + '.csv', mode='x') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['Number', 'Scramble', 'Single', 'Best Single', 'Best Single No', 'Ao5', 'Best Ao5', 'Best Ao5 No', 'Ao12', 'Best Ao12', 'Best Ao12 No', 'Ao50', 'Best Ao50', 'Best Ao50 No', 'Ao100', 'Best Ao100', 'Best Ao100 No', 'Ao1000', 'Best Ao1000', 'Best Ao1000 No'])


scramble = ''


sessionbutton = tk.Button(root, text='Session', command=changesession)
sessionbutton.grid(row=0, column=0, padx=5, pady=0)


sessionvar = tk.StringVar(master=root,value=sessions[session])
sessionlabel = tk.Label(root, textvariable=sessionvar)
sessionlabel.grid(row=0, column=1, padx=5, pady=0)

timestatus = []
guiavgstatus = []
for i in range(len(avgnum)):
    timestatus.append(tk.StringVar(master=root,value="--.---"))
    if i > 0:
        guiavgstatus.append([tk.Label(root, text="Ao"+str(avgnum[i])), tk.Button(root, textvariable=timestatus[i], command=viewtime(i))])
    if i == 0:
        guiavgstatus.append([tk.Label(root, text="Single"), tk.Button(root, textvariable=timestatus[i], command=viewtime(i))])

btimestatus = []
guibavgstatus = []
for i in range(len(avgnum)):
    btimestatus.append(tk.StringVar(master=root,value="--.---"))
    if i > 0:
        guibavgstatus.append([tk.Label(root, text="Best Ao"+str(avgnum[i])), tk.Button(root, textvariable=btimestatus[i], command=viewbtime(i))])
    if i == 0:
        guibavgstatus.append([tk.Label(root, text="Best Single"), tk.Button(root, textvariable=btimestatus[i], command=viewbtime(i))])

timesstatus = []
for i in range(len(avgnum)):
    timesstatus.append([])
    for j in range(avgnum[i]):
        timesstatus[i].append([tk.StringVar(master=root, value=""), tk.StringVar(master=root, value="")])

btimesstatus = []
for i in range(len(avgnum)):
    btimesstatus.append([])
    for j in range(avgnum[i]):
        btimesstatus[i].append([tk.StringVar(master=root, value=""), tk.StringVar(master=root, value="")])

guiavgstatus[1][0].grid(row=1, column=0, padx=5, pady=0)
guiavgstatus[1][1].grid(row=2, column=0, padx=5, pady=0)

guiavgstatus[0][0].grid(row=1, column=1, padx=5, pady=0)
guiavgstatus[0][1].grid(row=2, column=1, padx=5, pady=0)

guiavgstatus[2][0].grid(row=1, column=2, padx=5, pady=0)
guiavgstatus[2][1].grid(row=2, column=2, padx=5, pady=0)

scramblevar1 = tk.StringVar(master=root, value='')
scramblelabel1 = tk.Label(root, textvariable=scramblevar1)
scramblelabel1.grid(row=3, column=0, columnspan=3, padx=0, pady=0)

scramblevar2 = tk.StringVar(master=root, value='')
scramblelabel2 = tk.Label(root, textvariable=scramblevar2)
scramblelabel2.grid(row=4, column=0, columnspan=3, padx=0, pady=0)

scramblevar3 = tk.StringVar(master=root, value='')
scramblelabel3 = tk.Label(root, textvariable=scramblevar3)
scramblelabel3.grid(row=5, column=0, columnspan=3, padx=0, pady=0)

scramblevar4 = tk.StringVar(master=root, value='')
scramblelabel4 = tk.Label(root, textvariable=scramblevar4)
scramblelabel4.grid(row=6, column=0, columnspan=3, padx=0, pady=0)


deletebutton = tk.Button(root, text='  Delete  ', command=delete)
deletebutton.grid(row=7, column=0, padx=5, pady=10)

statbutton = tk.Button(root, text='  Status  ', command=stat)
statbutton.grid(row=7, column=1, padx=5, pady=10)

statbackbutton = tk.Button(root, text='   Back   ', command=statback)

nextbutton = tk.Button(root, text='   Next   ', command=nextscramble)
nextbutton.grid(row=7, column=2, padx=5, pady=10)


startbutton = tk.Button(root, text='  Start  ', command=timing)
startbutton.grid(row=8, column=1, padx=5, pady=10)

stopbutton = tk.Button(root, text='  Stop  ', command=stoptiming)


sessionbuttons = []
for i in range(len(sessions)):
    sessionbuttons.append(tk.Button(root, text=sessions[i], command=switchsession(i)))

nextscramble()
calctime()


root.columnconfigure(0, weight=1, uniform='group1')
root.columnconfigure(1, weight=1, uniform='group1')
root.columnconfigure(2, weight=1, uniform='group1')


root.mainloop()