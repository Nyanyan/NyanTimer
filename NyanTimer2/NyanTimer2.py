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
import serial

def changesession():
    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    for i in range(3):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    for i in range(scramblerows):
        scramblelabels[i].grid_forget()
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
        
        for i in range(scramblerows):
            scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)
        deletebutton.grid(row=9, column=0, padx=5, pady=10)
        statbutton.grid(row=9, column=1, padx=5, pady=10)
        nextbutton.grid(row=9, column=2, padx=5, pady=10)
        startbutton.grid(row=10, column=1, padx=5, pady=10)

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
        row = ['Number', 'Scramble', 'Single', 'Best Single', 'Best Single No']
        for i in avgnum[1:]:
            row.append('Ao' + str(i))
            row.append('Best Ao' + str(i))
            row.append('Best Ao' + str(i) + ' No')
        writer.writerow(row)
    with open('data'+sessions[session] + '.csv', mode='a') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in range(len(rows) - 1):
            writer.writerow(rows[i])
    calctime()

def stat():
    calctime()
    sessionbutton.grid_forget()
    for i in range(scramblerows):
        scramblelabels[i].grid_forget()
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
    for i in range(scramblerows):
        scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)
    deletebutton.grid(row=9, column=0, padx=5, pady=10)
    statbutton.grid(row=9, column=1, padx=5, pady=10)
    nextbutton.grid(row=9, column=2, padx=5, pady=10)
    startbutton.grid(row=10, column=1, padx=5, pady=10)

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
    scrambles = []
    for i in range(scramblerows):
        scrambles.append('')
    while l < len(scramble) and j < scramblerows:
        i = 65 * (j + 1)
        if i <= len(scramble)-1:
            while scramble[i] != ' ':
                i -= 1
        scrambles[j] = scramble[l:i]
        j += 1
        l = i
    for i in range(scramblerows):
        scramblevars[i].set(scrambles[i])


def timing(tim):
    #global starttime
    #starttime = time.time()
    #print(starttime)

    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    for i in range(3):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    for i in range(scramblerows):
        scramblelabels[i].grid_forget()
    deletebutton.grid_forget()
    statbutton.grid_forget()
    nextbutton.grid_forget()
    startbutton.grid_forget()

    timingvar.set(str(tim))
    timinglabel.grid(row=0, column=1, padx=5, pady=10)
    #stopbutton.grid(row=6, column=1, padx=5, pady=10)

def stoptiming(tim):
    global avgnum, scramble
    exceptpercentage = 5
    #stoptime = time.time()
    #print(stoptime)
    #single = math.floor((stoptime - starttime) * pow(10,3)) / pow(10, 3)
    single = math.floor((tim) * pow(10,3)) / pow(10, 3)
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
    for i in range(scramblerows):
        scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)
    deletebutton.grid(row=9, column=0, padx=5, pady=10)
    statbutton.grid(row=9, column=1, padx=5, pady=10)
    nextbutton.grid(row=9, column=2, padx=5, pady=10)
    startbutton.grid(row=10, column=1, padx=5, pady=10)

    for i in range(30):
        ser.write('y'.encode())
    #stopbutton.grid_forget()
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
                    timesstatus[i][j] = str(round(rows[start + j - 1][2], 3)) + ': ' + rows[start + j - 1][1]
        for i in range(len(avgnum)):
            start = row[3 * i + 4] -avgnum[i] + 1
            if start > 0:
                for j in range(avgnum[i]):
                    btimesstatus[i][j] = str(round(rows[start + j - 1][2], 3)) + ': ' + rows[start + j - 1][1]
    else:
        for i in range(len(avgnum)):
            timestatus[i].set('--.---')
        for i in range(len(avgnum)):
            btimestatus[i].set('--.---')


