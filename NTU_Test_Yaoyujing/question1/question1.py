def findPath(arr,x,y,sum,path):
    global n,m,required_sum
    if x==n-1 and y==m-1:
        if sum+arr[x][y] ==required_sum:
            return path
        else:
            return 0
    if sum >required_sum:
        return 0
    if x<n-1:
        ans = findPath(arr,x+1,y,sum+arr[x][y],path+'D')
        if ans!=0:
            return ans
    if y<m-1:
        ans = findPath(arr,x,y+1,sum+arr[x][y],path+'R')
        if ans!=0:
            return ans
    return 0
from tqdm import tqdm
stage = 1
if stage ==1:
    arr = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
    sum = 0
    required_sum = 13
    n,m = 4,4
    x,y=0,0
    path = ''
    ans = findPath(arr,x,y,sum,path)
    if ans!=0:
        print(ans)
    else:
        print('no ans')
if stage ==2:
    import sys
    sys.setrecursionlimit(1000000000)
    sum = 0
    required_sum = 87127231192
    n,m = 90000,100000
    x,y=0,0
    arr = [[i]*n for i in tqdm(range(m))]
    path = ''
    ans = findPath(arr,x,y,sum,path)
    with open('res_87.txt','w') as f:
        f.writelines(ans)
    required_sum = 5994891682
    path = ''
    ans = findPath(arr,x,y,sum,path)
    with open('res_599.txt','w') as f:
        f.writelines(ans)

    if ans!=0:
        print(ans)
    else:
        print('no ans')
