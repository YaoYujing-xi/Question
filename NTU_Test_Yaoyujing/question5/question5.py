# coding: utf-8
import numpy
import pandas
stage = 1
R,B,n0,n1 = 12,13,12,13
def coloring(L,n,color_name):
    beads = numpy.zeros((L,L),dtype = int)
    for i in range(L):
        for j in range(L):
            if(i==0 and j==0):
                color = findcolor(n)
            elif (i==0 and j>0):
                color = findcolor(n, -1, beads[i,j-1])
            elif (i>0 and j==0):
                color = findcolor(n, beads[i-1,j], -1)
            else:
                color = findcolor(n, beads[i-1,j], beads[i,j-1])
            if (color!=-1):
                beads[i,j] = color
                n[color] = n[color]-1
    return(beads)

def findcolor(colorBeads,Upcolor=-1,Leftcolor=-1):
    maxcolor = -1
    maxcolorNum = 0
    for i in range(len(colorBeads)):
        if (i!= Upcolor and i!= Leftcolor and colorBeads[i]>maxcolorNum):
            maxcolor = i
            maxcolorNum = colorBeads[i]
    if(maxcolor==-1):
        if(Upcolor!=-1 and Leftcolor!=-1):
            if(colorBeads[Upcolor]>=colorBeads[Leftcolor] and colorBeads[Upcolor]>0):
                maxcolor = Upcolor
            elif (colorBeads[Leftcolor]>0):
                maxcolor = Leftcolor
        elif(Upcolor==-1 and Leftcolor!=-1):
            if(colorBeads[Leftcolor]>0):
                maxcolor = Leftcolor
        elif(Upcolor!=-1 and Leftcolor==-1):
            if(colorBeads[Upcolor]>0):
                maxcolor = Upcolor
    return(maxcolor)
if stage <=1:
    color_name = ['R','B','G','W','Y']
    n = [139,1451,977,1072,457]
    L = 64
    Beads = coloring(L,n,color_name)
    Beadscolor_name = numpy.zeros((L,L),dtype=str)
    for i in range(L):
        for j in range(L):
            index = int(Beads[i,j])
            Beadscolor_name[i,j] = color_name[index]
    Beadscolor_name = pandas.DataFrame(Beadscolor_name)
    Beadscolor_name.to_csv('output_question_5_2',index=False,header = False,sep=' ')

if stage<=2:
    color_name = ['R','B']
    n = [12,13]
    L = 5
    Beads = coloring(L,n,color_name)
    Beadscolor_name = numpy.zeros((L,L),dtype=str)
    for i in range(L):
        for j in range(L):
            index = int(Beads[i,j])
            Beadscolor_name[i,j] = color_name[index]
    Beadscolor_name = pandas.DataFrame(Beadscolor_name)
    print(Beadscolor_name)
    Beadscolor_name.to_csv('output_question_5_1',index=False,header = False,sep=' ')







