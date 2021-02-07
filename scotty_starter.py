# Scotty Dog Starter File

# NOTE: You can run this file locally to test if your program is working.

#=============================================================================

# INPUT FORMAT: board

# board: A 15 x 15 2D array, where each element is:
#   0 - an empty square
#   1 - the current position of Scotty
#   2 - a naturally generated barrier
#   3 - a player placed barrier

# Example Input:

# board: See "SAMPLE_BOARD" below.

#=============================================================================

# OUTPUT FORMAT when scotty_bot is called:

# A list of two integers [dx, dy], designating in which
# direction you would like to move. Your output must satisfy

# -1 <= dx, dy <= 1

# and one of the following, where board[y][x] is Scotty's current position:

# max(x + dx, y + dy) >= 15 OR min(x + dx, y + dy) < 0 (move off the board)
# OR
# board[y + dy][x + dx] < 2 (move to an empty square or stay still)

# Invalid outputs will result in Scotty not moving.

#=============================================================================

# OUTPUT FORMAT when trapper_bot is called:

# A list of two integers [x, y], designating where you would
# like to place a barrier. The square must be currently empty, i.e.
# board[y][x] = 0

# Invalid outputs will result in no barrier being placed.

### WARNING: COMMENT OUT YOUR DEBUG/PRINT STATEMENTS BEFORE SUBMITTING !!!
### (this file uses standard IO to communicate with the grader!)

#=============================================================================

# Write your bots in the scotty_bot and trapper_bot classes. Helper functions
# and standard library modules are allowed, and can be written before/inside
# these classes.

# You can define as many different strategies as you like, but only the classes
# currently named "scotty_bot" and "trapper_bot" will be run officially.


# Example Scotty bot that makes a random move:
from collections import deque
import random
class scotty_bot:

    def __init__(self):
        self.visited = []
        pass

    def find_scotty(self, board):
        # Helper function that finds Scotty's location on the board
        for r in range(15):
            for c in range(15):
                if board[r][c] == 1:
                    return (r, c)

    def move(self, board):
        # You should write your code that moves every turn here
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1), (1,-1), (-1, -1), (-1, 1), (1, 1)]

        r,c = self.find_scotty(board)
        if r == 0:
            return [0,-1]
        elif r == 14:
            return [0,1]
        elif c == 0:
            return [-1,0]
        elif c == 14:
            return [1,0]

        dists = [[100000 for i in range(15)] for j in range(15)]
        par = [[100000 for i in range(15)] for j in range(15)]
        queue = deque([(r, c)])
        dists[r][c] = 0

        while queue:
            cur = queue.popleft()

            for i in range(8):
                nr = cur[0] + moves[i][0]
                nc = cur[1] + moves[i][1]

                if nr<0 or nc < 0:
                    continue
                if nr > 14 or nc > 14:
                    continue
                if board[nr][nc]!=0:
                    continue
                if dists[nr][nc]!=100000:
                    continue
                dists[nr][nc]=dists[cur[0]][cur[1]]+1
                par[nr][nc] = [cur[0], cur[1]]
                queue.append((nr, nc))

        # assert dists[0][0]!=100000
        bestDist = 100000
        exit = [0,0]

        for i in range(15):
            if dists[0][i]<bestDist:
                exit = [0, i]
                bestDist = dists[0][i]
            if dists[14][i]<bestDist:
                exit = [14, i]
                bestDist = dists[14][i]
            if dists[i][0]<bestDist:
                exit = [i, 0]
                bestDist = dists[i][0]
            if dists[i][14]<bestDist:
                exit = [i, 14]
                bestDist = dists[i][14]

        if bestDist==100000:
            return 0, 0

        while True:
            nr, nc = par[exit[0]][exit[1]]
            if nr==r and nc==c:
                break
            else:
                exit = [nr, nc]
        return [exit[1]-c,exit[0]-r]
        # return [1, 1]

# Example trapper bot that places a barrier randomly:

