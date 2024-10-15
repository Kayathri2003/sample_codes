import math

def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def max_dist(points):
    max_d=0
    n=len(points)
    
    for i in range(n):
        for j in range(i+1,n):
            dist=distance(points[i],points[j])
            max_d=max(max_d,dist)
    return max_d

points = [(0, 0), (3, 4), (6, 8)]
print(max_dist(points)) 