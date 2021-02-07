import math
x = -8
y = 0
status = -1
moves = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
def addedAngle(x,y,newx,newy):
    old_angle = math.atan2(y,x)
    new_angle = math.atan2(newy,newx)
    if old_angle > math.pi/2 and new_angle<-math.pi/2:
        return (2*math.pi + new_angle - old_angle)*status
    elif new_angle > math.pi/2 and old_angle < -math.pi/2:
        return (new_angle-old_angle-2*math.pi)*status
    else:
        return (new_angle-old_angle)*status
move_dict = {(x+move[0],y+move[1]): addedAngle(x, y, x+move[0],y+move[1]) for move in moves}
print(move_dict)
sorted_locs = [loc for loc, dist in sorted(move_dict.items(),key=lambda k: -k[1])]
print(sorted_locs)
