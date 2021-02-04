from ast import literal_eval
import numpy as np
INCR = 1
# edit to the name of the input file
f = open('circlecovers3.txt', 'r')
print(INCR)
n = int(f.readline())
points = [f.readline() for _ in range(n)]

m = int(f.readline())
radii = [int(f.readline()) for _ in range(m)]

centers = []
# replace from here to line 18 with your own logic
# points is a list of tuples of the points, and radii is a list of radii

points = [i.strip().split(' ') for i in points]
points = [(int(i[0]), int(i[1])) for i in points]
radii = np.array([int(i) for i in radii])
radii_indices = np.argsort(radii)
radii = radii[radii_indices]
inverse = np.empty_like(radii_indices)
inverse[radii_indices] = np.arange(radii_indices.size)

def inCircle(center,coords,r):
    return np.linalg.norm(np.array(coords)-np.array(center)) <= r

active_points = points.copy()

def getCenters(point,r):
    centers = []
    r2 = r**2
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            if x**2 + y**2 < r2:
                centers.append((x,y))
    return [(c[0]+point[0],c[1]+point[1]) for c in centers]
for r in radii:
    c_points = {}
    for p in active_points:
        for c in getCenters(p,r):
            try:
                c_points[c].append(p)
            except KeyError:
                c_points[c] = [p]
    best_center = max(c_points, key=lambda k: len(c_points[k]))
    # print(c_points)
    new_points = [p for p in active_points if p not in c_points[best_center]]
    active_points = new_points.copy()
    centers.append(best_center)
    print(m-len(active_points))

# change to whatever you want your output file to be called
out = open('output23.txt', 'w')

for t in np.array(centers)[inverse]:
    out.write(str(t[0]) + ' '+ str(t[1]))
    out.write("\n")
out.close()
