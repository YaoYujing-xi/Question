# coding: utf-8
import numpy
import pandas
stage = 1
R,B,n0,n1 = 12,13,12,13

#Generate a L^2 grid and place the beads on the grid
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

#Find the color of the current grid bead, which is different from the color of its left and upper neighbors
def findcolor(color_beads,u_color=-1,l_color=-1):
    maxcolor = -1
    maxcolorNum = 0
    for i in range(len(color_beads)):
        if (i!= u_color and i!= l_color and color_beads[i]>maxcolorNum):
            maxcolor = i
            maxcolorNum = color_beads[i]
    if(maxcolor==-1):
        if(u_color!=-1 and l_color!=-1):
            if(color_beads[u_color]>=color_beads[l_color] and color_beads[u_color]>0):
                maxcolor = u_color
            elif (color_beads[l_color]>0):
                maxcolor = l_color
        elif(u_color==-1 and l_color!=-1):
            if(color_beads[l_color]>0):
                maxcolor = l_color
        elif(u_color!=-1 and l_color==-1):
            if(color_beads[u_color]>0):
                maxcolor = u_color
    return(maxcolor)

if stage <=1:
    color_name = ['R','B','G','W','Y']
    n = [139,1451,977,1072,457]
    L = 64
    beads = coloring(L,n,color_name)
    beads_color_name = numpy.zeros((L,L),dtype=str)
    for i in range(L):
        for j in range(L):
            index = int(beads[i,j])
            beads_color_name[i,j] = color_name[index]
    beads_color_name = pandas.DataFrame(beads_color_name)
    beads_color_name.to_csv('output_question_5_2',index=False,header = False,sep=' ')

if stage<=2:
    color_name = ['R','B']
    n = [12,13]
    L = 5
    beads = coloring(L,n,color_name)
    beads_color_name = numpy.zeros((L,L),dtype=str)
    for i in range(L):
        for j in range(L):
            index = int(beads[i,j])
            beads_color_name[i,j] = color_name[index]
    beads_color_name = pandas.DataFrame(beads_color_name)
    print(beads_color_name)
    beads_color_name.to_csv('output_question_5_1',index=False,header = False,sep=' ')







