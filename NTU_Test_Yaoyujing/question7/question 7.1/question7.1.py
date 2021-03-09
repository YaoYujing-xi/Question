# coding: utf-8
import numpy
import pandas
def co2inx(x1,x2,t):
    c = t*x2+x1
    return c
input_coordinates_7_1 = pandas.read_csv('input_coordinates_7_1.txt',sep='\t')
L = [50,57]
n = len(L)
row ,col = input_coordinates_7_1.shape[1] ,input_coordinates_7_1.shape[0]
I,data,k= numpy.zeros([col,row]),input_coordinates_7_1.iloc[:, 1], 0
for i in range(1,2):
    print(i)
    x2 = data
    x1 = (input_coordinates_7_1.iloc[:, i-1]).values
    data = co2inx(x1,x2,L[i-1])
index = data.to_frame()
index.rename(columns={'x2':'index'},inplace=True)
index.to_csv( 'output_index_7_1.txt',index=False)
input_index_7_1 = pandas.read_csv('input_index_7_1.txt',sep='\t')
index = input_index_7_1.values
col = input_index_7_1.shape[0] #30240
I0 = numpy.zeros(col)
data = numpy.zeros((col,n))
for i in range(col):
    I0[0] = index[i]
    data[i,0] = I0[0]%L[0]
    I0[1] = I0[0]//L[0]
    data[i,1] = I0[1]%L[1]
data = data.astype(numpy.int16)
data = pandas.DataFrame(data)
data.columns = ['x1','x2']
data.to_csv('output_coordinates_7_1.txt',index=False,sep='\t')

