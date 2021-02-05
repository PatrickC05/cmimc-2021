from ast import literal_eval
import numpy as np
INCR = 1
# edit to the name of the input file
print(INCR)
f = open('circlecovers6.txt', 'r')
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
    r2 = r**2
    yield point
    for i in np.arange(1,r+INCR,INCR):
        yield i+point[0],point[1]
        yield point[0]-i,point[1]
        yield point[0],point[1]+i
        yield point[0],point[1]-i
    for x in np.arange(1,r+INCR,INCR):
        for y in np.arange(x,r+INCR,INCR):
            if x**2 + y**2 < r2:
                yield x+point[0],y+point[1]
                yield point[0]-x,y+point[1]
                yield point[0]+x,point[1]-y
                yield point[0]-x,point[1]-y
                if x!=y:
                    yield y+point[0],x+point[1]
                    yield point[0]-y,x+point[1]
                    yield point[0]+y,point[1]-x
                    yield point[0]-y,point[1]-x
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
    print(n-len(active_points))

# change to whatever you want your output file to be called
out = open('output26.txt', 'w')

for t in np.array(centers)[inverse]:
    out.write(str(t[0]) + ' '+ str(t[1]))
    out.write("\n")
out.close()
