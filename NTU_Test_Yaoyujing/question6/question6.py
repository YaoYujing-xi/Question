# -*- coding: utf-8 -*-
import os
max_num = 10000
#The given points form a polygon; take the point to be judged as the vertex to make a ray. 
#If the ray has an odd number of intersections with the graph, it is inside the graph, otherwise outside.
def seg_func(p: tuple, q: tuple, r: tuple) -> bool:
    if ((q[0] <= max(p[0], r[0])) &
            (q[0] >= min(p[0], r[0])) &
            (q[1] <= max(p[1], r[1])) &
            (q[1] >= min(p[1], r[1]))):
        return True
    return False
def o_function(p: tuple, q: tuple, r: tuple) -> int:
    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))

    if val == 0:
        return 0
    if val > 0:
        return 1
    else:
        return 2
#Check whether the inspection is carried out internally
def doIntersect(p1, q1, p2, q2):
    o1 = o_function(p1, q1, p2)
    o2 = o_function(p1, q1, q2)
    o3 = o_function(p2, q2, p1)
    o4 = o_function(p2, q2, q1)
    if (o1 != o2) and (o3 != o4):
        return True
    if (o1 == 0) and (seg_func(p1, p2, q1)):
        return True
    if (o2 == 0) and (seg_func(p1, q2, q1)):
        return True

    if (o3 == 0) and (seg_func(p2, p1, q2)):
        return True

    if (o4 == 0) and (seg_func(p2, q1, q2)):
        return True

    return False
#Judge whether it is inside
def is_in_p(points: list, p: tuple) -> bool:
    n = len(points)
    if n < 3:
        return False
    extreme = (max_num, p[1])
    count = i = 0
    while True:
        next = (i + 1) % n
        if (doIntersect(points[i],
                        points[next],
                        p, extreme)):
            if o_function(points[i], p,
                           points[next]) == 0:
                return seg_func(points[i], p,
                                 points[next])
            count += 1
        i = next
        if (i == 0):
            break
    return (count % 2 == 1)

if __name__ == '__main__':
    polygon = []
    points = []
    with open('./input_question_6_polygon','r')as f:
        tmp=f.readlines()
    for t in tmp:
        try:
            polygon.append(tuple(eval(','.join(t.split()))))
        except:
            pass
    with open('./input_question_6_points','r')as f:
        pt=f.readlines()

    for p_ in pt:
        try:
            points.append(tuple(eval(','.join(p_.split()))))
        except:
            pass
    res = []
    path = os.getcwd()
    if os.path.exists(os.path.join(path ,'output_question_6')):
        os.remove(os.path.join(path ,'output_question_6'))
    for p in points:
        if (is_in_p(points=polygon, p=p)):
            with open('output_question_6','a') as f:
                f.writelines(str(p).replace('(','').replace(')','').replace(',','') + ' inside')
                f.writelines('\n')
        else:
            with open('output_question_6','a') as f:
                f.writelines(str(p).replace('(','').replace(')','').replace(',','') + ' outside')
                f.writelines('\n')

