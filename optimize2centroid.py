from ast import literal_eval
import numpy as np
INCR = 10
# edit to the name of the input file
f = open('circlecovers6.txt', 'r')

n = int(f.readline())
points = [f.readline() for _ in range(n)]

m = int(f.readline())
radii = [int(f.readline()) for _ in range(m)]

centers = []
# replace from here to line 18 with your own logic
# points is a list of tuples of the points, and radii is a list of radii

points = [i.strip().split(' ') for i in points]
points = [[int(i[0]), int(i[1])] for i in points]
radii = np.array([int(i) for i in radii])
radii_indices = np.argsort(radii)[::-1]
radii = np.sort(radii)[::-1]

def inCircle(center,coords,r):
    return np.linalg.norm(np.array(coords)-center) <= r

active_points = points.copy()


for r in radii:
    c = active_points[2*len(active_points)//3]
    new_points = [p for p in active_points if not inCircle(c,p,r)]
    active_points = new_points.copy()
    centers.append(c)
    print(len(active_points))


# change to whatever you want your output file to be called
out = open('output6.txt', 'w')

for t in np.array(centers)[radii_indices]:
    out.write(str(t[0]) + ' '+ str(t[1]))
    out.write("\n")
out.close()
