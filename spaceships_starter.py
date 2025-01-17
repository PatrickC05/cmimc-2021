# Spaceship Starter File

# NOTE: You can run this file locally to test if your program is working.

#===============================================================================

# INPUT FORMAT: ship, others

# ship: A list of length 4 consisting of [x, y, status, score], where

#   x, y is your current position

#   status = 1 if your goal is to travel counterclockwise
#   status = -1 if your goal is to travel clockwise
#   status = 0 if you have crashed

#   score = Number of times you have orbited the center in your target direction

# others: A list containing all other players' ships, in a fixed order. Each
#   ship is given in the same format as your ship, i.e. a list of length 4.

# Example input:

# ship: [3, 5, -1, 1.1]
# others: [[4, 4, 1, -1.3], [4, 6, 0, 0.1], [4, 6, 0, -0.3]]

#=============================================================================

# OUTPUT FORMAT: A list of two integers dx, dy satisfying dx^2 + dy^2 = 5.
# Your spaceship will move to the square x + dx, y + dy.

# Invalid outputs will result in the move you previously played being played
# again, with the exception of the first move, where a random move will be
# played instead.

### WARNING: COMMENT OUT YOUR DEBUG/PRINT STATEMENTS BEFORE SUBMITTING !!!
### (this file uses standard IO to communicate with the grader!)

#===============================================================================

# Write your bot in the spaceship_bot class. Helper functions and standard
# library modules are allowed, and can be written before before/inside these
# classes.

# You can define as many different strategies as you like, but only the class
# currently named "spaceship_bot" will be run officially.


# Example bot that moves in a random direction every round:

import random
import math

def safeFromSun(x,y,move):
    return abs(x+move[0]) > 2.5 and abs(y+move[1]) > 2.5

class spaceship_bot:

    def __init__(self):

        # You can define global states (that last between moves) here
        self.moves = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]

    def manDist(self,x, y):
        return abs(x) + abs(y)

    def addedAngle(self,x,y,newx,newy):
        old_angle = math.atan2(y,x)
        new_angle = math.atan2(newy,newx)
        if old_angle > math.pi/2 and new_angle<-math.pi/2:
            return (2*math.pi + new_angle - old_angle)*self.status
        elif new_angle > math.pi/2 and old_angle < -math.pi/2:
            return (new_angle-old_angle-2*math.pi)*self.status
        else:
            return (new_angle-old_angle)*self.status

    def precomputeCrashable(self,others):
        crashable = []
        for other_x, other_y, status, _ in others:
            if status != 0:
                for i in range(8):
                    crashable.append((other_x + self.moves[i][0], other_y + self.moves[i][1]))
        self.canCrash = set(crashable)

    def willCrash(self,x, y):
        if min(abs(x),abs(y)) < 3:
            return True
        return (x,y) in self.canCrash

    def move(self, ship, others):
        x, y, self.status, score = ship
        if self.manDist(x, y)>7:
            move_dict = {(x+m[0],y+m[1]): self.manDist(x+m[0],y+m[1]) for m in self.moves}
            sorted_locs = [loc for loc, dist in sorted(move_dict.items(),key=lambda k: k[1])]
        else:
            move_dict = {(x+m[0],y+m[1]): self.addedAngle(x, y, x+m[0],y+m[1]) for m in self.moves}
            sorted_locs = [loc for loc, dist in sorted(move_dict.items(),key=lambda k: -k[1])]

        self.precomputeCrashable(others)

        for new_x,new_y in sorted_locs:
            if not self.willCrash(new_x,new_y):
                return new_x-x, new_y-y
        return sorted_locs[0][0]-x, sorted_locs[0][1]-y

#=============================================================================

# Local testing parameters

# If you would like to view a turn by turn game display while testing locally,
# set this parameter to True

LOCAL_VIEW = True

# Set the size of the area (around the origin) you would like to display, as a
# square of side length 2 * SIDE + 1
# The first ship will be displayed as "1", other ships will be displayed as "0",
# crashed ships will be displayed as "X", and the sun will be displayed as "S".

SIDE = 10

# Set a list of (arbitrarily many) strategies you would like to test locally

