from ast import literal_eval
from sklearn.cluster import KMeans
import numpy as np
import itertools
INCR = 10
# edit to the name of the input file
f = open('circlecovers4.txt', 'r')

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
radii_indices = np.argsort(radii)[::-1]
radii = np.sort(radii)[::-1]

def inCircle(center,coords,r):
    return np.linalg.norm(np.array(coords)-center) <= r


kmeans = KMeans(len(radii),n_init=1000, max_iter=10000).fit(points)
kcenters=kmeans.cluster_centers_.tolist()
active_points = points.copy()

active_points = points.copy()
active_centers = kcenters.copy()

for r in radii:
    best_center = None
    to_remove = None
    max_points = -1
    for c in active_centers:
        count = 0
        in_c = []
        for p in active_points:
            if inCircle(c,p,r):
                count += 1
                in_c.append(p)
        if count > max_points:
            max_points = count
            best_center = c
            to_remove = in_c.copy()
    centers.append(best_center)

    new_p = [p for p in active_points if p not in to_remove]
    active_points = new_p.copy()
    active_centers.remove(best_center)


    print(n-len(active_points))

# change to whatever you want your output file to be called
out = open('output24.txt', 'w')

for t in np.array(centers)[radii_indices]:
    out.write(str(t[0]) + ' '+ str(t[1]))
    out.write("\n")
out.close()
