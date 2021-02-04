from ast import literal_eval
import numpy as np
from dijkstar import Graph, find_path
import random
# edit to the name of the input file
f = open('robotrecovery2.txt', 'r')
# change this function however you want: it takes in a character representing a cell
# of the maze and x/y coordinates and returns whatever representation you want
def rep(c,x,y):
    if c == '.':
        return c
    elif c == 'X':
        return c
    elif c == 'R':
        robots.append([x,y])
        return c
    elif c == 'E':
        entrance.append([x,y])
        return c
# you shouldn't need to edit lines 18-25
r,c,n = map(int, f.readline().strip().split())
robots = []
entrance = []
maze = []
instructions = []
for y in range(r):
    s = f.readline().strip()
    maze.append([rep(s[x],x,y) for x in range(c)])
maze = np.array(maze)
isWall = maze == "X"
isWall = np.pad(isWall, pad_width=1, mode='constant', constant_values=True)
# replace from here to line 30 with your own logic
graph = Graph()
for y in range(1,r+1):
    for x in range(1,c+1):
        if not isWall[y][x]:
            try:
                if not isWall[y][x+1]:
                    graph.add_edge((x,y),(x+1,y),"R")
            except IndexError:
                pass
            try:
                if not isWall[y][x-1]:
                    graph.add_edge((x,y),(x-1,y),"L")
            except IndexError:
                pass
            try:
                if not isWall[y+1][x]:
                    graph.add_edge((x,y),(x,y+1),"D")
            except IndexError:
                pass
            try:
                if not isWall[y-1][x]:
                    graph.add_edge((x,y),(x,y-1),"U")
            except IndexError:
                pass
print('graph created')
def cost_func(u, v, edge, prev_edge):
    return 1
entrance = (entrance[0][0]+1,entrance[0][1]+1)
robots = [(r[0]+1,r[1]+1) for r in robots]
# path = find_path(graph,robots[0],entrance,cost_func=cost_func)
# instructions = path.edges

def moveRobot(coords,move):
    if move == "R":
        if not isWall[coords[1],coords[0]+1]:
            return coords[0]+1,coords[1]
    elif move == "L":
        if not isWall[coords[1],coords[0]-1]:
            return coords[0]-1,coords[1]
    elif move == "U":
        if not isWall[coords[1]-1,coords[0]]:
            return coords[0],coords[1]-1
    elif move == "D":
        if not isWall[coords[1]+1,coords[0]]:
            return coords[0],coords[1]+1
    return coords
active_bots = robots.copy()
while len(active_bots) > 0:
    min_bot = np.argmin([(np.absolute(r[0]-entrance[0]))**2+(np.absolute(r[1]-entrance[1]))**2 for r in active_bots])
    new_instructions = find_path(graph,active_bots[min_bot],entrance,cost_func=cost_func).edges
    new_bots = []
    for r in active_bots:
        done = False
        cur_loc = r
        for move in new_instructions:
            cur_loc = moveRobot(cur_loc,move)
            if cur_loc == entrance:
                done = True
                break
        if not done:
            new_bots.append(cur_loc)
    active_bots = new_bots.copy()
    instructions += new_instructions
    print(len(active_bots))
# change to whatever you want your output file to be called
print(len(instructions))
out = open('output32.txt', 'w')
for i in instructions:
    out.write(i)
out.close()
