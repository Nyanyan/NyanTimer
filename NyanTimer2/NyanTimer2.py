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

def changesession():
    sessionbutton.grid_forget()
    sessionlabel.grid_forget()
    '''
    ao5label.grid_forget()
    timelabel.grid_forget()
    ao12label.grid_forget()
    ao5numlabel.grid_forget()
    timenumlabel.grid_forget()
    ao12numlabel.grid_forget()
    '''
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
    '''
    button3x3.grid(row=1, column=0, padx=5, pady=5)
    button2x2.grid(row=1, column=1, padx=5, pady=5)
    button4x4.grid(row=1, column=2, padx=5, pady=5)
    button5x5.grid(row=2, column=0, padx=5, pady=5)
    button6x6.grid(row=2, column=1, padx=5, pady=5)
    button7x7.grid(row=2, column=2, padx=5, pady=5)
    button3BLD.grid(row=3, column=0, padx=5, pady=5)
    button3OH.grid(row=3, column=1, padx=5, pady=5)
    buttonClock.grid(row=3, column=2, padx=5, pady=5)
    buttonMega.grid(row=4, column=0, padx=5, pady=5)
    buttonPyra.grid(row=4, column=1, padx=5, pady=5)
    buttonSkewb.grid(row=4, column=2, padx=5, pady=5)
    buttonSquare.grid(row=5, column=0, padx=5, pady=5)
    button4BLD.grid(row=5, column=1, padx=5, pady=5)
    button5BLD.grid(row=5, column=2, padx=5, pady=5)
    '''


def switchsession(num):
    print(num)
    global session
    session = num
    sessionvar.set(sessions[session])

    sessionbutton.grid(row=0, column=0, padx=5, pady=0)
    sessionlabel.grid(row=0, column=1, padx=5, pady=0)
    '''
    ao5label.grid(row=1, column=0, padx=5, pady=0)
    timelabel.grid(row=1, column=1, padx=5, pady=0)
    ao12label.grid(row=1, column=2, padx=5, pady=0)
    ao5numlabel.grid(row=2, column=0, padx=5, pady=0)
    timenumlabel.grid(row=2, column=1, padx=5, pady=0)
    ao12numlabel.grid(row=2, column=2, padx=5, pady=0)
    '''
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
    '''
    button3x3.grid_forget()
    button2x2.grid_forget()
    button4x4.grid_forget()
    button5x5.grid_forget()
    button6x6.grid_forget()
    button7x7.grid_forget()
    button3BLD.grid_forget()
    button3OH.grid_forget()
    buttonClock.grid_forget()
    buttonMega.grid_forget()
    buttonPyra.grid_forget()
    buttonSkewb.grid_forget()
    buttonSquare.grid_forget()
    button4BLD.grid_forget()
    button5BLD.grid_forget()
    '''

    nextscramble()
    calctime()

