from ast import literal_eval
import numpy as np
INCR = 10
# edit to the name of the input file
f = open('circlecovers3.txt', 'r')

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
    return np.linalg.norm(np.array(coords)-np.array(center)) <= r

active_points = points.copy()


for r in radii:
    max_x = -np.inf
    max_y = -np.inf
    min_x = np.inf
    min_y = np.inf
    for x,y in active_points:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    max_points = -np.inf
    best_center = None
    to_remove = None
    for x in np.arange(min_x-r,max_x+r,INCR):
        for y in np.arange(min_y-r,max_y+r,INCR):
        count = 0
        in_c = []
        for p in active_points:
            if inCircle([x,y],p,r):
                count += 1
                in_c.append(p)
        if count > max_points:
            max_points = count
            best_center = [x,y]
            to_remove = in_c.copy()
    centers.append(best_center)
    new_p = [p for p in active_points if p not in to_remove]
    active_points = new_p.copy()
    print(len(active_points))


# change to whatever you want your output file to be called
out = open('output3.txt', 'w')

for t in np.array(centers)[radii_indices]:
    out.write(str(t[0]) + ' '+ str(t[1]))
    out.write("\n")
out.close()
