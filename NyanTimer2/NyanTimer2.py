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
import psutil

def float2str(num):
    vals = []
    num = round(num, 3)
    vals.append(int(num // 60))
    vals.append(int(num - vals[0] * 60) // 10)
    vals.append(int(num - vals[0] * 60) - vals[1] * 10)
    vals.append(int((num - int(num)) * 10))
    vals.append(int((num - int(num)) * 100) - vals[3] * 10)
    vals.append(int((num - int(num)) * 1000) - vals[3] * 100 - vals[4] * 10)
    #print(num, vals)
    for i in range(len(vals)):
        vals[i] = str(vals[i])
    ans = vals[0] + ':' + vals[1] + vals[2] + '.' + vals[3] + vals[4] + vals[5]
    return ans

def deg(num, n):
    res = str(num)
    for i in range(n - len(res)):
        res = '0' + res
    return res

def changesession():
    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    inspbutton.grid_forget()
    #insplabel.grid_forget()
    for i in range(3):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    for i in range(scramblerows):
        scramblelabels[i].grid_forget()
    deletebutton.grid_forget()
    statbutton.grid_forget()
    nextbutton.grid_forget()
    #startbutton.grid_forget()

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
        stopinspection()
        inspbutton.grid(row=0, column=2, padx=5, pady=0)
        nextbutton.grid(row=9, column=2, padx=5, pady=10)
        #startbutton.grid(row=10, column=1, padx=5, pady=10)

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
    inspbutton.grid_forget()
    #insplabel.grid_forget()
    for i in range(scramblerows):
        scramblelabels[i].grid_forget()
    deletebutton.grid_forget()
    statbutton.grid_forget()
    nextbutton.grid_forget()
    #startbutton.grid_forget()

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
    stopinspection()
    inspbutton.grid(row=0, column=2, padx=5, pady=0)
    for i in range(scramblerows):
        scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)
    deletebutton.grid(row=9, column=0, padx=5, pady=10)
    statbutton.grid(row=9, column=1, padx=5, pady=10)
    nextbutton.grid(row=9, column=2, padx=5, pady=10)
    #startbutton.grid(row=10, column=1, padx=5, pady=10)

    for i in range(3, len(avgnum)):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    for i in range(len(avgnum)):
        for j in range(2):
            guibavgstatus[i][j].grid_forget()
    
def nextscramble():
    global scramble
    string = ['333', '222', '444', '555', '666', '777', '333ni', '333', 'clock', 'minx', 'pyram', 'skewb', 'sq1', '444ni', '555ni']
    response = urllib.request.urlopen('http://localhost:2014/scramble/.txt?e=' + string[session])
    scramble = response.read().decode('utf8', 'ignore').rstrip(os.linesep)
    scramble = ''.join(scramble.splitlines())
    response.close()
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


def timing():
    #global starttime
    #starttime = time.time()
    #print(starttime)

    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    #insplabel.grid_forget()
    inspbutton.grid_forget()
    for i in range(3):
        for j in range(2):
            guiavgstatus[i][j].grid_forget()
    for i in range(scramblerows):
        scramblelabels[i].grid_forget()
    deletebutton.grid_forget()
    statbutton.grid_forget()
    nextbutton.grid_forget()
    #startbutton.grid_forget()
    labelvar = tim[0] + ':' + tim[1:3] + '.' + tim[3:6]
    timingvar.set(labelvar)
    timinglabel.grid(row=0, column=1, padx=5, pady=10)
    #stopbutton.grid(row=6, column=1, padx=5, pady=10)

def stoptiming():
    global avgnum, scramble, inspectiontime, plus2flag, dnfflag
    exceptpercentage = 5
    #stoptime = time.time()
    #print(stoptime)
    #single = math.floor((stoptime - starttime) * pow(10,3)) / pow(10, 3)
    tmp = [int(tim[0]), int(tim[1:3]), int(tim[3:6])]
    print(tmp)
    if plus2flag:
        tmp[1] += 2
        if tmp[1] >= 60:
            tmp[1] -= 60
            tmp[0] += 1
    single = str(tmp[0]) + ':' + deg(tmp[1], 2) + '.' + deg(tmp[2], 3)
    if dnfflag:
        single = 'DNF'
    print(single)
    #timenum.set(str(tmp))
    timestatus[0].set(single)
    rows = numpy.asarray(pd.read_csv('data'+sessions[session] + '.csv', header=0))
    number = len(rows)
    usedinsp = 15 - inspectiontime
    #print(number)
    if number >= 1:
        #f = open('data'+sessions[session] + '.csv', 'r')
        #f.close()
        row1 = []
        for i in range(len(rows[number - 1])):
            row1.append(rows[number - 1][i])
        rowavg = []
        for i in avgnum[1:]:
            rowavg.append(rows[max(0, number - i + 1):])
        for i in range(2, len(row1)):
            if i % 3 != 1 and row1[i] != 'DNF':
                row1[i] = float(int(row1[i][0]) * 60 + int(row1[i][2]) * 10 + int(row1[i][3]) + int(row1[i][5]) / 10 + int(row1[i][6]) / 100 + int(row1[i][7]) / 1000)
        avg = []
        for i in range(len(avgnum) - 1):
            aox = 0
            if len(rowavg[i]) == avgnum[i + 1] - 1:
                times = []
                for j in range(avgnum[i + 1] - 1):
                    if rowavg[i][j][2] != 'DNF':
                        timtmp = round(float(int(rowavg[i][j][2][0]) * 60 + int(rowavg[i][j][2][2:4]) + int(rowavg[i][j][2][5:8]) / 1000), 3)
                        times.append(timtmp)
                if single != 'DNF':
                    times.append(float(int(single[0]) * 60 + int(single[2:4]) + int(single[5:8]) / 1000))
                #print(times)
                exceptnum = math.ceil(avgnum[i + 1] * exceptpercentage / 100)
                if len(times) >= avgnum[i + 1] - exceptnum:
                    times.sort()
                    #print(times, avgnum[i + 1])
                    for j in range(exceptnum, avgnum[i + 1] - exceptnum):
                        aox += times[j]
                    aox /= avgnum[i + 1] - 2 * exceptnum
                    aox = math.floor(aox * 1000) / 1000
                    aox = round(aox, 3)
                    aoxstr = float2str(aox)
                else:
                    aoxstr = 'DNF'
                timestatus[i + 1].set(aoxstr)
            avg.append(aox)
        #print(avg)
        with open('data'+sessions[session] + '.csv', mode='a') as f:
            writer = csv.writer(f, lineterminator='\n')
            no = row1[4]
            singletime = round(float(int(tim[0]) * 60 + int(tim[1]) * 10 + int(tim[2]) + int(tim[3]) / 10 + int(tim[4]) / 100 + int(tim[5]) / 1000), 3)
            if singletime < row1[3]:
                no = number + 1
            if singletime < row1[3]:
                bsingle = single
            else:
                bsingle = str(rows[number - 1][3])
            #print('bsingle', bsingle)
            newrow = [number + 1, scramble, usedinsp, single, bsingle, no]
            for i in range(1, len(avgnum)):
                avgstr = float2str(avg[i - 1])
                newrow.append(avgstr)
                if row1[3 * i + 3] == '0:00.000':
                    formerpb = 0
                else:
                    formerpb = row1[3 * i + 3]
                pb = min(avg[i - 1], formerpb)
                if pb == 0:
                    pb = avg[i - 1]
                no = row1[3 * i + 4]
                pb = round(pb, 3)
                if pb == avg[i - 1] and pb != formerpb:
                    no = number + 1
                pbstr = float2str(pb)
                newrow.append(pbstr)
                newrow.append(no)
            #print(newrow)
            writer.writerow(newrow)
    else:
        with open('data'+sessions[session] + '.csv', mode='a') as f:
            writer = csv.writer(f, lineterminator='\n')
            newrow = [number + 1, scramble, usedinsp, single, single, number + 1]
            for i in range(1, len(avgnum)):
                for j in range(2):
                    newrow.append('0:00.000')
                newrow.append(0)
            writer.writerow(newrow)
    timinglabel.grid_forget()
    sessionbutton.grid(row=0, column=0, padx=5, pady=0)
    sessionlabel.grid(row=0, column=1, padx=5, pady=0)
    inspbutton.grid(row=0, column=2, padx=5, pady=0)
    guiavgstatus[0][0].grid(row=1, column=1, padx=5, pady=0)
    guiavgstatus[0][1].grid(row=2, column=1, padx=5, pady=0)
    for i in range(scramblerows):
        scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)
    deletebutton.grid(row=9, column=0, padx=5, pady=10)
    statbutton.grid(row=9, column=1, padx=5, pady=10)
    nextbutton.grid(row=9, column=2, padx=5, pady=10)
    #startbutton.grid(row=10, column=1, padx=5, pady=10)

    for i in range(30):
        ser.write('y'.encode())
        #print('y')
    #stopbutton.grid_forget()
    if not plus2flag and not dnfflag:
        nextscramble()
    plus2flag = False
    dnfflag = False

def calctime():
    rows = numpy.asarray(pd.read_csv('data'+sessions[session] + '.csv', header=0))
    number = len(rows)
    mem = psutil.virtual_memory() 
    print('memory used', mem.percent, '%')
    if number > 0:
        row = rows[-1]
        #print(row)
        for i in range(3, len(row)):
            if i % 3 != 1 and row[i] != 'DNF':
                row[i] = float(int(row[i][0]) * 60 + int(row[i][2]) * 10 + int(row[i][3]) + int(row[i][5]) / 10 + int(row[i][6]) / 100 + int(row[i][7]) / 1000)
        for i in range(3, number):
            if row[i] != 'DNF':
                row[i] = round(row[i], 3)
        for i in range(len(avgnum)):
            if row[3 * i + 3] > 0:
                timestatus[i].set(row[3 * i + 3])
                btimestatus[i].set(row[3 * i + 4])
            else:
                timestatus[i].set('--.---')
                btimestatus[i].set('--.---')
        for i in range(len(avgnum)):
            start = number - avgnum[i] + 1
            if start > 0:
                for j in range(avgnum[i]):
                    timesstatus[i][j] = str(rows[start + j - 1][3]) + ': ' + rows[start + j - 1][0]
        for i in range(len(avgnum)):
            start = row[3 * i + 4] -avgnum[i] + 1
            if start > 0:
                for j in range(avgnum[i]):
                    btimesstatus[i][j] = str(rows[start + j - 1][3]) + ': ' + rows[start + j - 1][0]
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
        inspbutton.grid_forget()
        #insplabel.grid_forget()
        for i in range(3):
            for j in range(2):
                guiavgstatus[i][j].grid_forget()
        for i in range(scramblerows):
            scramblelabels[i].grid_forget()
        deletebutton.grid_forget()
        statbutton.grid_forget()
        nextbutton.grid_forget()
        #startbutton.grid_forget()
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
        inspbutton.grid_forget()
        #insplabel.grid_forget()
        for i in range(3):
            for j in range(2):
                guiavgstatus[i][j].grid_forget()
        for i in range(scramblerows):
            scramblelabels[i].grid_forget()
        deletebutton.grid_forget()
        statbutton.grid_forget()
        nextbutton.grid_forget()
        #startbutton.grid_forget()
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
    stopinspection()
    inspbutton.grid(row=0, column=2, padx=5, pady=0)
    arr = [1, 0, 2]
    for i in range(3):
        for j in range(2):
            guiavgstatus[arr[i]][j].grid(row=j + 1, column=i, padx=5, pady=0)
    for i in range(scramblerows):
        scramblelabels[i].grid(row=3+i, column=0, columnspan=3, padx=0, pady=0)
    deletebutton.grid(row=9, column=0, padx=5, pady=10)
    statbutton.grid(row=9, column=1, padx=5, pady=10)
    nextbutton.grid(row=9, column=2, padx=5, pady=10)
    #startbutton.grid(row=10, column=1, padx=5, pady=10)

def startinspection():
    global inspectiontime, inspflag
    inspectiontime = 15
    inspvar.set('15')
    #inspbutton.grid_forget()
    #insplabel.grid(row=0, column=2, padx=5, pady=0)
    inspflag = True
    root.after(1000, inspection)

def stopinspection():
    global inspflag
    inspflag = False

def inspection():
    global inspectiontime, inspflag
    if inspectiontime > -3:
        inspectiontime -= 1
    if inspectiontime > 0:
        inspvar.set(str(inspectiontime))
    elif -2 < inspectiontime <= 0:
        inspvar.set('+2')
    else:
        inspvar.set('DNF')
    if inspectiontime == 7:
        os.system("aplay --quiet '8sec.wav' &")
    elif inspectiontime == 3:
        os.system("aplay --quiet '12sec.wav' &")
    if inspflag:
        root.after(1000, inspection)

def plus2():
    global plus2flag
    plus2flag = True
    stoptiming()

def dnf():
    global dnfflag
    dnfflag = True
    stoptiming()

def mainprocessing():
    global stopflag, tim
    line = ser.readline().decode('utf8', 'ignore').rstrip(os.linesep)[1:]
    if len(line) == 8:
        flag = True
        for i in range(1, 7):
            flag = False
            for j in range(10):
                if line[i] == str(j):
                    flag = True
            if not flag:
                break
        if flag:
            checksum = 64
            for i in range(1, 7):
                checksum += int(line[i])
            if chr(checksum) == line[7]:
                status = line[0]
                if line[1:7] != '000000':
                    tim = line[1:7] 
                #print(status, tim)
                if status == ' ':
                    stopinspection()
                    timing()
                    stopflag = True
                elif status == 'S' and stopflag:
                    stoptiming()
                    stopflag = False
    root.after(100,mainprocessing)

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

inspectiontime = 15
inspflag = False
dnfflag = False
plus2flag = False
tim = '000000'


sessionbutton = tk.Button(root, text='Session', command=changesession)
sessionbutton.grid(row=0, column=0, padx=5, pady=0)


sessionvar = tk.StringVar(master=root,value=sessions[session])
sessionlabel = tk.Label(root, textvariable=sessionvar)
sessionlabel.grid(row=0, column=1, padx=5, pady=0)

inspvar = tk.StringVar(master=root,value='15')
inspbutton = tk.Button(root, textvariable=inspvar, command=startinspection)
inspbutton.grid(row=0, column=2, padx=5, pady=0)
#insplabel = tk.Label(root, textvariable=inspvar)

timestatus = [tk.StringVar(master=root,value="--.---") for _ in range(len(avgnum))]
guiavgstatus = []
for i in range(len(avgnum)):
    if i > 0:
        guiavgstatus.append([tk.Label(root, text="Ao"+str(avgnum[i]), font=("",7)), tk.Button(root, textvariable=timestatus[i], command=viewtime(i), font=("",7))])
    if i == 0:
        guiavgstatus.append([tk.Label(root, text="Single", font=("",7)), tk.Button(root, textvariable=timestatus[i], command=viewtime(i), font=("",7))])

btimestatus = [tk.StringVar(master=root,value="--.---") for _ in range(len(avgnum))]
guibavgstatus = []
for i in range(len(avgnum)):
    if i > 0:
        guibavgstatus.append([tk.Label(root, text="Best Ao"+str(avgnum[i]), font=("",7)), tk.Button(root, textvariable=btimestatus[i], command=viewbtime(i), font=("",7))])
    if i == 0:
        guibavgstatus.append([tk.Label(root, text="Best Single", font=("",7)), tk.Button(root, textvariable=btimestatus[i], command=viewbtime(i), font=("",7))])

timesstatus = [['' for _ in range(avgnum[i])] for i in range(len(avgnum))]

btimesstatus = [['' for _ in range(avgnum[i])] for i in range(len(avgnum))]

plus2button = tk.Button(root, text='+2', command=plus2)
plus2button.grid(row=2, column=0, padx=5, pady=0)

#guiavgstatus[1][0].grid(row=1, column=0, padx=5, pady=0)
#guiavgstatus[1][1].grid(row=2, column=0, padx=5, pady=0)

guiavgstatus[0][0].grid(row=1, column=1, padx=5, pady=0)
guiavgstatus[0][1].grid(row=2, column=1, padx=5, pady=0)

dnfbutton = tk.Button(root, text='DNF', command=plus2)
dnfbutton.grid(row=2, column=2, padx=5, pady=0)

#guiavgstatus[2][0].grid(row=1, column=2, padx=5, pady=0)
#guiavgstatus[2][1].grid(row=2, column=2, padx=5, pady=0)

scramblerows = 6
scramblevars = [tk.StringVar(master=root, value='') for i in range(scramblerows)]

scramblelabels = [tk.Label(root, textvariable=scramblevars[i], font=("",7)) for i in range(scramblerows)]
for i in range(scramblerows):
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

sessionbuttons = [tk.Button(root, text=sessions[i], command=switchsession(i)) for i in range(len(sessions))]

scrollbar_frame = tk.Frame(root, width=320, height=200)
scrollbar_frame.propagate(False)
listbox2 = tk.Listbox(scrollbar_frame)
scroll_bary =tk.Scrollbar(scrollbar_frame, command=listbox2.yview, orient=tk.VERTICAL)
scroll_barx =tk.Scrollbar(scrollbar_frame, command=listbox2.xview, orient=tk.HORIZONTAL)
endviewtimebutton = tk.Button(scrollbar_frame, text='   Quit   ', command=endviewtime)
viewlabelvar = tk.StringVar(master=scrollbar_frame,value='')
viewlabel = tk.Label(scrollbar_frame, textvariable=viewlabelvar)

timingvar = tk.StringVar(master=root,value='')
timinglabel = tk.Label(root, textvariable=timingvar)


nextscramble()
calctime()


root.columnconfigure(0, weight=1, uniform='group1')
root.columnconfigure(1, weight=1, uniform='group1')
root.columnconfigure(2, weight=1, uniform='group1')

root.after(100,mainprocessing)
root.mainloop()