def delete():
    rows = numpy.asarray(pd.read_csv('data'+sessions[session] + '.csv',header=0))
    #print(rows)
    with open('data'+sessions[session] + '.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['Number', 'Single', 'Best Single', 'Ao5', 'Best Ao5', 'Ao12', 'Best Ao12', 'Ao50', 'Best Ao50', 'Ao100', 'Best Ao100', 'Ao1000', 'Best'])
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
    '''
    ao50label.grid(row=3, column=0, padx=5, pady=0)
    ao100label.grid(row=3, column=1, padx=5, pady=0)
    ao1000label.grid(row=3, column=2, padx=5, pady=0)
    ao50numlabel.grid(row=4, column=0, padx=5, pady=0)
    ao100numlabel.grid(row=4, column=1, padx=5, pady=0)
    ao1000numlabel.grid(row=4, column=2, padx=5, pady=0)

    bestao5label.grid(row=5, column=0, padx=5, pady=0)
    besttimelabel.grid(row=5, column=1, padx=5, pady=0)
    bestao12label.grid(row=5, column=2, padx=5, pady=0)
    bestao5numlabel.grid(row=6, column=0, padx=5, pady=0)
    besttimenumlabel.grid(row=6, column=1, padx=5, pady=0)
    bestao12numlabel.grid(row=6, column=2, padx=5, pady=0)

    bestao50label.grid(row=7, column=0, padx=5, pady=0)
    bestao100label.grid(row=7, column=1, padx=5, pady=0)
    bestao1000label.grid(row=7, column=2, padx=5, pady=0)
    bestao50numlabel.grid(row=8, column=0, padx=5, pady=0)
    bestao100numlabel.grid(row=8, column=1, padx=5, pady=0)
    bestao1000numlabel.grid(row=8, column=2, padx=5, pady=0)
    '''
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
    '''
    ao50label.grid_forget()
    ao100label.grid_forget()
    ao1000label.grid_forget()
    ao50numlabel.grid_forget()
    ao100numlabel.grid_forget()
    ao1000numlabel.grid_forget()

    bestao5label.grid_forget()
    besttimelabel.grid_forget()
    bestao12label.grid_forget()
    bestao5numlabel.grid_forget()
    besttimenumlabel.grid_forget()
    bestao12numlabel.grid_forget()

    bestao50label.grid_forget()
    bestao100label.grid_forget()
    bestao1000label.grid_forget()
    bestao50numlabel.grid_forget()
    bestao100numlabel.grid_forget()
    bestao1000numlabel.grid_forget()
    '''
    
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
    scramble = subprocess.check_output('curl "http://localhost:2014/scramble/.txt?e=' + string[session] + '"', shell=True).decode('utf8', 'ignore').rstrip(os.linesep)
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
    '''
    ao5label.grid_forget()
    timelabel.grid_forget()
    ao12label.grid_forget()
    ao5numlabel.grid_forget()
    timenumlabel.grid_forget()
    ao12numlabel.grid_forget()
    '''
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
    '''
    row1 = []
    rows5 = []
    rows12 = []
    rows50 = []
    rows100 = []
    rows1000 = []
    '''
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
        '''
        if number == 1:
            row1 = rows[0]
        else:
            row1 = rows[number - 1]
        if number >= 4:
            rows5 = rows[number - 4:]
            if number >= 11:
                rows12 = rows[number - 11:]
                if number >= 49:
                    rows50 = rows[number - 49:]
                    if number >= 99:
                        rows100 = rows[number - 99:]
                        if number >= 999:
                            rows1000 = rows[number - 999:]
        '''
        avg = []
        for i in range(len(avgnum) - 1):
            aox = 0
            if len(rowavg[i]) == avgnum[i + 1] - 1:
                times = []
                for j in range(avgnum[i + 1] - 1):
                    times.append(rowavg[i][j][2])
                times.append(single)
                print(times)
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
            newrow = [number + 1, scramble, single, min(single, row1[2])]
            for i in range(1, len(avgnum)):
                newrow.append(avg[i - 1])
                tmp = min(avg[i - 1], row1[2 * i + 2])
                if tmp == 0:
                    tmp = avg[i - 1]
                tmp = round(tmp, 3)
                newrow.append(tmp)
            print(newrow)
            writer.writerow(newrow)
    else:
        with open('data'+sessions[session] + '.csv', mode='a') as f:
            writer = csv.writer(f, lineterminator='\n')
            newrow = [number + 1, scramble, single, single]
            for i in range(1, len(avgnum)):
                for j in range(2):
                    newrow.append(0)
            writer.writerow(newrow)
    '''        
    with open('data'+sessions[session] + '.csv', mode='a') as f:
        writer = csv.writer(f, lineterminator='\n')
        if number >= 1:

            if number >= 4:
                ao5 = 0
                times5 = []
                for i in range(4):
                    times5.append(rows5[i][1])
                times5.append(tmp)
                times5.sort()
                for i in range(1, 4):
                    ao5 += times5[i]
                ao5 = math.floor(ao5 / 3 * pow(10, 3)) / pow(10, 3)
                ao5num.set(ao5)

                if number >= 11:
                    ao12 = 0
                    times12 = []
                    for i in range(11):
                        times12.append(rows12[i][1])
                    times12.append(tmp)
                    times12.sort()
                    for i in range(1, 11):
                        ao12 += times12[i]
                    ao12 = math.floor(ao12 / 10 * pow(10, 3)) / pow(10, 3)
                    ao12num.set(ao12)

                    if number >= 49:
                        ao50 = 0
                        times50 = []
                        for i in range(49):
                            times50.append(rows50[i][1])
                        times50.append(tmp)
                        times50.sort()
                        ex = 3
                        for i in range(ex, 50 - ex):
                            ao50 += times50[i]
                        ao50 = math.floor(ao50 / (50 - 2 * ex) * pow(10, 3)) / pow(10, 3)
                        ao50num.set(ao50)

                        if number >= 99:
                            ao100 = 0
                            times100 = []
                            for i in range(99):
                                times100.append(rows100[i][1])
                            times100.append(tmp)
                            times100.sort()
                            ex = 5
                            for i in range(ex, 100 - ex):
                                ao100 += times100[i]
                            ao100 = math.floor(ao100 / (100 - ex * 2) * pow(10, 3)) / pow(10, 3)
                            ao100num.set(ao100)

                            if number >= 999:
                                ao1000 = 0
                                times1000 = []
                                for i in range(999):
                                    times1000.append(rows1000[i][1])
                                times1000.append(tmp)
                                times1000.sort()
                                ex = 50
                                for i in range(ex, 1000 - ex):
                                    ao1000 += times1000[i]
                                ao1000 = math.floor(ao1000 / (1000 - ex * 2) * pow(10, 3)) / pow(10, 3)
                                ao1000num.set(ao1000)

                                if number == 999:
                                    bsingle = min(tmp, row1[2])
                                    bao5 = min(ao5, row1[4])
                                    bao12 = min(ao12, row1[6])
                                    bao50 = min(ao50, row1[8])
                                    bao100 = min(ao100, row1[10])
                                    writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, bao12, ao50, bao50, ao100, bao100, ao1000, ao1000])
                                    besttimenum.set(bsingle)
                                    bestao5num.set(bao5)
                                    bestao12num.set(bao12)
                                    bestao50num.set(bao50)
                                    bestao100num.set(bao100)
                                    bestao1000num.set(ao1000)
                                else:
                                    bsingle = min(tmp, row1[2])
                                    bao5 = min(ao5, row1[4])
                                    bao12 = min(ao12, row1[6])
                                    bao50 = min(ao50, row1[8])
                                    bao100 = min(ao100, row1[10])
                                    bao1000 = min(ao1000, row1[12])
                                    writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, bao12, ao50, bao50, ao100, bao100, ao1000, bao1000])
                                    besttimenum.set(bsingle)
                                    bestao5num.set(bao5)
                                    bestao12num.set(bao12)
                                    bestao50num.set(bao50)
                                    bestao100num.set(bao100)
                                    bestao1000num.set(bao1000)
                        
                            else:
                                if number == 99:
                                    bsingle = min(tmp, row1[2])
                                    bao5 = min(ao5, row1[4])
                                    bao12 = min(ao12, row1[6])
                                    bao50 = min(ao50, row1[8])
                                    writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, bao12, ao50, bao50, ao100, ao100, 0, 0])
                                    besttimenum.set(bsingle)
                                    bestao5num.set(bao5)
                                    bestao12num.set(bao12)
                                    bestao50num.set(bao50)
                                    bestao100num.set(ao100)
                                else:
                                    bsingle = min(tmp, row1[2])
                                    bao5 = min(ao5, row1[4])
                                    bao12 = min(ao12, row1[6])
                                    bao50 = min(ao50, row1[8])
                                    bao100 = min(ao100, row1[10])
                                    writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, bao12, ao50, bao50, ao100, bao100, 0, 0])
                                    besttimenum.set(bsingle)
                                    bestao5num.set(bao5)
                                    bestao12num.set(bao12)
                                    bestao50num.set(bao50)
                                    bestao100num.set(bao100)

                        else:
                            if number == 49:
                                bsingle = min(tmp, row1[2])
                                bao5 = min(ao5, row1[4])
                                bao12 = min(ao12, row1[6])
                                writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, bao12, ao50, ao50, 0, 0, 0, 0])
                                besttimenum.set(bsingle)
                                bestao5num.set(bao5)
                                bestao12num.set(bao12)
                                bestao50num.set(ao50)
                            else:
                                bsingle = min(tmp, row1[2])
                                bao5 = min(ao5, row1[4])
                                bao12 = min(ao12, row1[6])
                                bao50 = min(ao50, row1[8])
                                writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, bao12, ao50, bao50, 0, 0, 0, 0])
                                besttimenum.set(bsingle)
                                bestao5num.set(bao5)
                                bestao12num.set(bao12)
                                bestao50num.set(bao50)

                    else:
                        if number == 11:
                            bsingle = min(tmp, row1[2])
                            bao5 = min(ao5, row1[4])
                            writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, ao12, 0, 0, 0, 0, 0, 0])
                            besttimenum.set(bsingle)
                            bestao5num.set(bao5)
                            bestao12num.set(ao12)
                        else:
                            bsingle = min(tmp, row1[2])
                            bao5 = min(ao5, row1[4])
                            bao12 = min(ao12, row1[6])
                            writer.writerow([number+1, tmp, bsingle, ao5, bao5, ao12, bao12, 0, 0, 0, 0, 0, 0])
                            besttimenum.set(bsingle)
                            bestao5num.set(bao5)
                            bestao12num.set(bao12)

                else:
                    if number == 4:
                        bsingle = min(tmp, row1[2])
                        writer.writerow([number+1, tmp, bsingle, ao5, ao5, 0, 0, 0, 0, 0, 0, 0, 0])
                        besttimenum.set(bsingle)
                        bestao5num.set(ao5)
                    else:
                        bsingle = min(tmp, row1[2])
                        bao5 = min(ao5, rows5[3][4])
                        writer.writerow([number+1, tmp, bsingle, ao5, bao5, 0, 0, 0, 0, 0, 0, 0, 0])
                        besttimenum.set(bsingle)
                        bestao5num.set(bao5)

            else:
                bsingle = min(tmp, row1[2])
                writer.writerow([number+1, tmp, bsingle, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                besttimenum.set(bsingle)

        else:
            writer.writerow([number+1, tmp, tmp, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            besttimenum.set(tmp)
    '''
    sessionbutton.grid(row=0, column=0, padx=5, pady=0)
    sessionlabel.grid(row=0, column=1, padx=5, pady=0)
    '''
    ao5label.grid(row=1, column=0, padx=5, pady=0)
    timelabel.grid(row=1, column=1, padx=5, pady=0)
    ao12label.grid(row=1, column=2, padx=5, pady=0)
    ao5numlabel.grid(row=2, column=0, padx=5, pady=0)
    timenumlabel.grid(row=2, column=1, padx=5, pady=0)
    ao12numlabel.grid(row=2, column=2, padx=5, pady=0)
    '''
    arr = [1, 0, 2]
    for i in range(3):
        for j in range(2):
            guiavgstatus[arr[i]][j].grid(row=j + 1, column=i, padx=5, pady=0)
    '''
    guiavgstatus[1][1].grid(row=2, column=0, padx=5, pady=0)
    guiavgstatus[0][0].grid(row=1, column=1, padx=5, pady=0)
    guiavgstatus[0][1].grid(row=2, column=1, padx=5, pady=0)
    guiavgstatus[2][0].grid(row=1, column=2, padx=5, pady=0)
    guiavgstatus[2][1].grid(row=2, column=2, padx=5, pady=0)
    '''

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
            if row[2 * i + 2] > 0:
                timestatus[i].set(row[2 * i + 2])
                btimestatus[i].set(row[2 * i + 3])
            else:
                timestatus[i].set('--.---')
                btimestatus[i].set('--.---')
        '''
        timenum.set(row[1])
        besttimenum.set(row[2])
        if row[3] != 0:
            ao5num.set(row[3])
            bestao5num.set(row[4])
        if row[5] != 0:
            ao12num.set(row[5])
            bestao12num.set(row[6])
        if row[7] != 0:
            ao50num.set(row[7])
            bestao50num.set(row[8])
        if row[9] != 0:
            ao100num.set(row[9])
            bestao100num.set(row[10])
        if row[11] != 0:
            ao1000num.set(row[11])
            bestao1000num.set(row[12])
        '''
    else:
        for i in range(len(avgnum)):
            timestatus[i].set('--.---')
        for i in range(len(avgnum)):
            btimestatus[i].set('--.---')
        '''
        timenum.set('--.---')
        besttimenum.set('--:---')
        ao5num.set('--.---')
        bestao5num.set('--.---')
        ao12num.set('--.---')
        bestao12num.set('--.---')
        ao50num.set('--.---')
        bestao50num.set('--.---')
        ao100num.set('--.---')
        bestao100num.set('--.---')
        ao1000num.set('--.---')
        bestao1000num.set('--.---')
        '''


def viewtime(num):
    return 0

def viewbtime(num):
    return 0

root= tk.Tk()
root.geometry('320x240')

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
session = 0
avgnum = [1, 5, 12, 50, 100, 1000]

for s in sessions:
    if not os.path.isfile('data' + s + '.csv'):
        with open('data' + s + '.csv', mode='x') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['Number', 'Scramble', 'Single', 'Best Single', 'Ao5', 'Best Ao5', 'Ao12', 'Best Ao12', 'Ao50', 'Best Ao50', 'Ao100', 'Best Ao100', 'Ao1000', 'Best Ao1000'])


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
        guiavgstatus.append([tk.Label(root, text="Ao"+str(avgnum[i])), tk.Button(root, textvariable=timestatus[i], command=lambda: viewtime(i))])
    if i == 0:
        guiavgstatus.append([tk.Label(root, text="Single"), tk.Button(root, textvariable=timestatus[i], command=lambda: viewtime(i))])