LOCAL_STRATS = [
    spaceship_bot(),
    spaceship_bot(),
    spaceship_bot(),
    spaceship_bot(),
    spaceship_bot(),
    spaceship_bot()
    ]

# Set how many rounds you would like the game to run for (official is 500)

ROUNDS = 10

#=============================================================================












































# You don't need to change any code below this point

import json
import sys
import random
import math
import copy

def WAIT():
    return json.loads(input())

def SEND(data):
    print(json.dumps(data), flush=True)

def dispboard_for_tester(board):
    print()
    print('\n'.join(' '.join(i) for i in board))
    print()

MASK = lambda a,i:a[:i]+a[i+1:]
LEGAL = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
SIDES = 2*SIDE+1

def PLAY(playerlist):
    n = len(playerlist)
    players = [(playerlist[i],i) for i in range(n)]
    random.shuffle(players)
    r = max(8,n)
    ships = [[0]*4 for i in range(n)]
    moves = [random.choice(LEGAL) for i in range(n)]
    history = []
    off = 2*math.pi*random.random()/n
    for i in range(n):
        theta = i*2*math.pi/n+off
        x,y = int(r*math.sin(theta)),int(r*math.cos(theta))
        if (x+y)%2:
            if random.choice((0,1)):
                x += random.choice((-1,1))
            else:
                y += random.choice((-1,1))
        ships[i][0] = x
        ships[i][1] = y
        ships[i][2] = 2*(i%2)-1
    board = [[' ']*SIDES for i in range(SIDES)]
    for i in range(SIDE-2, SIDE+3):
        for j in range(SIDE-2, SIDE+3):
            board[i][j] = 'S'
    for _ in range(ROUNDS):
        chips=copy.deepcopy(ships)
        history.append(chips)
        for i in range(SIDES):
            for j in range(SIDES):
                if board[i][j] in '01':
                    board[i][j]='.'
        for i in range(n):
            if ships[i][2]:
                player = players[i][0]
                try:
                    move = player.move(chips[i], MASK(chips,i))
                    if move not in LEGAL:
                        raise Exception("invalid move")
                    moves[i] = move
                except Exception as e:
                    print(f"Player {players[i][1]} has an error: {e}! Defaulting to previous move.")
                    print(e)
                oldx, oldy = ships[i][0],ships[i][1]
                ships[i][0] += moves[i][0]
                ships[i][1] += moves[i][1]
                newx, newy = ships[i][0],ships[i][1]
                if -2 <= newx <= 2 and -2 <= newy <= 2:
                    ships[i][2] = 0
                else:
                    delta = math.atan2(newy,newx)-math.atan2(oldy,oldx)
                    if delta<-math.pi:
                        delta += 2*math.pi
                    elif delta>math.pi:
                        delta -= 2*math.pi
                    delta *= ships[i][2]
                    ships[i][3] += delta/(2*math.pi)
                    if abs(ships[i][0]) <= SIDE and abs(ships[i][1]) <= SIDE:
                        board[SIDE-ships[i][1]][SIDE+ships[i][0]]='1' if players[i][1]==0 else '0'
            else:
                if abs(ships[i][0]) <= SIDE and abs(ships[i][1]) <= SIDE:
                    if not (-2 <= ships[i][0] <= 2 and -2 <= ships[i][1] <= 2):
                        board[SIDE-ships[i][1]][SIDE+ships[i][0]]='X'
        if LOCAL_VIEW:
            dispboard_for_tester(board)
            input("Enter to continue (change LOCAL_VIEW to toggle this)")
        for i in range(n):
            for j in range(i):
                if ships[i][0]==ships[j][0] and ships[i][1]==ships[j][1]:
                    ships[i][2] = 0
                    ships[j][2] = 0
    scores = sorted((players[i][1],ships[i][3]) for i in range(n))
    final = [x[1] for x in scores]
    print("Final scores:")
    print('\n'.join(map(str,final)))
    if not LOCAL_VIEW:
        print("Change LOCAL_VIEW to True to see a turn by turn replay")

if len(sys.argv) < 2 or sys.argv[1] != 'REAL':
    PLAY(LOCAL_STRATS)
    input()

else:
    player = spaceship_bot()
    while True:
        data = WAIT()
        play = player.move(data["ship"], data["others"])
        SEND(play)
