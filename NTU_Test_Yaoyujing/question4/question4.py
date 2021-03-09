# coding: utf-8
import pandas
import numpy
inp = pandas.read_csv('input_question_4',sep='\t',header=None).values
m ,n = len(inp[:,1]),len(inp[1,:])
m0 ,n0,label= 5,4,1
example_matrix = numpy.array([[0,0,1,1],[1,1,0,0],[0,0,0,0], [0,1,1,0],[0,1,1,1]])
for j in range(n):
    for i in range(m):
        if (inp[i,j] == 1):
            inp[i,j] = -1

#For a given image s, 0 means background, -1 means non-background,
#For candidate pixels, s_i_j, find the component that connects it and mark its index
def fill_img(s,i,j,index):
    if (s[i,j]==-1):
        s[i,j] = index
        if(i-1>=0 and s[i-1,j]==-1):
            fill_img(s,i-1,j,index)
        if(i+1<=m-1and s[i+1,j]==-1):
            fill_img(s,i+1,j,index)
        if(j-1>=0 and s[i,j-1]==-1):
            fill_img(s,i,j-1,index)
        if(j+1<=n-1and s[i,j+1]==-1):
            fill_img(s,i,j+1,index)
    return
#Change the pixel value from 1 to -1 for easy labeling
for j in range(n):
    for i in range(m):
        if (inp[i,j]==-1):
            fill_img(inp,i,j,label)
            label = label+1
a = pandas.DataFrame(inp)
a.to_csv('output_question_4', sep=' ',index=False,header=None)