btimestatus = []
guibavgstatus = []
for i in range(len(avgnum)):
    btimestatus.append(tk.StringVar(master=root,value="--.---"))
    if i > 0:
        guibavgstatus.append([tk.Label(root, text="Best Ao"+str(avgnum[i])), tk.Button(root, textvariable=btimestatus[i], command=lambda: viewbtime(i))])
    if i == 0:
        guibavgstatus.append([tk.Label(root, text="Best Single"), tk.Button(root, textvariable=btimestatus[i], command=lambda: viewbtime(i))])

guiavgstatus[1][0].grid(row=1, column=0, padx=5, pady=0)
guiavgstatus[1][1].grid(row=2, column=0, padx=5, pady=0)

guiavgstatus[0][0].grid(row=1, column=1, padx=5, pady=0)
guiavgstatus[0][1].grid(row=2, column=1, padx=5, pady=0)

guiavgstatus[2][0].grid(row=1, column=2, padx=5, pady=0)
guiavgstatus[2][1].grid(row=2, column=2, padx=5, pady=0)

'''
ao5label = tk.Label(root, text="Ao5")
ao5label.grid(row=1, column=0, padx=5, pady=0)

timelabel = tk.Label(root, text="Single")
timelabel.grid(row=1, column=1, padx=5, pady=0)

ao12label = tk.Label(root, text="Ao12")
ao12label.grid(row=1, column=2, padx=5, pady=0)

ao50label = tk.Label(root, text="Ao50")

ao100label = tk.Label(root, text="Ao100")

ao1000label = tk.Label(root, text="Ao1000")


ao5num = tk.StringVar(master=root,value="-.---")
ao5numlabel = tk.Label(root, textvariable=ao5num)
ao5numlabel.grid(row=2, column=0, padx=5, pady=0)

timenum = tk.StringVar(master=root,value="-.---")
timenumlabel = tk.Label(root, textvariable=timenum)
timenumlabel.grid(row=2, column=1, padx=5, pady=0)

ao12num = tk.StringVar(master=root,value="-.---")
ao12numlabel = tk.Label(root, textvariable=ao12num)
ao12numlabel.grid(row=2, column=2, padx=5, pady=0)

ao50num = tk.StringVar(master=root,value="-.---")
ao50numlabel = tk.Label(root, textvariable=ao50num)

ao100num = tk.StringVar(master=root,value="-.---")
ao100numlabel = tk.Label(root, textvariable=ao100num)

ao1000num = tk.StringVar(master=root,value="-.---")
ao1000numlabel = tk.Label(root, textvariable=ao1000num)


bestao5label = tk.Label(root, text="Best Ao5")

besttimelabel = tk.Label(root, text="Best Single")

bestao12label = tk.Label(root, text="Best Ao12")

bestao50label = tk.Label(root, text="Best Ao50")

bestao100label = tk.Label(root, text="Best Ao100")

bestao1000label = tk.Label(root, text="Best Ao1000")


bestao5num = tk.StringVar(master=root,value="-.---")
bestao5numlabel = tk.Label(root, textvariable=bestao5num)

besttimenum = tk.StringVar(master=root,value="-.---")
besttimenumlabel = tk.Label(root, textvariable=besttimenum)

bestao12num = tk.StringVar(master=root,value="-.---")
bestao12numlabel = tk.Label(root, textvariable=bestao12num)

bestao50num = tk.StringVar(master=root,value="-.---")
bestao50numlabel = tk.Label(root, textvariable=bestao50num)

bestao100num = tk.StringVar(master=root,value="-.---")
bestao100numlabel = tk.Label(root, textvariable=bestao100num)

bestao1000num = tk.StringVar(master=root,value="-.---")
bestao1000numlabel = tk.Label(root, textvariable=bestao1000num)
'''

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
    sessionbuttons.append(tk.Button(root, text=sessions[i], command=lambda:switchsession(i)))