def viewtime(num):
    def x():
        calctime()
        sessionbutton.grid_forget()
        sessionlabel.grid_forget()
        for i in range(3):
            for j in range(2):
                guiavgstatus[i][j].grid_forget()
        for i in range(scramblerows):
            scramblelabels[i].grid_forget()
        deletebutton.grid_forget()
        statbutton.grid_forget()
        nextbutton.grid_forget()
        startbutton.grid_forget()
        statbackbutton.grid_forget()
        for i in range(len(avgnum)):
            for j in range(2):
                guiavgstatus[i][j].grid_forget()
        for i in range(len(avgnum)):
            for j in range(2):
                guibavgstatus[i][j].grid_forget()

        endviewtimebutton.pack()
        if avgnum[num] == 1:
            viewlabelvar.set("Single " + timestatus[num].get())
        else:
            viewlabelvar.set("Ao" + str(avgnum[num]) + ' ' + timestatus[num].get())
        viewlabel.pack()

        scrollbar_frame.pack_propagate(0)
        scrollbar_frame.grid(row=1, column=0, columnspan=2, rowspan=9, padx=0, pady=0)
        scroll_bary.pack(side=tk.RIGHT,fill=tk.Y)
        scroll_barx.pack(side=tk.TOP,fill=tk.X)
        listbox2.delete(0, 'end')
        for i in range(avgnum[num]):
            listbox2.insert(tk.END, timesstatus[num][i])
        listbox2.pack(fill=tk.BOTH)
    return x

def viewbtime(num):
    def x():
        calctime()
        sessionbutton.grid_forget()
        sessionlabel.grid_forget()
        for i in range(3):
            for j in range(2):
                guiavgstatus[i][j].grid_forget()
        for i in range(scramblerows):
            scramblelabels[i].grid_forget()
        deletebutton.grid_forget()
        statbutton.grid_forget()
        nextbutton.grid_forget()
        startbutton.grid_forget()
        statbackbutton.grid_forget()
        for i in range(len(avgnum)):
            for j in range(2):
                guiavgstatus[i][j].grid_forget()
        for i in range(len(avgnum)):
            for j in range(2):
                guibavgstatus[i][j].grid_forget()

        endviewtimebutton.pack()
        if avgnum[num] == 1:
            viewlabelvar.set("Best Single " + btimestatus[num].get())
        else:
            viewlabelvar.set("Best Ao" + str(avgnum[num]) + ' ' + btimestatus[num].get())
        viewlabel.pack()

        scrollbar_frame.pack_propagate(0)
        scrollbar_frame.grid(row=1, column=0, columnspan=2, rowspan=9, padx=0, pady=0)
        scroll_bary.pack(side=tk.RIGHT,fill=tk.Y)
        scroll_barx.pack(side=tk.TOP,fill=tk.X)
        listbox2.delete(0, 'end')
        for i in range(avgnum[num]):
            listbox2.insert(tk.END, btimesstatus[num][i])
        listbox2.pack(fill=tk.BOTH)
    return x

def endviewtime():
    scrollbar_frame.grid_forget()

    sessionbutton.grid(row=0, column=0, padx=5, pady=0)
    sessionlabel.grid(row=0, column=1, padx=5, pady=0)
    arr = [1, 0, 2]
    for i in range(3):
        for j in range(2):
            guiavgstatus[arr[i]][j].grid(row=j + 1, column=i, padx=5, pady=0)
    for i in range(scramblerows):
        scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)
    deletebutton.grid(row=9, column=0, padx=5, pady=10)
    statbutton.grid(row=9, column=1, padx=5, pady=10)
    nextbutton.grid(row=9, column=2, padx=5, pady=10)
    startbutton.grid(row=10, column=1, padx=5, pady=10)


def mainprocessing():
    line = ser.readline().decode('utf8', 'ignore').rstrip(os.linesep)
    if len(line) == 8:
        flag = True:
        for i in range(1, 7):
            tmp = False
            for j in range(10):
                if line[i] == str(j):
                    tmp = True
            flag = tmp
        if flag:
            checksum = 0
            for i in range(1, 7):
                checksum += int(line[i])
            if chr(checksum) == line[7]:
                status = line[0]
                tim = int(line[1:7])
                print(status, tim)
                if status == ' ':
                    timing(tim)
                    stopflag = True
                elif status == 'S' and stopflag:
                    stoptiming(tim)
                    stopflag = False
    root.after(1,mainprocessing)

ser=serial.Serial('/dev/serial0', 1200, timeout=10)

root= tk.Tk()
root.geometry('320x240')
#root.attributes("-fullscreen", True)

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
session = 0
avgnum = [1, 5, 12, 50, 100, 1000]

for s in sessions:
    if not os.path.isfile('data' + s + '.csv'):
        with open('data' + s + '.csv', mode='x') as f:
            writer = csv.writer(f, lineterminator='\n')
            row = ['Number', 'Scramble', 'Single', 'Best Single', 'Best Single No']
            for i in avgnum[1:]:
                row.append('Ao' + str(i))
                row.append('Best Ao' + str(i))
                row.append('Best Ao' + str(i) + ' No')
            writer.writerow(row)


