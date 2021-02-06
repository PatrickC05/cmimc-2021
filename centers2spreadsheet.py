from ast import literal_eval
import numpy as np
import pandas as pd
INCR = 1
# edit to the name of the input file
print(INCR)
f = open('circlecovers3.txt', 'r')
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
df = pd.DataFrame(points)
df.to_csv('circles3.csv',index=False,header=False)

# change to whatever you want your output file to be called
# out = open('output25.txt', 'w')
#
# for t in np.array(centers)[inverse]:
#     out.write(str(t[0]) + ' '+ str(t[1]))
#     out.write("\n")
# out.close()