'''
button3x3 = tk.Button(root, text='3x3', command=lambda :switchsession(0))
button2x2 = tk.Button(root, text='2x2', command=lambda :switchsession(1))
button4x4 = tk.Button(root, text='4x4', command=lambda :switchsession(2))
button5x5 = tk.Button(root, text='5x5', command=lambda :switchsession(3))
button6x6 = tk.Button(root, text='6x6', command=lambda :switchsession(4))
button7x7 = tk.Button(root, text='7x7', command=lambda :switchsession(5))
button3BLD = tk.Button(root, text='3BLD', command=lambda :switchsession(6))
button3OH = tk.Button(root, text='3OH', command=lambda :switchsession(7))
buttonClock = tk.Button(root, text='Clock', command=lambda :switchsession(8))
buttonMega = tk.Button(root, text='Megaminx', command=lambda :switchsession(9))
buttonPyra = tk.Button(root, text='Pyraminx', command=lambda :switchsession(10))
buttonSkewb = tk.Button(root, text='Skewb', command=lambda :switchsession(11))
buttonSquare = tk.Button(root, text='Square-1', command=lambda :switchsession(12))
button4BLD = tk.Button(root, text='4BLD', command=lambda :switchsession(13))
button5BLD = tk.Button(root, text='5BLD', command=lambda :switchsession(14))
'''

nextscramble()
calctime()


root.columnconfigure(0, weight=1, uniform='group1')
root.columnconfigure(1, weight=1, uniform='group1')
root.columnconfigure(2, weight=1, uniform='group1')


root.mainloop()