scramble = ''


stopflag = False


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
        guiavgstatus.append([tk.Label(root, text="Ao"+str(avgnum[i]), font=("",7)), tk.Button(root, textvariable=timestatus[i], command=viewtime(i), font=("",7))])
    if i == 0:
        guiavgstatus.append([tk.Label(root, text="Single", font=("",7)), tk.Button(root, textvariable=timestatus[i], command=viewtime(i), font=("",7))])

btimestatus = []
guibavgstatus = []
for i in range(len(avgnum)):
    btimestatus.append(tk.StringVar(master=root,value="--.---"))
    if i > 0:
        guibavgstatus.append([tk.Label(root, text="Best Ao"+str(avgnum[i]), font=("",7)), tk.Button(root, textvariable=btimestatus[i], command=viewbtime(i), font=("",7))])
    if i == 0:
        guibavgstatus.append([tk.Label(root, text="Best Single", font=("",7)), tk.Button(root, textvariable=btimestatus[i], command=viewbtime(i), font=("",7))])

timesstatus = []
for i in range(len(avgnum)):
    timesstatus.append([])
    for j in range(avgnum[i]):
        timesstatus[i].append('')

btimesstatus = []
for i in range(len(avgnum)):
    btimesstatus.append([])
    for j in range(avgnum[i]):
        btimesstatus[i].append('')

guiavgstatus[1][0].grid(row=1, column=0, padx=5, pady=0)
guiavgstatus[1][1].grid(row=2, column=0, padx=5, pady=0)

guiavgstatus[0][0].grid(row=1, column=1, padx=5, pady=0)
guiavgstatus[0][1].grid(row=2, column=1, padx=5, pady=0)

guiavgstatus[2][0].grid(row=1, column=2, padx=5, pady=0)
guiavgstatus[2][1].grid(row=2, column=2, padx=5, pady=0)

scramblerows = 6
scramblevars = []
for i in range(scramblerows):
    scramblevars.append(tk.StringVar(master=root, value=''))

scramblelabels = []
for i in range(scramblerows):
    scramblelabels.append(tk.Label(root, textvariable=scramblevars[i], font=("",7)))
    scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)

deletebutton = tk.Button(root, text='  Delete  ', command=delete)
deletebutton.grid(row=9, column=0, padx=5, pady=10)

statbutton = tk.Button(root, text='  Status  ', command=stat)
statbutton.grid(row=9, column=1, padx=5, pady=10)

statbackbutton = tk.Button(root, text='   Back   ', command=statback)

nextbutton = tk.Button(root, text='   Next   ', command=nextscramble)
nextbutton.grid(row=9, column=2, padx=5, pady=10)


#startbutton = tk.Button(root, text='  Start  ', command=timing)
#startbutton.grid(row=10, column=1, padx=5, pady=10)

#stopbutton = tk.Button(root, text='  Stop  ', command=stoptiming)

sessionbuttons = []
for i in range(len(sessions)):
    sessionbuttons.append(tk.Button(root, text=sessions[i], command=switchsession(i)))

scrollbar_frame = tk.Frame(root, width=320, height=200)
scrollbar_frame.propagate(False)
listbox2 = tk.Listbox(scrollbar_frame)
scroll_bary =tk.Scrollbar(scrollbar_frame, command=listbox2.yview, orient=tk.VERTICAL)
scroll_barx =tk.Scrollbar(scrollbar_frame, command=listbox2.xview, orient=tk.HORIZONTAL)
endviewtimebutton = tk.Button(scrollbar_frame, text='   Quit   ', command=endviewtime)
viewlabelvar = tk.StringVar(master=scrollbar_frame,value='')
viewlabel = tk.Label(scrollbar_frame, textvariable=viewlabelvar)

timingvar = tk.StringVar(master=root,value='')
timinglabel = tk.Label(root, textvariable=timinglabel)


nextscramble()
calctime()


root.columnconfigure(0, weight=1, uniform='group1')
root.columnconfigure(1, weight=1, uniform='group1')
root.columnconfigure(2, weight=1, uniform='group1')

root.after(1,mainprocessing)
root.mainloop()