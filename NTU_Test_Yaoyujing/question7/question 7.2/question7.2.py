# coding: utf-8
import numpy
import pandas
#Pure mathematical calculations
def co2inx(x1,x2,t):
    c = t*x2+x1
    return c
input_coordinates_7_2 = pandas.read_csv('input_coordinates_7_2.txt',sep='\t')
L = [4,8,5,9,6,7]
n = len(L)
row = input_coordinates_7_2.shape[1] #6
col = input_coordinates_7_2.shape[0]
I = numpy.zeros([col,row])
data = input_coordinates_7_2.iloc[:, 5]
k = 0
for i in range(5,0,-1):
    print(i)
    x2 = data
    x1 = (input_coordinates_7_2.iloc[:, i-1]).values#Data slice
    data = co2inx(x1,x2,L[i-1])
index = data.to_frame()
index.rename(columns={'x6':'index'},inplace=True)
index.to_csv('output_index_7_2.txt',index=False)
input_index_7_2 = pandas.read_csv('input_index_7_2.txt',sep='\t')
index = input_index_7_2.values
col = input_index_7_2.shape[0]
i_0 = numpy.zeros(col)
data = numpy.zeros((col,n))
for i in range(col):#calculation process
    i_0[0] = index[i]
    data[i,0] = i_0[0]%L[0]
    for j in range(1,6,1):
        i_0[j] = i_0[j-1]//L[j-1]
        data[i,j] = i_0[j]%L[j]
data = data.astype(numpy.int16)
data = pandas.DataFrame(data)
data.columns = ['x1','x2','x3','x4','x5','x6']
data.to_csv('output_coordinates_7_2.txt',index=False,sep='\t')




