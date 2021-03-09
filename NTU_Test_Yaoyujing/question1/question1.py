# coding: utf-8
import pandas as pd
import numpy as np

def drawpath(df1,num_sum,N,m,n):
    for i in range(N):
        steps = main_func(m,n,num_sum[i])
        if (steps != 0):
            StepsStr= ''.join(steps)
            new = pd.DataFrame({'num_sum':num_sum[i],
                                'path':StepsStr},index=[i]  )
            df1 = df1.append(new,ignore_index=True)
        else:
            StepsStr = 'false'
    order = ['num_sum','path']
    df1 = df1[order]
    return df1

def main_func(m,n,num_sum):
    step_count = m+n-2
    path = ['0']*step_count
    s_1 = (1+m)*m//2
    sum_new = num_sum-s_1
    r_step = n-1
    d_step = m-1
    d_s_1 = sum_new//(n-1)-1
    r_s_2 = sum_new%(n-1)
    r_s_1 = r_step-r_s_2
    if(r_s_2>0):
        d_s_2 = 1
    else:
        d_s_2 = 0
    d_s_3 = d_step-d_s_2-d_s_1
    if (d_s_3<0):
        path = 0
        return path
    for i in range(d_s_1):
        path[i] = 'D'
    for i in range(d_s_1, r_s_1+d_s_1):
        path[i] = 'R'
    if(d_s_2==1):
        path[r_s_1+d_s_1] = 'D'
        for i in range(r_s_1+d_s_1+1, r_s_1+d_s_1+1+r_s_2):
            path[i]= 'R'
    for i in range(r_s_1+d_s_1+d_s_2+r_s_2,step_count):
        path[i]= 'D'
    return path
df1 = pd.DataFrame(columns = ['num_sum','path'])
num_sum = [65,72,90,110]
N = len(num_sum)
m = 9
n = 9
df1 = drawpath(df1,num_sum,N,m,n)
df2 = pd.DataFrame(columns = ['num_sum','path'])
num_sum = [87127231192,5994891682]
m = 90000
n = 100000
N = len(num_sum)
df2 = drawpath(df2,num_sum,N,m,n)
df = pd.concat([df1,pd.DataFrame([[np.NaN]*2],columns = df1.columns),df2],ignore_index=True)
df.to_csv('output_question_1',header = False,index=False,sep=' ')