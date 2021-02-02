from ast import literal_eval
from sklearn.cluster import KMeans
import numpy as np
import itertools
INCR = 10
# edit to the name of the input file
f = open('circlecovers6.txt', 'r')
c = open('output26.txt')

n = int(f.readline())
points = [f.readline() for _ in range(n)]

m = int(f.readline())
radii = [int(f.readline()) for _ in range(m)]

centers = [c.readline() for _ in range(m)]
c.close()
f.close()
# replace from here to line 18 with your own logic
# points is a list of tuples of the points, and radii is a list of radii

points = [i.strip().split(' ') for i in points]
points = [(int(i[0]), int(i[1])) for i in points]
centers = [i.strip().split(' ') for i in centers]
centers = [(float(i[0]), float(i[1])) for i in centers]
radii = np.array([int(i) for i in radii])
radii_indices = np.argsort(radii)[::-1]
radii = radii[radii_indices]
inverse = np.empty_like(radii_indices)
inverse[radii_indices] = np.arange(radii_indices.size)


# change to whatever you want your output file to be called
out = open('output26.txt', 'w')

for t in np.array(centers)[inverse][inverse]:
    out.write(str(t[0]) + ' '+ str(t[1]))
    out.write("\n")
out.close()