class trapper_bot:

    def __init__(self):
        # You can define global states (that last between moves) here
        pass
    def find_scotty(self, board):
        # Helper function that finds Scotty's location on the board
        for y in range(15):
            for x in range(15):
                if board[y][x] == 1:
                    return (x, y)

    def move(self, board):
        tmp = scotty_bot()
        move = tmp.move(board)
        pos = self.find_scotty(board)
        if move==(0,0):
            moves = [(-1, 0), (0, 1), (1, 0), (0, -1), (1,-1), (-1, -1), (-1, 1), (1, 1)]
            for i in range(8):
                nx = pos[0] + moves[i][0]
                ny = pos[1] + moves[i][1]
                if board[ny][nx]==0:
                    return nx, ny
        else:
            return pos[0] + move[0], pos[1] + move[1]



#=============================================================================

# Local testing parameters

# If you would like to view a turn by turn game display while testing locally,
# set this parameter to True

LOCAL_VIEW = True

# Sample board your game will be run on (flipped vertically)
# This file will display 0 as ' ', 1 as '*', 2 as 'X', and 3 as 'O'

SAMPLE_BOARD = [
    [0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2],
    [0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 2, 0, 2, 0, 2],
    [0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2],
    [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 2, 0, 2, 2, 2, 0, 2, 0, 0],
    [2, 2, 0, 2, 2, 2, 0, 1, 0, 0, 2, 0, 0, 2, 0],
    [2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    [2, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2],
    [0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0]]

#=============================================================================












































# You don't need to change any code below this point

import json
import sys

def WAIT():
    return json.loads(input())

def SEND(data):
    print(json.dumps(data), flush=True)

def dispboard_for_tester(board):
    print()
    print('\n'.join(''.join(map(lambda x:' *XO'[x],i))for i in reversed(board)))
    print()

def find_scotty_for_tester(board):
    for y in range(15):
        for x in range(15):
            if board[y][x] == 1:
                return (x, y)

def trapped_for_tester(board):
    pos = find_scotty_for_tester(board)
    moves = [*zip([0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1])]
    trap = True
    for i in moves:
        if 0 <= pos[0] + i[0] < 15 and 0 <= pos[1] + i[1] < 15:
            if board[pos[1] + i[1]][pos[0] + i[0]] == 0:
                trap = False
                break
        else:
            trap = False
            break
    return trap

def PLAY(scotty, trapper, board):
    result = -1
    while True:
        try:
            val = trapper.move(board)
            if not (val[0] == int(val[0]) and 0 <= val[0] < 15
                and val[1] == int(val[1]) and 0 <= val[1] < 15
                and board[val[1]][val[0]] == 0):
                raise Exception('invalid move')
            board[val[1]][val[0]] = 3
        except Exception as e:
            print(f'Your trapper has an error: {e}! Doing nothing instead.')
            val = -1
        if trapped_for_tester(board):
            result = 1
            break
        if LOCAL_VIEW:
            dispboard_for_tester(board)
            input("Enter to continue (change LOCAL_VIEW to toggle this)")
        try:
            val = scotty.move(board)
            if not (val[0] == int(val[0]) and -1 <= val[0] <= 1
                and val[1] == int(val[1]) and -1 <= val[1] <= 1):
                    raise Exception('invalid move')
        except Exception as e:
            print(f'Your Scotty has an error: {e}! Doing nothing instead.')
            val = (0, 0)
        pos = find_scotty_for_tester(board)
        if 0 <= pos[0] + val[0] < 15 and 0 <= pos[1] + val[1] < 15:
            if board[pos[1] + val[1]][pos[0] + val[0]] == 0:
                board[pos[1] + val[1]][pos[0] + val[0]] = 1
                board[pos[1]][pos[0]] = 0
        else:
            board[pos[1]][pos[0]] = 0
            result = 0
            break
        if LOCAL_VIEW:
            dispboard_for_tester(board)
            input("Enter to continue (change LOCAL_VIEW to toggle this)")
    print(["Scotty", "Trapper"][result], "won!")
    if not LOCAL_VIEW:
        print("Change LOCAL_VIEW to True to see a turn by turn replay")

if len(sys.argv) < 2 or sys.argv[1] != 'REAL':
    PLAY(scotty_bot(), trapper_bot(), SAMPLE_BOARD)
    input()

else:
    scotty = scotty_bot()
    trapper = trapper_bot()
    while True:
        data = WAIT()
        board = data["board"]
        role = data["role"]
        if role == "trapper":
            SEND(trapper.move(board))
        else:
            SEND(scotty.move(board))
